import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ExchangeRate from '../views/ExchangeRate.vue'
import SignUpView from '../views/Account/SignUpView.vue'
import LoginView from '../views/Account/LoginView.vue'
import KakaoMap from '../views/KakaoMap.vue'
import ArticleView from '../views/Boards/ArticleView.vue'
import CreateView from '../views/Boards/CreateView.vue'
import DetailView from '../views/Boards/DetailView.vue'
import ProductView from '../views/ProductView.vue'
import ProfileView from '../views/Account/ProfileView.vue'
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
