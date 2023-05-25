<template>
  <div id="onetoone-page" class="container">
    <div class="menu-links">
      <router-link to="/article" class="menu-link">자유게시판</router-link> 
      <router-link to="/question" class="menu-link">자주 묻는 질문</router-link> 
      <router-link to="/onetoone" class="menu-link">1:1 문의</router-link> 
      <div class="onetoone-button">문의하기</div>
    </div><hr>
  </div>
</template>

<script>
export default {
    name:'OnetoOne',
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
.onetoone-container{
  background-color: black;
  height: 5000px;
}
</style>