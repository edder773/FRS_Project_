import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'bootstrap'
import { BootstrapVue } from 'bootstrap-vue'
import '@/assets/font.css';

// const instance = axios.create({
//   baseURL: '/api', // 프록시 경로 설정
// })

// Vue.config.productionTip = false
// Vue.prototype.$axios = instance
Vue.use(BootstrapVue)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
