<template>
  <div class="bg-black w-screen h-screen p-0 m-0">
    <div class="w-full h-full px-10 py-6">
      <!-- Header -->
      <div class="mb-4 flex items-center justify-between">
        <div class="flex items-center gap-2">
          <div class="flex h-10 w-10 items-center justify-center rounded-lg bg-gradient-to-br from-[#4090b5] to-pink-500">
            <svg class="h-5 w-5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" />
            </svg>
          </div>
          <h3 class="text-base font-semibold text-white">App Review Analytics</h3>
        </div>
        <span class="flex items-center gap-1 rounded-full bg-emerald-500/10 px-2 py-1 text-xs font-medium text-emerald-500">
          <span class="h-1.5 w-1.5 rounded-full bg-emerald-500"></span>
          Live
        </span>
      </div>

      <!-- Metrics -->
      <div class="mb-4 grid grid-cols-2 gap-4">
        <div class="rounded-xl bg-slate-900/50 p-4">
          <p class="text-xs font-medium text-slate-400">Total Views</p>
          <p class="text-xl font-semibold text-white">24.5K</p>
          <span class="text-xs font-medium text-emerald-500">+12.3%</span>
        </div>
        <div class="rounded-xl bg-slate-900/50 p-4">
          <p class="text-xs font-medium text-slate-400">Conversions</p>
          <p class="text-xl font-semibold text-white">1.2K</p>
          <span class="text-xs font-medium text-emerald-500">+8.1%</span>
        </div>
      </div>

      <!-- Chart -->
      <div class="mb-4 h-28 w-full overflow-hidden rounded-xl bg-slate-900/50 p-3">
        <div class="flex h-full w-full items-end justify-between gap-1">
          <div class="h-[40%] w-3 rounded-sm bg-[#4090b5]/30"><div class="h-[60%] w-full rounded-sm bg-[#4090b5]"></div></div>
          <div class="h-[60%] w-3 rounded-sm bg-[#4090b5]/30"><div class="h-[40%] w-full rounded-sm bg-[#4090b5]"></div></div>
          <div class="h-[75%] w-3 rounded-sm bg-[#4090b5]/30"><div class="h-[80%] w-full rounded-sm bg-[#4090b5]"></div></div>
          <div class="h-[45%] w-3 rounded-sm bg-[#4090b5]/30"><div class="h-[50%] w-full rounded-sm bg-[#4090b5]"></div></div>
          <div class="h-[85%] w-3 rounded-sm bg-[#4090b5]/30"><div class="h-[90%] w-full rounded-sm bg-[#4090b5]"></div></div>
          <div class="h-[65%] w-3 rounded-sm bg-[#4090b5]/30"><div class="h-[70%] w-full rounded-sm bg-[#4090b5]"></div></div>
          <div class="h-[95%] w-3 rounded-sm bg-[#4090b5]/30"><div class="h-[85%] w-full rounded-sm bg-[#4090b5]"></div></div>
        </div>
      </div>

      <!-- Footer -->
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-2">
          <span class="text-xs font-medium text-slate-400">Last 7 days</span>
          <svg class="h-4 w-4 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
          </svg>
        </div>
        <button
          class="flex items-center gap-1 rounded-lg bg-gradient-to-r from-[#4090b5] to-pink-500 px-3 py-1 text-xs font-medium text-white hover:from-[#b3409e] hover:to-pink-600">
          View Details
          <svg class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>
