<template>
  <tr>
    <td>{{ article.id }}</td>
    <td>{{ article.user }}</td>
    <td>{{ article.title }}</td>
    <td>{{ article.created_at }}</td>
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
  }
}
</script>

<style scoped>
td {
  padding: 10px;
  border-bottom: 1px solid #ccc;
}
</style>
