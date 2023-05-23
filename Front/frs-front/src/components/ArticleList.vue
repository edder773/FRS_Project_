<template>
  <div class="article-list">
    <b-card title="Article List" class="text-primary">
      <template v-if="articles && articles.length > 0">
        <ArticleListItem
          v-for="article in articles"
          :key="article.id"
          :article="article"
        />
      </template>
      <p v-else class="text-danger">게시글이 없습니다.</p>
    </b-card>
  </div>
</template>

<script>
import ArticleListItem from '@/components/ArticleListItem'
import { BCard } from 'bootstrap-vue'

export default {
  name: 'ArticleList',
  components: {
    ArticleListItem,
    BCard
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
