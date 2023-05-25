<template>
  <div id="deposit-page">
    <div id="deposit-router">
      <a href="/deposit">예금비교</a> |
      <a href="/saving">적금비교</a> |
      <h2>정기예금</h2>
      <p @click="openRecommend">추천받기</p>
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
    <div class="filter-container">
      <label for="month-filter">개월 수:</label>
      <select id="month-filter" v-model="selectedMonth">
        <option value="">전체</option>
        <option value="6">6개월</option>
        <option value="12">12개월</option>
        <option value="24">24개월</option>
        <option value="36">36개월</option>
      </select>
      <label for="bank-filter">은행 이름:</label>
      <select id="bank-filter" v-model="selectedBank">
        <option value="">전체</option>
        <option v-for="bank in banks" :value="bank" :key="bank">{{ bank }}</option>
      </select>
      <button @click="applyFilter">확인</button>
    </div>
    <b-table striped hover style="cursor: pointer;" @row-clicked="openModal" :items="filteredProducts" :fields="tableFields">
      <template #cell(fin_prdt_nm)="row">
        <p>{{ row.value }}</p>
      </template>
    </b-table>
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
    getImagePath(image) {
      return require(`@/views/Image/${image}`)
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
h3{
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'TheJamsil5Bold';
  font-weight: 500;
}
h4{
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'TheJamsil5Bold';
  font-weight: 400;
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