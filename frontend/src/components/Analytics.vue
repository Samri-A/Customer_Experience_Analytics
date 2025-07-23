<script setup>
import { marked} from 'marked'
import { ref, onMounted, computed } from 'vue'
import { useAnalyticsStore } from '@/stores/analytics'
import {
  Chart,
  BarController,
  BarElement,
  CategoryScale,
  LineElement,
  LineController,
  PointElement,
  LinearScale,
  Title,
  Tooltip,
  Legend
} from 'chart.js'

Chart.register(BarController, BarElement, CategoryScale , LineElement, LineController, PointElement, LinearScale, Title, Tooltip, Legend)

// Store
const store = useAnalyticsStore()

// Define refs
const themeValues = ref([])
const themeLabels = ref([])
const rating_labels = ref([])
const rating_values = ref([])
const Painpoints = ref([])
const Drivers = ref([])
const message = ref('')
const app_id = ref('')
const messages = ref([
  { sender: 'ai', text: 'Hi, I am your review assistant. Ask me about the app user feedback!' }
])
const showChat = ref(false)
const runQuery = async()=>{
        const userMsg = message.value.trim()
        if (!userMsg) return
        messages.value.push({ sender: 'user', text: userMsg })
        message.value = ''
        const id = app_id.value
       
        try {
        const response = await fetch('http://localhost:8000/api/ask', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ userMsg , id })
        })
        const data = await response.json()
        const txt = marked(data.reply)
        messages.value.push({ sender: 'ai', text:  txt})
      } catch (err) {
        messages.value.push({
        sender: 'ai',
        text: "Sorry, I couldn't reach the server. Try again later."
       })
       console.error('Chat error:', err)
      }
      }
    

onMounted(async () => {
  await store.analyser() 
  themeValues.value = store.theme_values
  themeLabels.value = store.theme_labels
  rating_labels.value = store.rating_labels
  rating_values.value = store.rating_values
  Painpoints.value = store.painpoints
  Drivers.value = store.drivers
  app_id.value = store.app_id
  const sentiment_data = computed(() => store.sentiment_data)
  console.log(sentiment_data)
  createBarChart('chart1', 'Distribution of Themes in App Reviews' , themeLabels , themeValues)
  createHBarChart('chart3', 'Rating Distribution' , rating_labels , rating_values)
  createSentimentLineChart('chart2' , sentiment_data)
})
function getColorBySentiment(sentiment) {
  switch (sentiment.toLowerCase()) {
    case 'positive':
      return 'rgba(158, 48, 169, 1)'  
    case 'negative':
      return 'rgba(255, 99, 132, 1)'
    case 'neutral':
      return 'rgba(201, 203, 207, 1)'
    default:
      return 'rgba(100, 100, 255, 1)' 
  }
}

const createSentimentLineChart =(id , timedata)=>{

   const ctx = document.getElementById(id)
   if (!ctx || !timedata.value?.labels?.length || !timedata.value?.datasets?.length) return
   new Chart(ctx, {
    type: 'line',
    data: {
      labels: timedata.value.labels,
      datasets: timedata.value.datasets.map(dataset => ({
        ...dataset,
        fill: false,
        tension: 0.3,
        pointStyle: 'circle',
        borderColor: getColorBySentiment(dataset.label),
      })),
    },
    options: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: 'Sentiment across Years',
        },
      },
      scales: {
        y: {
          title: {
            display: true,
            text: 'Count',
          },
        },
        x: {
          title: {
            display: true,
            text: 'Year',
          },
        },
      },
    },
  });
  
      

}


const createBarChart = (id, label , labels_ , value) => {
  const ctx = document.getElementById(id)
  if (!ctx || !themeLabels.value.length) return

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels_.value,
      datasets: [{
        label,
        data: value.value,
        backgroundColor: '#9e30a9'
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
      legend: {
        labels: {
          boxWidth: 0, 
          color: 'white'
        }
       }
       },
      scales: {
        x: {
        },
        y: {
          beginAtZero: true,
          ticks: { color: 'white' },
          grid: { color: 'rgba(255,255,255,0.1)' }
        }
      }

    }
  })
}
const createHBarChart = (id, label , labels_ , value) => {
  const ctx = document.getElementById(id)
  if (!ctx || !themeLabels.value.length) return

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels_.value,
      datasets: [{
        label,
        data: value.value,
        backgroundColor: '#9e30a9'
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      indexAxis: 'y',
      plugins: {
      legend: {
        labels: {
          boxWidth: 0, 
          color: 'white'
        }
       }
       }

    }
  })
}
</script>


<template>
  <div class="bg-black">
    <!-- Header -->
    <div class="fixed top-10 left-10 z-50 flex items-center gap-2">
      <div class="flex h-10 w-10 items-center justify-center rounded-lg bg-gradient-to-br from-[#4090b5] to-pink-500">
        <svg class="h-5 w-5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" />
        </svg>
      </div>
      <h3 class="text-base font-mono text-white">App Review Analytics</h3>
    </div>

    <!-- 2x2 Chart Grid -->
    <div class="bg-black w-full">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-16 mt-20 w-full">
      <div class=" rounded-lg p-4 h-[400px]">
        <h4 class="font-mono"> Themes </h4>
        <canvas id="chart1" class="w-full h-full"></canvas>
        
      </div>
      <div class="rounded-lg p-4 h-[400px]">
        <h4 class="font-mono">Sentiment Trends Over Time in User Reviews</h4>
        <canvas id="chart2" class="w-full h-full"></canvas>
      </div>
      <div class=" rounded-lg p-4 h-[400px]">
        <h4 class="font-mono"> Rating</h4>
        <canvas id="chart3" class="w-full h-full"></canvas>
      </div>
      <div class=" rounded-lg p-4 h-[400px]">
        <h4 class="font-mono">Painpoints</h4>
           <ul>
            <li v-for="(item , index ) in Painpoints" :key="index">
               {{item}}
            </li>
           </ul>
         <h4 class="font-mono">Drivers</h4>
         <ul>
          <div></div>
            <li v-for="(item , index ) in Drivers" :key="index">
               {{item}}
            </li>
           </ul>
      </div>
    </div>
     <!-- component -->
<button @click= "showChat = !showChat"
    class="fixed bg-transparent bottom-14 right-14 inline-flex items-center justify-center disabled:pointer-events-none disabled:opacity-50 hover:bg-gray-700 m-0 cursor-pointer bg-none p-0 normal-case leading-5 hover:text-gray-900"
    type="button" aria-haspopup="dialog" aria-expanded="false" data-state="closed">
    <svg xmlns=" http://www.w3.org/2000/svg" width="30" height="40" viewBox="0 0 24 24" fill="none"
      stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
      class="text-white block border-gray-200 align-middle">
      <path d="m3 21 1.9-5.7a8.5 8.5 0 1 1 3.8 3.8z" class="border-gray-200">
      </path>
    </svg>
    Ask
  </button>

   <!-- Chat Window -->
<div
  v-if="showChat"
  class="fixed bottom-24 right-4 w-[90vw] max-w-[440px] max-h-[80vh] bg-black text-white rounded-xl shadow-2xl flex flex-col justify-between border border-gray-700 overflow-hidden z-50"
>
  <!-- Header -->
  <div class="bg-black-900 text-white p-4 font-semibold">User Review Chat</div>

  <!-- Chat Messages -->
  <div class="p-4 overflow-y-auto flex-1 space-y-3">
    <div
      v-for="(msg, index) in messages"
      :key="index"
      :class="msg.sender === 'user' ? 'flex justify-end' : 'flex justify-start'"
    >
      <div v-html="msg.text"
        :class="msg.sender === 'user'
          ? 'bg-blue-700 text-white'
          : 'bg-gray-800 text-white'"
        class="px-4 py-2 rounded-lg max-w-[75%] break-words"
      >
      </div>
    </div>
  </div>

  <!-- Input Section -->
  <form @submit.prevent="runQuery" class="p-4 border-t border-gray-700 flex gap-2 bg-black-900">
    <input
      v-model="message"
      type="text"
      class="flex-grow px-3 py-2 border border-gray-600 rounded-md bg-black text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500"
      placeholder="Type your message..."
    />
    <button
      type="submit"
      class="bg-black-700 text-white px-4 py-2 rounded-md hover:bg-blue-800"
    >
      Send
    </button>
  </form>
</div>

    


    </div>
  </div>
</template>
