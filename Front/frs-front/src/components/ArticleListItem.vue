<template>
  <tr @click="goToDetail(article.id)" style="cursor: pointer;">
    <td>{{ article.id }}</td>
    <td>{{ article.title }}</td>
    <td>{{ article.user }}</td>
    <td>{{ new Date(article?.created_at).toLocaleString('ko-KR', { year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit' }) }}</td>
  </tr>
</template>

<script>
export default {
  name: 'ArticleListItem',
  props: {
    article: {
      type: Object,
      required: true
    }
  },
  methods: {
    goToDetail(articleId) {
      this.$emit('click', articleId)
    }
  }
}
</script>

<style scoped>
td {
  padding: 10px;
  border-bottom: 1px solid #ccc;
}
</style>
