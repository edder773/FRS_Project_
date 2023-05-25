<template>
  <div id="article-page" class="container">
    <div class="menu-links  text-center">
      <router-link to="/article" class="menu-link">자유게시판</router-link> 
      <router-link to="/question" class="menu-link">자주 묻는 질문</router-link> 
      <router-link to="/onetoone" class="menu-link">1:1 문의</router-link> 
    </div>
    <hr>
    <b-row>
      <b-col class="d-flex align-items-center mt-3">
    <h2 class="section-title">자유게시판</h2>
    <b-button class="create-button ms-auto">
      <router-link :to="{ name: 'create' }" class="create-link" >글 작성하기</router-link>
    </b-button>
  </b-col>
  </b-row>
    <hr>
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
  color: #9bb5d1;
}
.create-button {
  background-color: #383838;
  color: #fff;
  cursor: pointer;
}

.create-button:hover {
  background-color: #bdbdbd;
  color: black;
}

.create-link {
  color: white;
  text-decoration: none;
}
</style>
