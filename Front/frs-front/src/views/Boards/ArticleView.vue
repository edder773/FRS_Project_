<template>
  <div id="article-page" class="container">
    <router-link to="/article" class="menu-link">자유게시판 | </router-link> 
    <router-link to="/question" class="menu-link">자주 묻는 질문 | </router-link> 
    <router-link to="/onetoone" class="menu-link">1:1 문의</router-link> 
    <hr>
    <h2>자유게시판</h2>
    <b-button class="create-button">
      <router-link :to="{ name: 'create' }" class="create-button" >글 작성하기</router-link>
    </b-button><br><br>
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
  .menu-link {
    color: black;
    font-size: 25px;
    font-family: 'Poppins', sans-serif;
    text-decoration: none;
  }
  
  .create-button {
    background-color: rgb(197, 225, 243);
    color: black;
    text-decoration: none;
    font-size: 15px;
  }

  </style>