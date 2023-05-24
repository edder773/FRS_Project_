<template>
  <div id="app">
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
          <b-nav-item v-if="!userId" @click="showSignUpModal" class="nav-link-custom">회원가입</b-nav-item>
          <b-modal size="lg" v-model="showModal" title="회원가입" @ok="signUp">
            <div style="width: 100%; height: 500px; margin: 0 auto; margin-top: 3%; overflow-y: auto;">
              <b-card bg-variant="light">
                <form @submit.prevent="signUp">
                  <b-form-group label-cols-lg="3" label-size="lg" label-class="font-weight-bold pt-0" class="mb-0">
                    <b-form-group label="*아이디:" label-for="username" label-cols-sm="3" label-align-sm="right">
                      <b-form-input id="username" v-model="username" :state="usernameValid"></b-form-input>
                      <b-form-invalid-feedback id="input-live-feedback">4글자 이상 입력하세요</b-form-invalid-feedback>
                    </b-form-group>
    
                    <b-form-group label="*이메일:" label-for="email" label-cols-sm="3" label-align-sm="right">
                      <b-form-input type="email" id="email" v-model="email" :state="emailValid"></b-form-input>
                      <b-form-invalid-feedback id="input-live-feedback">이메일 형태로 입력해주세요</b-form-invalid-feedback>
                    </b-form-group>
      
                    <b-form-group label="*비밀번호:" label-for="password" label-cols-sm="3" label-align-sm="right">
                      <b-form-input type="password" id="password1" v-model="password1" :state="passwordValid"></b-form-input>
                      <b-form-invalid-feedback id="input-live-feedback">8글자 이상 입력하세요</b-form-invalid-feedback>
                    </b-form-group>

                    <b-form-group label="*비밀번호번호:" label-for="password" label-cols-sm="3" label-align-sm="right">
                      <b-form-input type="password" id="password2" v-model="password2" :state="password2Valid"></b-form-input>
                      <b-form-invalid-feedback id="input-live-feedback">비밀번호가 일치하지 않습니다</b-form-invalid-feedback>
                    </b-form-group>

                    <b-form-group label="*이름:" label-for="nickname" label-cols-sm="3" label-align-sm="right">
                      <b-form-input id="nickname" v-model="nickname" :state="nicknameValid"></b-form-input>
                    </b-form-group>
                    <br>
                    선택 항목
                    <hr>

                    <b-form-group label="나이:" label-for="age" label-cols-sm="3" label-align-sm="right">
                      <b-form-input type="number" id="age" v-model="age"></b-form-input>
                    </b-form-group>

                    <b-form-group label="직업:" label-for="occupation" label-cols-sm="3" label-align-sm="right">
                      <b-form-input id="occupation" v-model="occupation"></b-form-input>
                    </b-form-group>

                    <b-form-group label="연봉:" label-for="annual_income" label-cols-sm="3" label-align-sm="right">
                      <b-form-input type="number" step="1000000" id="annual_income" v-model="annual_income"></b-form-input>
                    </b-form-group>

                    <b-form-group label="자산:" label-for="assets" label-cols-sm="3" label-align-sm="right">
                      <b-form-input type="number" step="1000000" id="assets" v-model="assets"></b-form-input>
                    </b-form-group>

                    <b-form-group label="선호은행:" label-for="bank" label-cols-sm="3" label-align-sm="right">
                      <b-form-select id="bank" v-model="bank" style="width: 100%; height: 37px;" >
                        <option v-for="option in bankOptions" :value="option" :key="option.id">{{ option }}</option>
                      </b-form-select>
                    </b-form-group>
                    <b-form-group label="주소:" label-for="location" label-cols-sm="3" label-align-sm="right">
                      <b-form-select id="location" v-model="location" style="width: 100%; height: 37px;" >
                        <option v-for="option in locationOptions" :value="option" :key="option.id">{{ option }}</option>
                      </b-form-select>
                    </b-form-group>   
                  </b-form-group>
                </form>
              </b-card>
            </div>
          </b-modal>
        <b-nav-item v-if="userId" @click="loggedout()" class="nav-link-custom">로그아웃</b-nav-item>
        <b-nav-item v-if="!userId" @click="showloginModal" class="nav-link-custom">로그인</b-nav-item>
          <b-modal size="lg" v-model="loginModal" title="로그인" @ok="login">
            <b-card bg-variant="light">
              <form @submit.prevent="signUp">
                <b-form-group label-cols-lg="3" label-size="lg" label-class="font-weight-bold pt-0" class="mb-0">
                  <b-form-group label="*아이디:" label-for="username" label-cols-sm="3" label-align-sm="right">
                    <b-form-input id="username" v-model="username"></b-form-input>
                  </b-form-group>
    
                  <b-form-group label="비밀번호:" label-for="password" label-cols-sm="3" label-align-sm="right">
                    <b-form-input type="password" id="password" v-model="password"></b-form-input>
                  </b-form-group>
                </b-form-group>
              </form>
            </b-card>
        </b-modal>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
  <router-view/>
</div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  data() {
    return {
      showModal: false,
      loginModal: false,
      username: null,
        email: null,
        password: null,
        password1: null,
        password2: null,
        nickname: null,
        annual_income: null,
        occupation: null,
        assets: null,
        bank: null,
        location: null,
        age: null,
        bankOptions: ["KEB하나은행", "SC은행", "경남은행", "광주은행", "국민은행", "기업은행", "농협은행", "대구은행", "부산은행",
       "새마을금고", "산업은행", "수협은행", "신한은행", "신협중앙회", "외환은행","우체국", "우리은행", "저축은행",
        "제주은행", "한국산업은행", "한국수출입은행", "한국은행", "현대은행"],
        locationOptions: [
      '서울특별시 ','부산광역시 ','대구광역시 ','인천광역시 ','광주광역시 ','대전광역시 ',
      '울산광역시 ','세종특별자치시 ','경기도 ','강원도 ','충청북도 ','충청남도 ',
      '전라북도 ','전라남도 ','경상북도 ','경상남도 ','제주특별자치도 '
      ],
        isSimilarUsername: false,
    }
  },
  methods: {
    ...mapActions(['logout']),
    loggedout() {
      this.logout()
    },
    showSignUpModal() {
      this.showModal = true
    },
    showloginModal(){
      this.loginModal = true
    },
    signUp() {
        const payload = {
          username: this.username,
          email: this.email,
          password1: this.password1,
          password2: this.password2,
          nickname: this.nickname,
          annual_income: this.annual_income !== null ? this.annual_income : undefined,
          occupation: this.occupation !== null ? this.occupation : undefined,
          assets: this.assets !== null ? this.assets : undefined,
          bank: this.bank !== null ? this.bank : undefined,
          location: this.location !== null ? this.location : undefined,
          age: this.age !== null ? this.age : undefined,
        }
        this.$store.dispatch('signUp', payload)
      },
      login() {
        const username = this.username
        const password = this.password
  
        const payload = {
          username, password
        }
  
        this.$store.dispatch('login', payload)
  
      }
  },
  computed: {
    ...mapState(['user']),
    userId() {
      return this.user && this.user.username ? this.user.username : null
    },
    usernameValid(){
        return this.username && this.username.length >= 4
      },
      passwordValid(){
        return this.password1 && this.password1.length >= 8
      },
      password2Valid(){
        return this.password2 && this.password1===this.password2
      },
      nicknameValid(){
        return this.nickname && this.nickname.length >= 2
      },
      emailValid() {
      const emailRegex = /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/;
      return this.email && emailRegex.test(this.email)
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
