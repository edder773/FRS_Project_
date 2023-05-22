<template>
  <div id="signup-page">
    <h1>회원가입</h1>
      <form @submit.prevent="signUp">
        <div class="row">
          <div class="col-sm-2">
            <label for="username" class="mb-0">*ID:</label>
          </div>
          <div class="col-sm-3 d-flex align-items-center">
            <b-form-input id="username" v-model="username" :state="usernameValid" size="sm"></b-form-input>
            <b-form-invalid-feedback id="input-live-feedback">
              4글자 이상 입력하세요
            </b-form-invalid-feedback>
          </div>
          <div class="col-sm-7"></div>
          <div class="col-sm-2">
            <label for="email" class="mb-0"> *이메일 : </label>
          </div>
          <div class="col-sm-3 d-flex align-items-center">
            <b-form-input type="email" id="email" v-model="email" :state="emailValid" size="sm"></b-form-input>
            <b-form-invalid-feedback id="input-live-feedback">
              이메일 형태로 입력해주세요
            </b-form-invalid-feedback>
          </div>
          <div class="col-sm-7"></div>
          <div class="col-sm-2">
            <label for="password" class="mb-0">*PW:</label>
          </div>
          <div class="col-sm-3 d-flex align-items-center">
            <b-form-input type="password" id="password1" v-model="password1" :state="passwordValid" size="sm"></b-form-input>
            <b-form-invalid-feedback id="input-live-feedback">
              8글자 이상 입력하세요
            </b-form-invalid-feedback>
          </div>
          <div class="col-sm-7"></div>
        <div class="col-sm-2">
            <label for="password" class="mb-0">비밀번호 확인:</label>
          </div>
          <div class="col-sm-3 d-flex align-items-center">
            <b-form-input type="password" id="password2" v-model="password2" :state="password2Valid" size="sm"></b-form-input>
            <b-form-invalid-feedback id="input-live-feedback">
              비밀번호가 일치하지 않습니다
            </b-form-invalid-feedback>
          </div>
        <div class="col-sm-7"></div>
        <div class="col-sm-2">
            <label for="nickname" class="mb-0"> *이름 : </label>
          </div>
          <div class="col-sm-3 d-flex align-items-center">
            <b-form-input id="nickname" v-model="nickname" :state="nicknameValid" size="sm"></b-form-input>
          </div>
          <div class="col-sm-7"></div>
          <div class="col-sm-2">
              <label for="age" class="mb-0"> 나이 : </label>
            </div>
            <div class="col-sm-3 d-flex align-items-center">
              <b-form-input id="age" v-model="age" size="sm"></b-form-input>
            </div>
            <div class="col-sm-7"></div>
            <div class="col-sm-2">
              <label for="annual_income" class="mb-0"> 연봉 : </label>
            </div>
            <div class="col-sm-3 d-flex align-items-center">
              <b-form-input id="annual_income" v-model="annual_income" size="sm"></b-form-input>
            </div>
            <div class="col-sm-7"></div>
            <div class="col-sm-2">
              <label for="occupation" class="mb-0"> 나이 : </label>
            </div>
            <div class="col-sm-3 d-flex align-items-center">
              <b-form-input id="occupation" v-model="occupation" size="sm"></b-form-input>
            </div>
            <div class="col-sm-7"></div>
            <div class="col-sm-2">
              <label for="assets" class="mb-0"> 자산 : </label>
            </div>
            <div class="col-sm-3 d-flex align-items-center">
              <b-form-input id="assets" v-model="assets" size="sm"></b-form-input>
            </div>
            <div class="col-sm-7"></div>
            <div class="col-sm-2">
              <label for="bank" class="mb-0"> 선호은행 : </label>
            </div>
            <div class="col-sm-3 d-flex align-items-center">
              <b-form-input id="bank" v-model="bank" size="sm"></b-form-input>
            </div>
            <div class="col-sm-7"></div>
            <div class="col-sm-2">
              <label for="location" class="mb-0"> 주소 : </label>
            </div>
            <div class="col-sm-3 d-flex align-items-center">
              <b-form-input id="location" v-model="location" size="sm"></b-form-input>
            </div>
            <div class="col-sm-7"></div>
          </div>
        <input type="submit" value="SignUp">
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: 'SignUpView',
    data() {
      return {
        username: null,
        email: null,
        password1: null,
        password2: null,
        nickname: null,
        annual_income: null,
        occupation: null,
        assets: null,
        bank: null,
        location: null,
        age: null,
        
      }
    },
    computed:{
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
      return this.email && emailRegex.test(this.email);
    }
    },
    methods: {
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
      }
    }
  }
  </script>
<style>

</style>