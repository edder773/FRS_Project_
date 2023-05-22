<template>
  <div id="app">
    <div id="home"><router-link to="/"></router-link></div>
    <div class="header-dev">
      <div id="header-dev-top">
        <div class="main"><a href="/">FRS</a></div >
        <div class="gnb">
          <li class="left deposit"><a href="/deposit">예금비교</a></li>
          <li class="left exchange"><a href="/exchange">환율계산</a></li>
          <li class="left map"><a href="/map">은행찾기</a></li>
          <li class="left article"><a href="/article">게시판</a></li>
        </div>
        <div class="gnb-right">
          <li class="right profile"><a :href="`/profile/${userId}`">프로필</a></li>
          <div class="right logout" @click="loggedout()">로그아웃</div>
          <li class="right login"><a href="/login">로그인</a></li>
          <li class="right signup"><a href="/signup">회원가입</a></li>
        </div>       
      </div>
    </div>
    <router-view/>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  methods:{
    ...mapActions(['logout']),
    loggedout(){
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
/* nav {
  padding: 30px;
}
nav a {
  font-weight: bold;
  color: #11038d;
}
nav a.router-link-exact-active {
  color: #61a9c5;
} */
.header-dev {
  list-style: none;
  position: fixed;
  top: 0; 
  width: 100%; 
  background-color: #fff; 
  z-index: 1; 
}
.main{
  font-weight: bold;
  font-size: 60px;
  position: relative;
  float: left;
}
#header-dev-top .gnb{
  position: relative;
  float: left;
}
.left{
  padding: 20px;
  position: relative;
  float: left;
}
.header-dev{
  list-style: none;
}

.right{
  padding: 10px;
  padding-top: 20px;
  position: relative;
  float: right;
}


</style>
