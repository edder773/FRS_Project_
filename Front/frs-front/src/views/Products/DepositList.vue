<template>
  <div id="deposit-page">
    <div id="deposit-router">
      <a href="/deposit">예금비교</a> |
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
          <tr v-for="product in products" :key="product.id" @click="openModal(product)">
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
    <b-modal v-if="selectedProduct" v-model="showModal" @hide="closeModal">
    <h3>{{ selectedProduct.fin_prdt_nm }}</h3>
    <h4>{{ selectedProduct.kor_co_nm }}</h4>
    <hr>
    <div>
    <KakaoMapCom :bank="selectedProduct.kor_co_nm"/>
    <!-- Modal content goes here -->
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
      options: {},
      selectedProduct: null,
      recommendItem: false,
      showModal: false,
    }
  },
  created() {
    this.fetchProducts()
  },
  methods: {
    fetchProducts() {
      axios.get('http://127.0.0.1:8000/deposits/products/')
        .then(response => {
          this.products = response.data
        })
        .catch(error => {
          console.error(error)
        })
    },
    openModal(product) {
      this.selectedProduct = product
      this.showModal = false // 모달을 닫음
      console.log('Modal')
      this.$nextTick(() => {
        this.showModal = true // 모달을 다시 열어 갱신
      })
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
    }
  }
}
</script>
<style scoped>

#deposit-router{
  display: block;
}

.table-container{
  display: flex;
  align-items: right;
  justify-content: right;
}
td{
  cursor: pointer;
}
</style>
