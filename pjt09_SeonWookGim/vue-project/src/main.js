import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-icons/font/bootstrap-icons.css'
import 'bootstrap/dist/js/bootstrap'

import axios from 'axios'
const app = createApp(App)

app.config.globalProperties.$axios = axios

app.use(router)

app.mount('#app')
