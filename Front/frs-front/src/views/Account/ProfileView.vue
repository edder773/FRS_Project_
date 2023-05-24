<template>
  <div id="profile-page">
    <h2>{{user.nickname}}님의 프로필</h2>
    <div v-if="isLogin && user">
      <div v-if="!editMode">
        <p>아이디: {{ user.username }}</p>
        <p>이메일: {{ user.email }}</p> 
        <p>이름: {{ user.nickname }}</p>
        <p>연봉: {{ user.annual_income }}</p>
        <p>자산: {{ user.assets }}</p>
        <p>나이: {{ user.age }}</p>
        <p>은행: {{ user.bank }}</p>
        <p>주소: {{ user.address }}</p>
        <p>직업: {{ user.occupation }}</p>
        <!-- {{ user.financial_products }} -->
        <button @click="editMode = true">수정하기</button>
        <div class="d-flex flex-column align-items-center">
          <b-list-group style="width: 70%">
            <b-card v-for="(product, index) in signedProducts" :key="index" :header="product.fin_prdt_nm" >
              <template #header>
                <b-icon icon="check-square" scale="1" variant="success"></b-icon>
                {{ product.fin_prdt_nm }}
              </template>
              {{ product.mtrt_int }}
            </b-card>
            
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
        <label for="age">나이:</label>
        <input id="age" v-model="editedUser.age" type="number"><br>
        <label for="bank">은행:</label>
        <select id="bank" v-model="editedUser.bank">
          <option v-for="option in bankOptions" :value="option" :key="option.id">{{ option }}</option>
        </select><br>
        <label for="address">주소:</label>
        <select id="address" v-model="editedUser.address">
          <option v-for="option in locationOptions" :value="option" :key="option.id">{{ option }}</option>
        </select><br>
        <label for="occupation">직업:</label>
        <select id="occupation" v-model="editedUser.occupation">
          <option v-for="option in occupationOptions" :value="option" :key="option.id">{{ option }}</option>
        </select><br>
        <button @click="saveChanges">Save</button>
        <button @click="cancelEdit">Cancel</button>
      </div>
    </div>
    <div v-else>
      <p>로------그------인--------필-------수</p>
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
        occupation: null,
        bank: "",
        address: "",
        age: 0
      },
      bankOptions: ["KEB하나은행", "SC은행", "경남은행", "광주은행", "국민은행", "기업은행", "농협은행", "대구은행", "부산은행",
      "새마을금고", "산업은행", "수협은행", "신한은행", "신협중앙회", "외환은행","우체국", "우리은행", "저축은행",
      "제주은행", "한국산업은행", "한국수출입은행", "한국은행", "현대은행"],
      locationOptions: [
        '서울특별시 ','부산광역시 ','대구광역시 ','인천광역시 ','광주광역시 ','대전광역시 ',
        '울산광역시 ','세종특별자치시 ','경기도 ','강원도 ','충청북도 ','충청남도 ',
        '전라북도 ','전라남도 ','경상북도 ','경상남도 ','제주특별자치도 '
      ],
      occupationOptions: ['의사', '교사', '변호사', '엔지니어', '회계사', '디자이너', '개발자', '마케터', '경찰관', '소방관',
      '간호사', '음악가', '배우', '기자', '요리사', '운전사', '경영자', '연구원', '프로그래머', '무직'],
      savingProduct: [],
      depositProducts: []
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
    fetchDeposits() {
      axios.get(`http://127.0.0.1:8000/deposits/products/`)
      .then(response => {
        this.depositProducts = response.data
      })
      .catch(error => {
        console.error(error);
      });
    },
    fetchSavings() {
      axios.get(`http://127.0.0.1:8000/deposits/savings/`)
      .then(response => {
        this.savingProduct = response.data
      })
      .catch(error => {
        console.error(error);
      });
    },
    async fetchSign() {
  try {
    await Promise.all([this.fetchDeposits(), this.fetchSavings()])
    setTimeout(() => {
      this.depositProducts.forEach((product) => {
      this.user.financial_products.forEach((result) => {
        if (product.id == result) {
          this.signedProducts.push(product);
        }
      });
    });
    
    this.savingProduct.forEach((product) => {
      this.user.financial_products.forEach((result) => {
        if (product.id == result) {
          this.signedProducts.push(product);
        }
      })
    })
    },1500)
  } catch (error) {
    console.error(error);
  }
},

  },
  created() {
  this.fetchSign();
}
}
</script>

<style>

</style>
