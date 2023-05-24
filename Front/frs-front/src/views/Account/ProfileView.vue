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
        <p>주소: {{ user.address }}</p>
        <p>나이: {{ user.age }}</p>
        <p>내가 가입한 상품 : {{ user.fin_prdt_nm }}</p>
        <button @click="editMode = true">수정하기</button>
        <div class="d-flex flex-column align-items-center">
          <b-list-group style="width: 70%">
            <b-list-group-item v-for="product in signedProducts" :key="product.id">
              <b-icon icon="check-square" scale="2" variant="success"></b-icon>
              {{ product }}
            </b-list-group-item>
          </b-list-group>
        </div>
      </div>
      <div v-else>
        <p>아이디: {{ user.username }}</p>
        <p>이메일: {{ user.email }}</p> 
        <p>이름: {{ user.nickname }}</p>
        <label for="annual-income">연봉:</label>
        <input id="annual-income" v-model="editedUser.annual_income" type="number" step="1000000"><br>
        <label for="assets">자산:</label>
        <input id="assets" v-model="editedUser.assets" type="number" step="1000000"><br>
        <label for="bank">은행:</label>
        <select id="bank" v-model="editedUser.bank">
          <option v-for="option in bankOptions" :value="option" :key="option.id">{{ option }}</option>
        </select><br>
        <label for="address">주소:</label>
        <input id="address" v-model="editedUser.address" type="text"><br>
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
import axios from 'axios'
export default {
  name: "ProfileView",
  data() {
    return {
      signedProducts: [],
      editMode: false,
      editedUser: {
        annual_income: 0,
        assets: 0,
        bank: "",
        address: "",
        age: 0
      },
      bankOptions: ["KEB하나은행", "SC은행", "경남은행", "광주은행", "국민은행", "기업은행", "농협은행", "대구은행", "부산은행",
       "새마을금고", "산업은행", "수협은행", "신한은행", "신협중앙회", "외환은행","우체국", "우리은행", "저축은행",
        "제주은행", "한국산업은행", "한국수출입은행", "한국은행", "현대은행"]
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin;
    },
    user() {
      return this.$store.getters.getUser;
    },
  },
  created(){
    this.signProducts()
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
        address: this.editedUser.address !== null ? this.editedUser.address : undefined,
        age: this.editedUser.age !== null ? this.editedUser.age : undefined,
        fin_prdt_nm: this.user.fin_prdt_nm,
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
        address: this.user.address,
        age: this.user.age,
        fin_prdt_nm: this.user.fin_prdt_nm,
      };
      this.editMode = false;
    },
    signProducts(){
      if (this.user.fin_prdt_nm){
        for (let product of this.user.fin_prdt_nm.split(',')){
          this.signedProducts.push(product)
        }
      }
    },
  }
}
</script>

<style>

</style>
