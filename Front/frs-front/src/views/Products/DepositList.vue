<template>
  <div id="deposit-page">
    <div id="deposit-router">
      <a href="/deposit">예금비교asdas</a> |
      <a href="/saving">적금비교</a> |
      <h2>정기예금</h2>
      <p @click="openRecommend">추천받기</p>
    </div>
    <b-modal v-model="recommendItem" @hide="closeRecommend">
      <h3>추천받기</h3>
      <a href="/recommend">
        <b-card overlay img-src="https://picsum.photos/2000/1500/?image=3" img-alt="Card Image" text-variant="white" title="나와 맞는 금융 상품 찾기">
          <b-card-text>
            간단한 미니 게임을 통해 나와 맞는 금융 상품을 찾아보세요
          </b-card-text>
        </b-card>
      </a>
    </b-modal>
    
    <div class="table-container">
      <!-- 필터링 -->
      <div class="filter-container">
      <label for="filter-option">필터링 옵션:</label>
      <select id="filter-option" v-model="selectedOption">
        <option value="">전체</option>
        <option value="6">6개월</option>
        <option value="12">12개월</option>
        <option value="24">24개월</option>
        <option value="36">36개월</option>
      </select>
      <button @click="filteredProducts">확인</button>
      </div>
      <table class="table table-striped">
        <thead>
          <tr>
            <th scope="col">번호</th>
            <th scope="col">6개월</th>
            <th scope="col">12개월</th>
            <th scope="col">24개월</th>
            <th scope="col">36개월</th>
            <th scope="col">금융기관</th>
            <th scope="col">상품</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="product in filterProducts" :key="product.id" :v-model="fetchOptions(product.id)">
            <td @click="openModal(product)">{{ product.id }}</td>
            <td @click="openModal(product)"><DepositOption6 :productId="product.id"/></td>
            <td @click="openModal(product)"><DepositOption12 :productId="product.id"/></td>
            <td @click="openModal(product)"><DepositOption24 :productId="product.id"/></td>
            <td @click="openModal(product)"><DepositOption36 :productId="product.id"/></td>
            <td @click="openModal(product)">{{ product.kor_co_nm }}</td>
            <td @click="openModal(product)">{{ product.fin_prdt_nm }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <b-modal v-if="selectedProduct" v-model="showModal" @hide="closeModal" size="xl">
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
import DepositOption6 from '@/components/DepositOption6.vue'
import DepositOption12 from '@/components/DepositOption12.vue'
import DepositOption24 from '@/components/DepositOption24.vue'
import DepositOption36 from '@/components/DepositOption36.vue'
import { BModal } from 'bootstrap-vue'

export default {
  name: 'DepositList',
  components: {
    BModal,
    // VBModal,
    KakaoMapCom,
    DepositOption6,
    DepositOption12,
    DepositOption24,
    DepositOption36,

  },
  data() {
    return {
      products: [],
      tempoptions: [],
      monthoptions: [],
      options: {},
      selectedProduct: null,
      recommendItem: false,
      showModal: false,
      selectedOption: '',
      filterProducts: [],
    }
  },
  created() {
    this.fetchProducts()
    // this.fetchOptions()
    setTimeout(() => {
    this.filteredProducts()
  }, 1000)
  },
  computed: {

  },
  methods: {
    fetchProducts() {
      axios.get('http://127.0.0.1:8000/deposits/products/')
        .then(response => {
          this.products = response.data
          console.log(response)
        })
        .catch(error => {
          console.error(error)
        })
    },
    fetchOptions(productId) {
      axios
        .get('http://127.0.0.1:8000/deposits/products-option/')
        .then(response => {
          // Filter options based on productId
          const tempoptions = response.data.filter(option => option.fin_prdt_cd === productId)
          this.monthoptions.push(tempoptions.save_trm)
        })
        .catch(error => {
          console.error(error)
        })
    },
    openModal(product) {
      this.selectedProduct = product
      this.showModal = true // 모달을 닫음
      console.log('Modal')
      // this.$nextTick(() => {
      //   this.showModal = true // 모달을 다시 열어 갱신
      // })
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
    filteredProducts() {
      if (this.selectedOption === '') {
        this.filterProducts = this.products; // 선택한 옵션이 없으면 전체 제품을 렌더링
      } else {
        const option = parseInt(this.selectedOption);
        this.filterProducts = this.products.filter(() => {
          return this.monthoptions.includes(option); // 선택한 옵션이 저장된 리스트에 있는 경우에만 렌더링
        });
      }
    },

}
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

</style>
