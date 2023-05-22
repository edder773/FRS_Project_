<template>
  <div id="profile-page">
    <h2>User Profile</h2>
    <div v-if="isLogin && user">
      <div v-if="!editMode">
        <p>아이디: {{ user.username }}</p>
        <p>이메일: {{ user.email }}</p> 
        <p>이름: {{ user.nickname }}</p>
        <p>연봉: {{ user.annual_income }}</p>
        <p>자산: {{ user.assets }}</p>
        <p>은행: {{ user.bank }}</p>
        <p>주소: {{ user.location }}</p>
        <p>나이: {{ user.age }}</p>
        <button @click="editMode = true">수정하기</button>
      </div>
      <div v-else>
        <p>아이디: {{ user.username }}</p>
        <p>이메일: {{ user.email }}</p> 
        <p>이름: {{ user.nickname }}</p>
        <label for="annual-income">연봉:</label>
        <input id="annual-income" v-model="editedUser.annual_income" type="number"><br>
        <label for="assets">자산:</label>
        <input id="assets" v-model="editedUser.assets" type="number"><br>
        <label for="bank">은행:</label>
        <input id="bank" v-model="editedUser.bank" type="text"><br>
        <label for="location">주소:</label>
        <input id="location" v-model="editedUser.location" type="text"><br>
        <label for="age">나이:</label>
        <input id="age" v-model="editedUser.age" type="number"><br>
        <button @click="saveChanges">Save</button>
        <button @click="cancelEdit">Cancel</button>
      </div>
    </div>
    <div v-else>
      <p>Please log in to view your profile.</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProfileView",
  data() {
    return {
      editMode: false,
      editedUser: {
        annual_income: 0,
        assets: 0,
        bank: "",
        location: "",
        age: 0
      }
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin;
    },
    user() {
      return this.$store.getters.getUser;
    }
  },
  methods: {
    saveChanges() {
      const payload = {
        username: this.user.username,
        email: this.user.email,
        nickname: this.user.nickname,
        annual_income: this.editedUser.annual_income !== null ? this.editedUser.annual_income : undefined,
        occupation: this.editedUser.occupation !== null ? this.editedUser.occupation : undefined,
        assets: this.editedUser.assets !== null ? this.editedUser.assets : undefined,
        bank: this.editedUser.bank !== null ? this.editedUser.bank : undefined,
        location: this.editedUser.location !== null ? this.editedUser.location : undefined,
        age: this.editedUser.age !== null ? this.editedUser.age : undefined,
        }
      this.editMode = false;
      this.$store.dispatch('profileChange', payload)
        console.log(payload)
    },
    cancelEdit() {
      this.editedUser = {
        username: this.user.username,
        email: this.user.email,
        nickname: this.user.nickname,
        annual_income: this.user.annual_income,
        assets: this.user.assets,
        bank: this.user.bank,
        location: this.user.location,
        age: this.user.age
      };
      this.editMode = false;
    },
    
  }
};
</script>

<style>
#profile-page {
  margin-top: 80px;
}
</style>
