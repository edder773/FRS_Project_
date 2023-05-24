import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)


export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    articles: [
    ],
    token: null,
    user: null,
    financialProducts: [],
    signedProducts: []
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    },
    getUser(state) {
      return state.user
    },
    getUserId(state) {
      return state.user.username ? state.user.username : null;
    },
    getToken(state){
      return state.token
    },
    getFinancialProducts(state) {
      return state.financialProducts;
    }
  },
  mutations: {
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
    // signup & login -> 완료하면 토큰 발급
    SAVE_TOKEN(state, token, context) {
      state.token = token
      router.push({name : 'ArticleView'})
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/`,
        headers: {
          Authorization: `Token ${token}`
        }
      })
        .then((res) => {
          const user = res.data
          console.log(res)
          context.commit('SAVE_USER', user)
          console.log('User:', user)
        })
        .catch((err) => console.log(err))
    },
    SAVE_USER(state, user){
      state.user = user
    },
    CLEAR_USER(state){
      state.user = null
    },
    CLEAR_TOKEN(state){
      state.token = null
    },
    UPDATE_USER(state, user){
      state.user = user
    },
  },
  actions: {
    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/`,
      })
        .then((res) => {
        // console.log(res, context)
          context.commit('GET_ARTICLES', res.data)
        })
        .catch((err) => {
        console.log(err)
      })
    },
    // 회원가입 부분
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2
      const nickname = payload.nickname
      const email = payload.email
      const annual_income = payload.annual_income
      const occupation = payload.occupation
      const assets = payload.assets
      const bank = payload.bank
      const address = payload.address
      const age = payload.age
      
      if (!username){
        alert('아이디를 입력해주세요')
        return
      }
      if (!password1 || !password2){
        alert('비밀번호를 입력해주세요')
        return
      }
      if (!email){
        alert('이메일을 입력해주세요')
        return
      }
      if (!nickname){
        alert('이름을 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2, email, nickname, annual_income, occupation, assets, bank, address, age
        }
      })
        .then((res) => {
          alert('회원가입 되었습니다. 로그인 해주세요.')
          context.commit('SAVE_TOKEN', res.data.key)
          location.reload()
        })
        .catch(() => {
        alert('아이디와 유사한 비밀번호는 사용할 수 없습니다.')
        return
      })
    },
    // 로그인 부분
    login(context, payload) {
      const username = payload.username
      const password = payload.password
  
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username,
          password
        }
      })
        .then((res) => {
          const token = res.data.key
          context.commit('SAVE_TOKEN', res.data.key)
          console.log('Token:', token)
  
          // 사용자 정보를 가져오는 axios 요청을 수정
          return axios({
            method: 'get',
            url: `${API_URL}/accounts/user/`,
            headers: {
              Authorization: `Token ${token}`
            }
          })
        })
        .then((res) => {
          const user = res.data
          context.commit('SAVE_USER', user)
          // location.reload()
        })
        .catch((err) => console.log(err))
    },
    // 로그아웃 부분
    logout(context){
      localStorage.removeItem('vuex')
      context.commit('CLEAR_USER')
      context.commit('CLEAR_TOKEN')

      location.reload()
    },
    addProduct(context, payload) {
      const user_id = payload.user_id
      const product_id = payload.product_id
      axios({
        method: 'post',
        url: `${API_URL}/deposits/add/`,
        data: {
          user_id, product_id
        },
      })
      .then((response) => {
        console.log(response)
        axios({
          method: 'get',
          url: `${API_URL}/accounts/user/`,
          headers: {
            Authorization: `Token ${context.state.token}`
          }
        })
        .then((res) => {
          const user = res.data
          context.commit('SAVE_USER', user)
        })
        .catch((err) => console.log(err))
      })
      .catch((error) => {
        console.log(error)
      })
    }
    ,
    //회원정보수정
    profileChange(context,payload){
      const username = payload.username
      const nickname = payload.nickname
      const email = payload.email
      const annual_income = payload.annual_income
      const occupation = payload.occupation
      const assets = payload.assets
      const bank = payload.bank
      const address = payload.address
      const age = payload.age
      const fin_prdt_nm = payload.fin_prdt_nm
      const token = context.state.token

      axios({
        method: 'put',
        url: `${API_URL}/accounts/user/change/`,
        data: {
          username, nickname, email, annual_income, occupation, assets, bank, address, age, fin_prdt_nm
        },
        headers: {
          Authorization: `Token ${token}`
        }
      })
        .then((response) => {
          const updatedUser = response.data
          context.commit('UPDATE_USER', updatedUser)

          axios({
            method: 'get',
            url: `${API_URL}/accounts/user/`,
            headers: {
              Authorization: `Token ${token}`
            }
          })
            .then((res) => {
              const user = res.data
              console.log(res)
              context.commit('SAVE_USER', user)
              console.log('User:', user)
            })
            .catch((err) => console.log(err))
        })
        .catch((err) => {
        console.log(err)
      })
    },
  },
  modules: {
  }
})
