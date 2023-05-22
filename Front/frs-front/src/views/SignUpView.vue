<template>
    <div id="signup-page">
      <h1>회원가입</h1>
      <form @submit.prevent="signUp">
        
        <label for="username">*ID : </label>
        <input type="text" id="username" :state="username" v-model="username"><br>
        
        <label for="email"> *이메일 : </label>
        <input type="email" id="email" v-model="email"><br>

        <label for="password1"> *PW : </label>
        <input type="password" id="password1" v-model="password1"><br>
        
        <label for="password2"> *PW Confirmation : </label>
        <input type="password" id="password2" v-model="password2"><br>
        
        <label for="nickname"> *이름 : </label>
        <input type="text" id="nickname" v-model="nickname"><br>
        
        <label for="age"> 나이 : </label>
        <input type="text" id="age" v-model="age"><br>

        <label for="annual_income"> 연봉 : </label>
        <input type="text" id="annual_income" v-model="annual_income"><br>

        <label for="occupation"> 직업 : </label>
        <input type="text" id="occupation" v-model="occupation"><br>

        <label for="assets"> 자산 : </label>
        <input type="text" id="assets" v-model="assets"><br>

        <label for="bank"> 선호은행 : </label>
        <input type="text" id="bank" v-model="bank"><br>

        <label for="location"> 주소 : </label>
        <input type="text" id="location" v-model="location"><br>
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
        console.log(payload)
      }
    }
  }
  </script>
<style>
#signup-page{
  margin-top: 80px;
}
</style>