import './assets/main.css'

import {createApp} from 'vue'
import {createPinia} from 'pinia'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import App from './App.vue'
import router from './router'
import '@icon-park/vue-next/styles/index.css'
import axios from 'axios'

axios.defaults.withCredentials = true

if (import.meta.env.MODE === 'production') {
    axios.defaults.baseURL = "http://dcqljw.com/api"
} else {
    axios.defaults.baseURL = "http://localhost:8000/api"
}


const app = createApp(App)
app.use(createPinia())
app.use(router)
app.use(ElementPlus)

app.mount('#app')
