import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import { useUiStore } from './stores/ui'
import './styles/global.css'
import './styles/experience.css'

const pinia = createPinia()
const app = createApp(App)
app.use(pinia).use(router)
useUiStore(pinia)
app.mount('#app')
