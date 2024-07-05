import './assets/main.css'

import {createApp} from 'vue'
import {createPinia} from 'pinia'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import App from './App.vue'
import router from './router'
import '@icon-park/vue-next/styles/index.css'
import 'element-plus/theme-chalk/dark/css-vars.css'
import hljs from "highlight.js"
import "highlight.js/styles/atom-one-dark.css"


const app = createApp(App)
app.use(createPinia())
app.use(router)
app.use(ElementPlus)

app.directive('highlight', (el) => {
    let blocks = el.querySelectorAll("pre code");
    blocks.forEach((block: any) => {
        hljs.highlightBlock(block)
    })
})

app.mount('#app')
