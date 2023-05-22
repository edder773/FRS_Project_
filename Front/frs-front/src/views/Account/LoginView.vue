<template>
    <div id="login-page">
      <h1>로그인</h1>
      <form @submit.prevent="login">
        <label for="username">ID : </label>
        <input type="text" id="username" v-model="username"><br>
  
        <label for="password"> password : </label>
        <input type="password" id="password" v-model="password"><br>
  
        <input type="submit" value="login">
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: 'LoginView',
    data() {
      return {
        username: null,
        password: null,
      }
    },
    methods: {
      login() {
        const username = this.username
        const password = this.password
  
        const payload = {
          username, password
        }
  
        this.$store.dispatch('login', payload)
  
      }
    }
  }
  </script>
  <style>

</style>