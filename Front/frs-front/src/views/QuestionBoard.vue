<template>
  
  <div>
    <router-link to="/article">자유게시판</router-link> |
      <router-link to="/question">자주 묻는 질문</router-link> |
      <router-link to="/onetoone">1:1 문의</router-link> |
      <router-view/>
  </div>
  
</template>

<script>
export default {
    name: 'QuestionBoard',

}
</script>

<style>

</style>