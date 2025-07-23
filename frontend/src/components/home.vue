<template>
    <form class="container" @submit.prevent="handleSubmit">
  <div class="input-container">
    <div class="input-content">
      <div class="input-dist">
        <div class="input-type">
          <input
            v-model="appid"
            class="input-is"
            id = "appid"
            type="text"
            required
            placeholder="Play Store App ID"
          />
        </div>
      </div>
    </div>
  </div>
  <button class="submit-button" type="submit" :disabled="isloading">Analyze App</button>
</form>
<p v-if="error" class="text-red-500 text-sm mt-2">{{ error }}</p> 
<div v-if="isloading" class="loader mx-auto w-64">
    <div class="bar1"></div>
    <div class="bar2"></div>
    <div class="bar3"></div>
    <div class="bar4"></div>
    <div class="bar5"></div>
    <div class="bar6"></div>
    <div class="bar7"></div>
    <div class="bar8"></div>
    <div class="bar9"></div>
    <div class="bar10"></div>
    <div class="bar11"></div>
    <div class="bar12"></div>
</div>

</template>

<script>
import { useAnalyticsStore } from '@/stores/analytics'

export default {
  data() {
    return {
      appid: '',
      error: '',
      isloading: false,
    }
  },
  methods: {
    async handleSubmit() {
      this.isloading = true
      const store = useAnalyticsStore()
      const success = await store.analyser(this.appid)
      this.isloading = false
      if (success) {
        this.$router.push('/analytics')
      } else {
        this.error = store.error || 'Failed to analyze app'
      }
    }
  }
}

</script>

<style>
.container {
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  font-style: italic;
  font-weight: bold;
  display: flex;
  margin: auto;
  aspect-ratio: 16/9;
  align-items: center;
  justify-items: center;
  justify-content: center;
  flex-wrap: nowrap;
  flex-direction: column;
  gap: 1em;
}

.input-container {
  filter: drop-shadow(46px 36px 24px #4090b5)
    drop-shadow(-55px -40px 25px #9e30a9);
  animation: blinkShadowsFilter 8s ease-in infinite;
}

.input-content {
  display: grid;
  align-content: center;
  justify-items: center;
  align-items: center;
  text-align: center;
  padding-inline: 1em;
}

.input-content::before {
  content: "";
  position: absolute;
  width: 100%;
  height: 100%;
  filter: blur(40px);
  -webkit-clip-path: polygon(
    26% 0,
    66% 0,
    92% 0,
    100% 8%,
    100% 89%,
    91% 100%,
    7% 100%,
    0 92%,
    0 0
  );
  clip-path: polygon(
    26% 0,
    66% 0,
    92% 0,
    100% 8%,
    100% 89%,
    91% 100%,
    7% 100%,
    0 92%,
    0 0
  );
  background: rgba(122, 251, 255, 0.5568627451);
  transition: all 1s ease-in-out;
}

.input-content::after {
  content: "";
  position: absolute;
  width: 98%;
  height: 98%;
  box-shadow: inset 0px 0px 20px 20px #212121;
  background: repeating-linear-gradient(
      to bottom,
      transparent 0%,
      rgba(64, 144, 181, 0.6) 1px,
      rgb(0, 0, 0) 3px,
      hsl(295, 60%, 12%) 5px,
      #153544 4px,
      transparent 0.5%
    ),
    repeating-linear-gradient(
      to left,
      hsl(295, 60%, 12%) 100%,
      hsla(295, 60%, 12%, 0.99) 100%
    );
  -webkit-clip-path: polygon(
    26% 0,
    31% 5%,
    61% 5%,
    66% 0,
    92% 0,
    100% 8%,
    100% 89%,
    91% 100%,
    7% 100%,
    0 92%,
    0 0
  );
  clip-path: polygon(
    26% 0,
    31% 5%,
    61% 5%,
    66% 0,
    92% 0,
    100% 8%,
    100% 89%,
    91% 100%,
    7% 100%,
    0 92%,
    0 0
  );
  animation: backglitch 50ms linear infinite;
}

.input-dist {
  z-index: 80;
  display: grid;
  align-items: center;
  text-align: center;
  width: 100%;
  padding-inline: 1em;
  padding-block: 1.2em;
  grid-template-columns: 1fr;
}

.input-type {
  display: flex;
  flex-wrap: wrap;
  flex-direction: column;
  gap: 1em;
  font-size: 1.1rem;
  background-color: transparent;
  width: 100%;
  border: none;
}

.input-is {
  color: #fff;
  font-size: 0.9rem;
  background-color: transparent;
  width: 100%;
  box-sizing: border-box;
  padding-inline: 0.5em;
  padding-block: 0.7em;
  border: none;
  transition: all 1s ease-in-out;
  border-bottom: 1px solid hsl(221, 26%, 43%);
}

.input-is:hover {
  transition: all 1s ease-in-out;
  background: linear-gradient(
    90deg,
    transparent 0%,
    rgba(102, 224, 255, 0.2) 27%,
    rgba(102, 224, 255, 0.2) 63%,
    transparent 100%
  );
}

.input-content:focus-within::before {
  transition: all 1s ease-in-out;
  background: hsla(0, 0%, 100%, 0.814);
}

.input-is:focus {
  outline: none;
  border-bottom: 1px solid hsl(192, 100%, 100%);
  color: hsl(192, 100%, 88%);
  background: linear-gradient(
    90deg,
    transparent 0%,
    rgba(102, 224, 255, 0.2) 27%,
    rgba(102, 224, 255, 0.2) 63%,
    transparent 100%
  );
}

.input-is::-moz-placeholder {
  color: hsla(192, 100%, 88%, 0.806);
}

.input-is::placeholder {
  color: hsla(192, 100%, 88%, 0.806);
}

.submit-button {
  width: 50%;
  border: none;
  color: hsla(192, 100%, 88%, 0.806);
  background: linear-gradient(
    90deg,
    transparent 0%,
    rgba(102, 224, 255, 0.2) 27%,
    rgba(102, 224, 255, 0.2) 63%,
    transparent 100%
  );
  clip-path: polygon(0 0, 85% 0%, 100% 0, 100% 15%, 100% 90%, 91% 100%, 0 100%);
  padding: 0.5em;
  animation: blinkShadowsFilter 0.5s ease-in infinite;
  transition: all 500ms;
}

.submit-button:hover {
  color: hsl(0, 0%, 100%);
  cursor: pointer;
  font-size: medium;
  font-weight: bold;
}

@keyframes backglitch {
  0% {
    box-shadow: inset 0px 20px 20px 30px #212121;
  }

  50% {
    box-shadow: inset 0px -20px 20px 30px hsl(297, 42%, 10%);
  }

  to {
    box-shadow: inset 0px 20px 20px 30px #212121;
  }
}

@keyframes rotate {
  0% {
    transform: rotate(0deg) translate(-50%, 20%);
  }

  50% {
    transform: rotate(180deg) translate(40%, 10%);
  }

  to {
    transform: rotate(360deg) translate(-50%, 20%);
  }
}

@keyframes blinkShadowsFilter {
  0% {
    filter: drop-shadow(46px 36px 28px rgba(64, 144, 181, 0.3411764706))
      drop-shadow(-55px -40px 28px #9e30a9);
  }

  25% {
    filter: drop-shadow(46px -36px 24px rgba(64, 144, 181, 0.8980392157))
      drop-shadow(-55px 40px 24px #9e30a9);
  }

  50% {
    filter: drop-shadow(46px 36px 30px rgba(64, 144, 181, 0.8980392157))
      drop-shadow(-55px 40px 30px rgba(159, 48, 169, 0.2941176471));
  }

  75% {
    filter: drop-shadow(20px -18px 25px rgba(64, 144, 181, 0.8980392157))
      drop-shadow(-20px 20px 25px rgba(159, 48, 169, 0.2941176471));
  }

  to {
    filter: drop-shadow(46px 36px 28px rgba(64, 144, 181, 0.3411764706))
      drop-shadow(-55px -40px 28px #9e30a9);
  }
}

/* From Uiverse.io by david-mohseni */ 
.loader {
  position: relative;
  width: 54px;
  height: 54px;
  border-radius: 10px;
}

.loader div {
  width: 8%;
  height: 24%;
  background: rgb(128, 128, 128);
  position: absolute;
  left: 50%;
  top: 30%;
  opacity: 0;
  border-radius: 50px;
  box-shadow: 0 0 3px rgba(0,0,0,0.2);
  animation: fade458 1s linear infinite;
}

@keyframes fade458 {
  from {
    opacity: 1;
  }

  to {
    opacity: 0.25;
  }
}

.loader .bar1 {
  transform: rotate(0deg) translate(0, -130%);
  animation-delay: 0s;
}

.loader .bar2 {
  transform: rotate(30deg) translate(0, -130%);
  animation-delay: -1.1s;
}

.loader .bar3 {
  transform: rotate(60deg) translate(0, -130%);
  animation-delay: -1s;
}

.loader .bar4 {
  transform: rotate(90deg) translate(0, -130%);
  animation-delay: -0.9s;
}

.loader .bar5 {
  transform: rotate(120deg) translate(0, -130%);
  animation-delay: -0.8s;
}

.loader .bar6 {
  transform: rotate(150deg) translate(0, -130%);
  animation-delay: -0.7s;
}

.loader .bar7 {
  transform: rotate(180deg) translate(0, -130%);
  animation-delay: -0.6s;
}

.loader .bar8 {
  transform: rotate(210deg) translate(0, -130%);
  animation-delay: -0.5s;
}

.loader .bar9 {
  transform: rotate(240deg) translate(0, -130%);
  animation-delay: -0.4s;
}

.loader .bar10 {
  transform: rotate(270deg) translate(0, -130%);
  animation-delay: -0.3s;
}

.loader .bar11 {
  transform: rotate(300deg) translate(0, -130%);
  animation-delay: -0.2s;
}

.loader .bar12 {
  transform: rotate(330deg) translate(0, -130%);
  animation-delay: -0.1s;
}

</style>