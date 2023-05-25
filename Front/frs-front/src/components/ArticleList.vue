<template>
  <div class="article-list">
      <template v-if="articles && articles.length > 0">
        <table>
          <thead>
            <tr>
              <th>번호</th>
              <th>제목</th>
              <th>아이디</th>
              <th>작성시간</th>
            </tr>
          </thead>
          <tbody>
            <ArticleListItem  v-for="article in articles" :key="article.id" :article="article" @click="goToDetail(article.id)"/>
          </tbody>
        </table>
      </template>
      <p v-else class="text-danger">게시글이 없습니다.</p>
  </div>
</template>

<script>
import ArticleListItem from '@/components/ArticleListItem'
// import { BCard } from 'bootstrap-vue'

export default {
  name: 'ArticleList',
  components: {
    ArticleListItem,
    // BCard,
  },
  computed: {
    articles() {
      return this.$store.state.articles
    }
  },
  methods: {
    goToDetail(articleId) {
      console.log(articleId)
      this.$router.push({ name: 'detail', params: { id: articleId } });
    }
  }
}
</script>

<style>
.article-list {
  text-align: start;
}

.article-card {
  padding: 20px;
  border: none;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
}

.text-danger {
  color: #dc3545;
  font-weight: bold;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  padding: 10px;
  text-align: left;
  border-bottom: 1px solid #ccc;
}
</style>
