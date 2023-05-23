<template>
    <div id="article-page">
      <router-link to="/article">자유게시판</router-link> |
      <router-link to="/question">자주 묻는 질문</router-link> |
      <router-link to="/onetoone">1:1 문의</router-link> |
      <hr>
      <h1>자유게시판</h1>
      <b-button variant="primary"><router-link :to="{ name: 'create' }">글 작성하기</router-link></b-button>
      <ArticleList />
      <hr>
      <router-view/>
    </div>
  </template>
  
  <script>
  import ArticleList from '@/components/ArticleList.vue'
  
  export default {
    name: 'ArticleView',
    components: {
      ArticleList,
    },
    computed:{
      isLogin() {
        return this.$store.getters.isLogin // 로그인 여부
      }
    },
    created() {
      this.getArticles()
    },
    methods: {
      getArticles() {
        if (this.isLogin) {
          this.$store.dispatch('getArticles')
        } else {
          alert('로그인이 필요한 페이지입니다...')
          this.$router.push({ name: 'LoginView' })
        }
      }
    }
  }
  </script>
  
  <style>

  </style>