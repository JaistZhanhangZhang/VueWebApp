import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
//导入pinia插件
import { createPinia } from 'pinia'
//实例化pinia插件
const store = createPinia()
//注册路由
import router from './router'
//引入路由
createApp(App).use(router).use(store).mount('#app')
