import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ExchangeRate from '../views/ExchangeRate.vue'
import SignUpView from '../views/SignUpView.vue'
import LoginView from '../views/LoginView.vue'
import KakaoMap from '../views/KakaoMap.vue'
import ArticleView from '../views/ArticleView.vue'
import CreateView from '../views/CreateView.vue'
import DetailView from '../views/DetailView.vue'
import ProductView from '../views/ProductView.vue'
import ProfileView from '../views/ProfileView.vue'
import DepositList from '@/views/Products/DepositList.vue'
import SavingList from '@/views/Products/SavingList.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/home',
    name: 'home',
    component: HomeView
  },
  {
    path: '/exchange',
    name: 'exchange',
    component: ExchangeRate
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/map',
    name: 'map',
    component: KakaoMap
  },
  {
    path: '/article',
    name: 'article',
    component: ArticleView
  },
  {
    path: '/create',
    name: 'create',
    component: CreateView
  },
  {
    path: '/detail',
    name: 'detail',
    component: DetailView
  },
  {
    path: '/product',
    name: 'product',
    component: ProductView
  },
  {
    path: '/profile/:userId',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/deposit',
    name: 'deposit',
    component: DepositList
  },
  {
    path: '/saving',
    name: 'saving',
    component: SavingList
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
