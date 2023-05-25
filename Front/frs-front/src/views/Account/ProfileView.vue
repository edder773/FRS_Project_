<template>
  <div id="profile-page" class="container">
    <div class="profile-image">
      <div class="profile-name">{{user.nickname}}님의 프로필</div>
    </div>
    <div v-if="isLogin && user">
      <div v-if="!editMode">
        <div class="profile-table">
        <table class="table table-bordered">
          <tbody class="text-center">
            <tr>
              <th>아이디</th>
              <td>{{ user.username }}</td>
            </tr>
            <tr>
              <th>이메일</th>
              <td>{{ user.email }}</td>
            </tr>
            <tr>
              <th>이름</th>
              <td>{{ user.nickname }}</td>
            </tr>
            <tr>
              <th>연봉</th>
              <td>{{ user.annual_income }}</td>
            </tr>
            <tr>
              <th>자산</th>
              <td>{{ user.assets }}</td>
            </tr>
            <tr>
              <th>나이</th>
              <td>{{ user.age }}</td>
            </tr>
            <tr>
              <th>은행</th>
              <td>{{ user.bank }}</td>
            </tr>
            <tr>
              <th>주소</th>
              <td>{{ user.address }}</td>
            </tr>
            <tr>
              <th>직업</th>
              <td>{{ user.occupation }}</td>
            </tr>
          </tbody>
        </table>
      </div>
        <!-- {{ user.financial_products }} -->
        <div class="profile-button"><button @click="editMode = true">수정하기</button></div>
        <hr><br>
        <!-- 가입한 목록 나오기 -->
        <div class="profile-join">
        <h2>🎁내가 가입한 상품🎁</h2>
        <div class="profile-card d-flex flex-column align-items-center">
          <b-list-group style="width: 70%">
            <b-card v-for="(product, index) in signedProducts" :key="index" :header="product.fin_prdt_nm" >
              <template #header>
                <b-icon icon="check-square" scale="1" variant="success" class="me-2 profilecard-title"></b-icon>
                {{ product.fin_prdt_nm }}
              </template>
              {{ product.mtrt_int }}
            </b-card>
          </b-list-group>
          <br>
        </div>
        <div class="profile-chart">
          <div id="chart" ref="chart" style="width: 100%; height: 400px;"></div>
        </div>
      </div>
      </div>
      <!-- 여기까지 가입한 목록 -->
      <div v-else>
        <div class="profile-table">
        <table class="table table-bordered">
          <tbody class="text-center">
            <tr>
              <th>아이디</th>
              <td>{{ user.username }}</td>
            </tr>
            <tr>
              <th>이메일</th>
              <td>{{ user.email }}</td>
            </tr>
            <tr>
              <th>이름</th>
              <td>{{ user.nickname }}</td>
            </tr>
            <tr>
              <th>연봉</th>
              <td>
                <input id="annual-income" v-model="editedUser.annual_income" type="number" step="1000000">
              </td>
            </tr>
            <tr>
              <th>자산</th>
              <td>
                <input id="assets" v-model="editedUser.assets" type="number" step="1000000">
              </td>
            </tr>
            <tr>
              <th>나이</th>
              <td>
                <input id="age" v-model="editedUser.age" type="number">
              </td>
            </tr>
            <tr>
              <th>은행</th>
              <td>
                  <select id="bank" v-model="editedUser.bank">
                  <option v-for="option in bankOptions" :value="option" :key="option.id">{{ option }}</option>
                </select>
              </td>
            </tr>
            <tr>
              <th>주소</th>
              <td>
                <select id="address" v-model="editedUser.address">
                  <option v-for="option in locationOptions" :value="option" :key="option.id">{{ option }}</option>
                </select>
              </td>
            </tr>
            <tr>
              <th>직업</th>
              <td>
                <select id="occupation" v-model="editedUser.occupation">
                  <option v-for="option in occupationOptions" :value="option" :key="option.id">{{ option }}</option>
                </select>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="profile-button" style="margin-bottom: 40px;">
        <button @click="saveChanges">저장하기</button>
        <button @click="cancelEdit">취소</button>
      </div>
      <hr><br>
      </div>
    </div>
    <div v-else>
      <p>로------그------인--------필-------수</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import * as echarts from "echarts"
export default {
  name: "ProfileView",
  data() {
    return {
      signedProducts: [],
      editMode: false,
      option :[], //chart를 위한 option
      editedUser: {
        annual_income: 0,
        assets: 0,
        occupation: null,
        bank: null,
        address: null,
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
      // savingProduct: [],
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
  mounted() {
    let chartDom = this.$refs.chart;
    let myChart = echarts.init(chartDom);

    if (myChart != null && myChart != '' && myChart != undefined) {
      myChart.dispose();
    }

    myChart = echarts.init(chartDom);

    let option = {
      tooltip: {
        trigger: 'item',
      },
      legend: {
        bottom: '10px',
        width: '300px',
      },
      series: this.series,
    };

    option && myChart.setOption(option);

    window.addEventListener('resize', () => {
      myChart.resize();
    });
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
      }
      this.editMode = false;
      console.log(payload)
      this.$store.dispatch('profileChange', payload)
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
    // fetchSavings() {
    //   axios.get(`http://127.0.0.1:8000/deposits/savings/`)
    //   .then(response => {
    //     this.savingProduct = response.data
    //   })
    //   .catch(error => {
    //     console.error(error);
    //   });
    // },
    async fetchSign() {
  try {
    await Promise.all([this.fetchDeposits()])
    setTimeout(() => {
      this.depositProducts.forEach((product) => {
      this.user.financial_products.forEach((result) => {
        if (product.id == result) {
          this.signedProducts.push(product);
        }
      })
    })
    
    // this.savingProduct.forEach((product) => {
    //   this.user.financial_products.forEach((result) => {
    //     if (product.id == result) {
    //       this.signedProducts.push(product);
    //     }
    //   })
    // })
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

<style scoped>
table{
  font-family: 'TheJamsil5Bold';
  font-size: 20px;
  
}
h2{
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'TheJamsil5Bold';
  font-weight: 600;
  font-size: 30px;
  margin-bottom: 20px;
}
.profile-button{
  display: flex;
  align-items: center;
  justify-content: center;
}
.profile-image{
  background-image: url('@/views/Image/chart.jpg');
  background-size: cover;
  height: 230px;
  margin-bottom: 30px;
  margin-top: 15px;
}
.profile-name{
  font-size: 30px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding-top: 80px;
  color: rgb(184, 183, 183);
  font-family: 'TheJamsil5Bold';
  font-weight: 300;
}

button {
  padding: 6px 12px;
  border: none;
  border-radius: 4px;
  background-color: #383838;
  color: #fff;
  cursor: pointer;
  margin-left: 10px; /* 버튼 간격을 위해 추가 */
  font-family: 'ONE-Mobile-Title';
}

.text-center {
  text-align: center;
}
.profile-card{
  font-family: 'GangwonEdu_OTFBoldA';
  font-weight: 300;
  margin-bottom: 100px;
}
.profilecard-title{
  font-family: 'GangwonEdu_OTFBoldA';
  font-weight: 700;
}
</style>