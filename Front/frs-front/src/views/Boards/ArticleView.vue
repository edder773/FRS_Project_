<template>
  <div id="article-page" class="container">
    <div class="menu-links  text-center">
      <router-link to="/article" class="menu-link">자유게시판</router-link> 
      <router-link to="/question" class="menu-link">자주 묻는 질문</router-link> 
      <router-link to="/onetoone" class="menu-link">1:1 문의</router-link> 
    </div>
    <hr>
    <h2 class="section-title">자유게시판</h2>
    <b-button class="create-button">
      <router-link :to="{ name: 'create' }" class="create-link" >글 작성하기</router-link>
    </b-button>
    <br><hr>
    <ArticleList />
    <!-- <hr> -->
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
  computed: {
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
.menu-links {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
  /* align-items: center; 추가 */
}

.menu-link {
  color: black;
  font-size: 18px;
  font-family: 'Poppins', sans-serif;
  text-decoration: none;
  padding-bottom: 5px;
  border-bottom: 2px solid transparent;
  transition: border-bottom-color 0.3s ease-in-out;
}

.menu-link:hover {
  border-bottom-color: #555;
}

.create-button {
  background-color: #007bff;
  color: white;
  text-decoration: none;
  font-size: 15px;
  padding: 10px 20px;
  border-radius: 5px;
  transition: background-color 0.3s ease-in-out;
  margin-left: 80%; /* 추가 */
}

.create-button:hover {
  background-color: #0056b3;
}

.create-link {
  color: white;
  text-decoration: none;
}
</style>
