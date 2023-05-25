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
        this.$router.push({ name: 'home' })
      }
    }
  }
}
</script>

<style scoped>
.menu-links {
  display: flex;
  justify-content: center;
}

.menu-link {
  color: #333;
  font-size: 18px;
  text-decoration: none;
  padding: 10px;
  margin-right: 10px;
  transition: color 0.3s;
}

.menu-link:hover {
  border-bottom-color: #555;
}
.menu-link:hover,
.menu-link.active {
  color: #007bff;
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
