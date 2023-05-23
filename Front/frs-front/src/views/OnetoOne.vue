<template>
  <div>
    <router-link to="/article" class="menu-link">자유게시판 | </router-link> 
    <router-link to="/question" class="menu-link">자주 묻는 질문 | </router-link> 
    <router-link to="/onetoone" class="menu-link">1:1 문의</router-link> 
    <router-view/>
  </div>
</template>

<script>
export default {
    name:'OnetoOne',
}
</script>

<style>

</style>