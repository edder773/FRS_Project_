<template>
    <div>
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
    computed: {
    isUsernameValid() {
      // username이 2글자 이상인지 확인
      return this.username && this.username.length >= 2;
    },
    isPasswordValid() {
      // password가 8글자 이상인지 확인
      return this.password1 && this.password1.length >= 8;
    },
    isNicknameValid() {
      // nickname이 2글자 이상인지 확인
      return this.nickname && this.nickname.length >= 2;
    },
    isOccupationValid() {
      // occupation이 2글자 이상인지 확인
      return this.occupation && this.occupation.length >= 2;
    },
    isLocationValid() {
      // location이 2글자 이상인지 확인
      return this.location && this.location.length >= 2;
    },
    usernameRules() {
      return [
        (value) => !!value || 'ID를 입력하세요',
        (value) =>
          (value && value.length >= 2) || 'ID는 2글자 이상이어야 합니다',
      ];
    },
    passwordRules() {
      return [
        (value) => !!value || '비밀번호를 입력하세요',
        (value) =>
          (value && value.length >= 8) || '비밀번호는 8글자 이상이어야 합니다',
      ];
    },
    nicknameRules() {
      return [
        (value) => !!value || '이름을 입력하세요',
        (value) =>
          (value && value.length >= 2) || '이름은 2글자 이상이어야 합니다',
      ];
    },
    occupationRules() {
      return [
        (value) => !!value || '직업을 입력하세요',
        (value) =>
          (value && value.length >= 2) || '직업은 2글자 이상이어야 합니다',
      ];
    },
    locationRules() {
      return [
        (value) => !!value || '주소를 입력하세요',
        (value) =>
          (value && value.length >= 2) || '주소는 2글자 이상이어야 합니다',
      ];
    },
    ageOptions() {
      // 나이 선택 상자의 옵션
      return [
        { value: '10', label: '10대' },
        { value: '20', label: '20대' },
        { value: '30', label: '30대' },
        // ...
      ];
    },
    annualIncomeOptions() {
      // 연봉 선택 상자의 옵션
      return [
        { value: '1000000', label: '100만 원 이상' },
        { value: '2000000', label: '200만 원 이상' },
        { value: '3000000', label: '300만 원 이상' },
        // ...
      ];
    },
    assetsOptions() {
      // 자산 선택 상자의 옵션
      return [
        { value: '1000000', label: '100만 원 이상' },
        { value: '2000000', label: '200만 원 이상' },
        { value: '3000000', label: '300만 원 이상' },
        // ...
      ];
    },
    bankOptions() {
      // 선호은행 선택 상자의 옵션
      return [
        { value: 'bank1', label: '은행1' },
        { value: 'bank2', label: '은행2' },
        { value: 'bank3', label: '은행3' },
        // ...
      ];
    },
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
  