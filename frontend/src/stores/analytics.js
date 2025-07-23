import { defineStore } from 'pinia'

export const useAnalyticsStore = defineStore('analytics', {
  state: () => ({
    theme_values: [],
    theme_labels: [],
    rating_values: [],
    rating_labels: [],
    sentiment_data: {},
    error: null,
    drivers: [],
    painpoints: [],
    app_id : ''
  }),
  actions: {
    async analyser(appid) {
      this.error = null
      try {
        const response = await fetch('http://localhost:8000/api/analysis', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ appid })
        })
        const data = await response.json()
        if (response.ok) {
          this.theme_values = data.theme_values
          this.theme_labels = data.theme_labels
          this.app_id = appid
          this.rating_values = data.rating_values
          this.rating_labels = data.rating_labels
          this.sentiment_data = data.sentiment_trend || null
          this.painpoints = data.painpoints
          this.drivers = data.drivers
          return true
        } else {
          this.error = data.error || 'App review analysis failed'
          return false
        }
      } catch (err) {
        this.error = 'An error occurred: ' + err.message
        return false
      }
    }
  }
})
