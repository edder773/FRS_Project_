<template>
  <div class="article-list">
    <h3 class="text-primary">Article List</h3>
    <template v-if="articles && articles.length > 0">
      <ArticleListItem
        v-for="article in articles"
        :key="article.id"
        :article="article"
      />
    </template>
    <p v-else class="text-danger">게시글이 없습니다.</p>
  </div>
</template>
<script>
import ArticleListItem from '@/components/ArticleListItem'

export default {
  name: 'ArticleList',
  components: {
    ArticleListItem,
  },
  computed: {
    articles() {
      return this.$store.state.articles
    }
  }
}
</script>
<style>
.article-list {
  text-align: start;
}

</style>