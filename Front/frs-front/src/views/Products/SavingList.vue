<template>
  <div id="deposit-page" class="container">
    <div><h2>예/적금 비교</h2></div>
    <div id="deposit-router">
      <div class="deposit-links">
        <a href="/deposit" class="deposit-link">예금비교</a><div class="deposit-link"> |</div>
        <a href="/saving" class="deposit-link">적금비교</a> 
      </div>
      <hr>
      <b-modal size="lg" title="금융 상품 추천 받기!" v-model="recommendItem" @hide="closeRecommend" centered>
        <b-row>
          <b-col>
            <a href="/recommend">
              <b-card overlay :img-src="getImagePath('recommend.jpg')" img-alt="Card Image" text-variant="white" title="금융BTI">
                <b-card-text>
                  간단한 미니 게임을 통해 나와 맞는 금융 상품을 찾아보세요
                </b-card-text>
              </b-card>
            </a>
          </b-col>
          <b-col>
            <a href="/similar">
              <b-card overlay :img-src="getImagePath('similar.png')" img-alt="Card Image" text-variant="white" title="나와 비슷한 사용자는?">
                <b-card-text>
                  나와 비슷한 사용자들이 가입한 상품이 궁금하다면?
                </b-card-text>
              </b-card>
            </a>
          </b-col>
        </b-row>
      </b-modal>
    </div>
    <div class="deposit-container">
      <!-- 필터부분 -->
      <div class="filter-container">
        <div class="filter-borderbox">
          <b-card title="상품 추천!" :img-src="getImagePath('recommendation.jpeg')" img-alt="Image" img-top tag="article" style="max-width: 20rem;font-family: 'TheJamsil5Bold';" class="mb-2"  >
            <b-card-text>
              <p style="font-family: 'GangwonEdu_OTFBoldA';font-size:20px;">나랑 맞는 상품이 어떤건지 궁금하다면?</p>
              <div class="text-center">
                <b-button class="deposit-button" style="background-color: #ff5b5b;border: none;" @click="openRecommend">추천받기</b-button>
              </div>
            </b-card-text>
          </b-card>
          <label for="month-filter" class="filterdetail-margin" style="margin-top: 10px;">개월 수</label>
          <select id="month-filter" v-model="selectedMonth" class="deposit-select">
            <option value="">전체</option>
            <option value="6">6개월</option>
            <option value="12">12개월</option>
            <option value="24">24개월</option>
            <option value="36">36개월</option>
          </select>
          <br><br>
          <label for="bank-filter" class="filterdetail-margin">은행 이름</label>
          <select id="bank-filter" v-model="selectedBank" class="deposit-select" style="width: 100%;">
            <option value="">전체</option>
            <option v-for="bank in banks" :value="bank" :key="bank">{{ bank }}</option>
          </select>
          <div class="apply-button-container">
            <button @click="applyFilter" class="apply-button">확인</button>
          </div>
        </div>
      </div>
      <div class="deposittable-container deposit-option">
        <b-table striped hover style="cursor: pointer;" @row-clicked="openModal" :items="filteredProducts" :fields="tableFields">
          <template #cell(fin_prdt_nm)="row">
            <p>{{ row.value }}</p>
          </template>
        </b-table>
      </div>
    </div>
    <b-modal id="modalId" v-if="selectedProduct" v-model="showModal" @hide="closeModal" size="xl">
      <h3>{{ selectedProduct.fin_prdt_nm }}</h3>
      <h4>{{ selectedProduct.kor_co_nm }}</h4>
      <hr>
      <div class="modal-content">
        <div class="left-section">
          <KakaoMapCom :bank="selectedProduct.kor_co_nm"/>
        </div>
        <div class="right-section">
          <div class="detail-info">
            <p><strong>상품 공시 시작일:</strong> {{ selectedProduct.dcls_strt_day }}</p>
            <p><strong>우대 조건:</strong> {{ selectedProduct.spcl_cnd }}</p>
            <p><strong>가입 가능 유형:</strong> {{ selectedProduct.join_member }}</p>
            <p><strong>기타 참고 사항:</strong> {{ selectedProduct.etc_note }}</p>
          </div>
        </div>
      </div>
    </b-modal>
  </div>
</template>


<script>
import axios from 'axios'
import KakaoMapCom from '@/components/KakaoMapCom.vue'
import { BTable } from 'bootstrap-vue'
import { BModal } from 'bootstrap-vue'

export default {
  name: 'SavingList',
  components: {
    BTable,
    BModal,
    KakaoMapCom,
  },
  data() {
    return {
      products: [],
      options: [],
      selectedMonth: '',
      selectedBank: '',
      selectedProduct: null,
      recommendItem: false,
      showModal: false,
      filteredProducts: [],
      tableFields: [
        { key: 'id', label: '번호' },
        { key: '6', label: '6개월' },
        { key: '12', label: '12개월' },
        { key: '24', label: '24개월' },
        { key: '36', label: '36개월' },
        { key: 'kor_co_nm', label: '은행 이름' },
        { key: 'fin_prdt_nm', label: '상품 이름' },
      ],
      banks:['경남은행','광주은행', '국민은행', '농협은행주식회사', '부산은행', '수협은행', '신한은행', '우리은행', '전북은행', '중소기업은행', '주식회사 케이뱅크', '주식회사 카카오뱅크', '토스뱅크 주식회사', '한국산업은행', '한국스탠다드차타드은행', '하나은행', '제주은행'],
    }
  },
  created() {
    this.fetchProducts().then(() => {
      return this.fetchOptions()
    }).then(() => {
      this.filteredProducts = this.formattedProducts
    }).catch((error) => {
      console.error(error)
    })
  },
  methods: {
    getImagePath(image) {
      return require(`@/views/Image/${image}`);
    },
    fetchProducts() {
      return new Promise((resolve, reject) => {
        axios
        .get('http://127.0.0.1:8000/deposits/savings/')
        .then((response) => {
          this.products = response.data
          this.fetchOptions()
          resolve()
        })
        .catch((error) => {
          console.error(error)
          reject(error)
        })
      })
    },
    fetchOptions() {
      return new Promise((resolve, reject) => {
        axios
        .get('http://127.0.0.1:8000/deposits/savings-option/')
        .then((response) => {
          this.options = response.data
          resolve()
        })
        .catch((error) => {
          console.error(error)
          reject(error)
        })
      })
    },
    getProductOptions(productId) {
      return this.options.filter((option) => option.fin_prdt_cd === productId)
    },
    applyFilter() {
      if (this.selectedMonth || this.selectedBank) {
        this.filteredProducts = this.formattedProducts.filter((product) => {
          const monthFilter = this.selectedMonth
          ? product[this.selectedMonth] !== '-'
          : true
          const bankFilter = this.selectedBank
          ? product.kor_co_nm === this.selectedBank
          : true
          return monthFilter && bankFilter
        })
      } else {
        this.filteredProducts = this.formattedProducts
      }
    },
    openModal(product) {
      this.selectedProduct = product
      this.showModal = true
    },  
    closeModal() {
      this.selectedProduct = null
      this.showModal = false
    },    
    openRecommend() {
      this.recommendItem = true
    },
    closeRecommend() {
      this.recommendItem = false
    },

  },
  computed: {
    formattedProducts() {
      const months = ['6', '12', '24', '36']
      return this.products.map((product) => {
        const options = this.getProductOptions(product.id)
        const optionData = {}
        options.forEach((option) => {
          optionData[option.save_trm] = option.intr_rate
        })
        const formattedOptionData = months.reduce((result, month) => {
          result[month] = optionData[month] || '-'
          return result
        }, {})
        return {
          id: product.id,
          ...formattedOptionData,
          kor_co_nm: product.kor_co_nm,
          fin_prdt_nm: product.fin_prdt_nm,
          dcls_strt_day: product.dcls_strt_day,
          spcl_cnd: product.spcl_cnd,
          join_member: product.join_member,
          etc_note: product.etc_note,
        }
      })
    },
  },
}
</script>

<style scoped>
#deposit-page{
  margin-top: 50px;
}
h2{
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'TheJamsil5Bold';
  font-weight: 600;
  font-size: 50px;
}
h3{
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'ONE-Mobile-Title';
  font-weight: 500;
}
h4{
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'ONE-Mobile-Title';
  font-weight: 400;
}
.deposit-links {
  margin-top: 20px;
  display: flex;
  justify-content: center;
}
.deposit-option {
    font-family: 'TheJamsil5Bold';
    text-align: center;
}
.deposit-link {
  font-family: 'ONE-Mobile-Title';
  color: #000000;
  font-size: 23px;
  text-decoration: none;
  padding: 10px;
  margin-right: 10px;
  transition: color 0.3s;
}

.deposit-link:hover,
.deposit-link.active {
  color: #b4b4b4;
}
#deposit-router{
  display: block;
}

td{
  cursor: pointer;
}

.modal-content {
  display: flex;
  flex-direction: row;
}

.left-section {
  flex: 1;
}
.right-section {
  flex: 1;
  font-family: 'GangwonEdu_OTFBoldA';
  font-size: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.deposit-container {
  display: flex;
}
.filter-container {
  display: flex;
  align-items: center;
  flex-direction: column;
  align-items: flex-start;
  /* width: 30%;  */
  border-right: 1px solid #ccc;
  padding-right: 10px;
}
.deposittable-container {
  flex: 1;
  width: 70%;
  padding-left: 10px;
}
.deposit-select {
  padding: 6px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #f7f7f7;
  width: 100%;
}
.filterdetail-margin {
  margin-bottom: 10px;
  font-family: 'ONE-Mobile-Title';
}
.filter-borderbox{
  border: 1px solid #ccc;
  border-radius: 10px; 
  padding: 16px 8px;
  margin-top: 20px;
}
.apply-button {
  padding: 8px 16px;
  font-family: 'TheJamsil5Bold';
  border: none;
  border-radius: 4px;
  background-color: #4caf50;
  color: white;
  cursor: pointer;
}
.apply-button-container {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}
.detail-info {
  width: 80%; /* 적절한 너비로 조정 */
  margin: 0 auto; /* 가운데 정렬 */
}

.detail-info p {
  margin-bottom: 10px; /* 각 항목 사이의 간격 조정 */
}
.filter-container {
  margin-bottom: 20px;
}

</style>