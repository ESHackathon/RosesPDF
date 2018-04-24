// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import axios from 'axios'
import Vue from 'vue'
import VueAxios from 'vue-axios'
import Vuetify from 'vuetify'

import 'vuetify/dist/vuetify.css'
import '@/assets/scss/roses.scss'

import App from './App'
import router from './router'

Vue.use(VueAxios, axios)
Vue.axios.defaults.baseURL = process.env.API_URL || 'http://localhost:5000'
Vue.use(Vuetify, { theme: {
  primary: '#1976d2',
  secondary: '#63a4ff',
  accent: '#004ba0',
  error: '#FF5252',
  info: '#2196F3',
  success: '#4CAF50',
  warning: '#FFC107'
}})

Vue.config.productionTip = process.env.NODE_ENV !== 'production'
Vue.config.devtools = process.env.NODE_ENV !== 'production'
Vue.config.performance = process.env.NODE_ENV !== 'production'

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
