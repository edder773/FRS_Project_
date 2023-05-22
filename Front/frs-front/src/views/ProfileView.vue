<!-- ProfileView.vue -->

<template>
    <div id="profile-page">
      <h2>User Profile</h2>
      <div v-if="isLogin && user">
        <p>아이디: {{ user.username }}</p>
        <p>이메일: {{ user.email }}</p> 
        <p>이름: {{ user.nickname }}</p>
        <p>연봉: {{ user.annual_income }}</p>
        <p>자산: {{ user.assets }}</p>
        <p>은행: {{ user.bank }}</p>
        <p>주소: {{ user.location }}</p>

      </div>
      <div v-else>
        <p>Please log in to view your profile.</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "ProfileView",
    computed: {
      isLogin() {
        return this.$store.getters.isLogin;
      },
      user() {
        return this.$store.getters.getUser
      },
      
    }
  }
  </script>
<style>
#profile-page{
  margin-top: 80px;
}
</style>