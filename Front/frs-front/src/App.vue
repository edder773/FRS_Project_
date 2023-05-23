<template>
  <div id="app">
    <!-- <b-container> -->
    <b-navbar toggleable="lg" type="light" class="header-dev container">
      <b-navbar-brand href="/" class="navbar-brand-custom">FRS</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item href="/deposit" class="nav-link-custom">예금비교</b-nav-item>
          <b-nav-item href="/exchange" class="nav-link-custom">환율계산</b-nav-item>
          <b-nav-item href="/map" class="nav-link-custom">은행찾기</b-nav-item>
          <b-nav-item href="/article" class="nav-link-custom">게시판</b-nav-item>
        </b-navbar-nav>
        <b-navbar-nav class="ms-auto">
          <b-nav-item v-if="userId"><router-link :to="`/profile/${userId}`" class="nav-link-custom">프로필</router-link></b-nav-item>
          <b-nav-item v-if="!userId"><router-link to="/signup" class="nav-link-custom">회원가입</router-link></b-nav-item> 
        <!-- </b-navbar-nav>
        <b-navbar-nav class="ms-auto"> -->
          <b-nav-item v-if="userId" @click="loggedout()" class="nav-link-custom">로그아웃</b-nav-item>
          <b-nav-item v-if="!userId"><router-link to="/login" class="nav-link-custom">로그인</router-link></b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <router-view/>
  <!-- </b-container> -->
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
    font-family: 'TTWanjudaedunsancheB';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2304-2@1.0/TTWanjudaedunsancheB.woff2') format('woff2');
    font-weight: 700;
    font-style: normal;
}

.header-dev {
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 1;
}

.b-navbar-nav .b-nav-item {
  padding: 20px;
}

.nav-link-custom {
  font-weight: bold;
  color: #505050;
  border-bottom: none;
}

.router-link-exact-active {
  color: #f9abe6;
}

.logout-button {
  color: #fff;
}
.logo {
    font-family: 'TTWanjudaedunsancheB';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2304-2@1.0/TTWanjudaedunsancheB.woff2') format('woff2');
    font-weight: 700;
    font-style: normal;
}
</style>
