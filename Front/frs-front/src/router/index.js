import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ExchangeRate from '../views/ExchangeRate.vue'
import KakaoMap from '../views/KakaoMap.vue'
import ArticleView from '../views/Boards/ArticleView.vue'
import CreateView from '../views/Boards/CreateView.vue'
import DetailView from '../views/Boards/DetailView.vue'
import ProfileView from '../views/Account/ProfileView.vue'
// import DepositList from '@/views/Products/DepositList.vue'
import DepositNew from '@/views/Products/DepositNew.vue'
import SavingList from '@/views/Products/SavingList.vue'
import RecommendSelect from '@/views/Products/RecommendSelect.vue'
import OnetoOne from '@/views/OnetoOne.vue'
import QuestionBoard from '@/views/QuestionBoard.vue'
import RecommendSimilar from '@/views/Products/RecommendSimilar.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/exchange',
    name: 'exchange',
    component: ExchangeRate
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
    path: '/profile/:userId',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/deposit',
    name: 'deposit',
    component: DepositNew
  },
  {
    path: '/saving',
    name: 'saving',
    component: SavingList
  },
  {
    path: '/recommend',
    name: 'recommend',
    component: RecommendSelect
  },
  {
    path: '/question',
    name: 'question',
    component: QuestionBoard
  },
  {
    path: '/onetoone',
    name: 'onetoone',
    component: OnetoOne
  },
  {
    path: '/similar',
    name: 'similar',
    component: RecommendSimilar
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
