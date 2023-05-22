import Vue from 'vue'
// import axios from 'axios'
import App from './App.vue'
import router from './router'
import store from './store'
// import BootstrapVue from 'bootstrap-vue'
// import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue/dist/bootstrap-vue.css'

// const instance = axios.create({
//   baseURL: '/api', // 프록시 경로 설정
// })

// Vue.config.productionTip = false
// Vue.prototype.$axios = instance
// Vue.use(BootstrapVue)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
