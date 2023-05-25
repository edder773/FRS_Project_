<template>
  <tr @click="goToDetail(article.id)" style="cursor: pointer;">
    <td style="text-align: center;">{{ article.id }}</td>
    <td class="create-button" style="width: 60%;text-align: center;" @click="goToDetail">{{ article.title }}</td>
    <td style="text-align: right;">{{ article.user }}</td>
    <td style="text-align: right;">{{ new Date(article?.created_at).toLocaleString('ko-KR', { year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit' }) }}</td>
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
  font-family: 'S-CoreDream-3Light';
  padding: 10px;
  border-bottom: 1px solid #ccc;
}
.create-button:hover {
  /* background-color: #bdbdbd; */
  color: #9a9a9a;
}
</style>
