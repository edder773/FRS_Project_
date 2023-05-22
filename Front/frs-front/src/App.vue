<template>
  <div id="app">
    <b-navbar toggleable="lg" type="light" variant="light" class="header-dev">
      <b-navbar-brand href="/">FRS</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item><router-link to="/deposit">예금비교</router-link></b-nav-item>
          <b-nav-item><router-link to="/exchange">환율계산</router-link></b-nav-item>
          <b-nav-item><router-link to="/map">은행찾기</router-link></b-nav-item>
          <b-nav-item><router-link to="/article">게시판</router-link></b-nav-item>
        </b-navbar-nav>
        <b-navbar-nav class="ml-auto">
          <b-nav-item v-if="userId" @click="loggedout()">로그아웃</b-nav-item>
          <b-nav-item v-else><router-link to="/signup">회원가입</router-link>
          <router-link to="/login">로그인</router-link></b-nav-item>
          <b-nav-item v-if="userId"><router-link :to="`/profile/${userId}`">프로필</router-link></b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <router-view/>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  methods: {
    ...mapActions(['logout']),
    loggedout() {
      this.logout()
    }
  },
  computed: {
    ...mapState(['user']),
    userId() {
      return this.user && this.user.username ? this.user.username : null
    },
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #505050;
  position: relative;
}

.header-dev {
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 1;
}

.b-navbar {
  padding: 20px;
}

.b-navbar-brand {
  font-weight: bold;
  font-size: 36px;
}

.b-navbar-nav .b-nav-item {
  padding: 20px;
}

.b-nav-item a {
  font-weight: bold;
  color: #11038d;
}

.b-nav-item.router-link-exact-active a {
  color: #61a9c5;
}

.b-nav-item {
  padding: 10px;
  padding-top: 20px;
}

</style>
