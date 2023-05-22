<template>
  <div id="deposit-page">
    <a href="/deposit">예금비교</a> |
    <a href="/saving">적금비교</a> |
    <h2>정기예금</h2>
    <div class="table-container">
      <table class="table table-striped">
        <thead>
          <tr>
            <th scope="col">번호</th>
            <th scope="col">기본금리</th>
            <th scope="col">우대금리</th>
            <th scope="col">금융기관</th>
            <th scope="col">상품</th>
          </tr>
        </thead>
        <tbody>
          <div v-for="product in products" :key="product.id">
            <td>{{ product.id }}</td>
            <td><DepositOption :productId="product.id"/></td>
            <td>{{ product.kor_co_nm }}</td>
            <td>{{ product.fin_prdt_nm }}</td>
          </div>
        </tbody>
      </table>
    </div>
    
    <div class="modal" v-if="selectedProduct" @click.self="closeModal">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">{{ selectedProduct.fin_prdt_nm }}</h5>
            <button type="button" class="close" @click="closeModal">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <h6>{{ selectedProduct.kor_co_nm }}</h6>
            <KakaoMap/>
            <p>가입 가능 유형: {{ selectedProduct.join_member }}</p>
            <p>상품 공시 시작일: {{ selectedProduct.dcls_strt_day }}</p>
            <p v-if="selectedProduct.max_limit">가입한도: {{ selectedProduct.max_limit }} 원</p>
            <p>{{ selectedProduct.etc_note }}</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" @click="closeModal">닫기</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import KakaoMap from '@/components/KakaoMap.vue'
// import DepositProduct from '@/components/DepositProduct.vue'
import DepositOption from '@/components/DepositOption.vue'

export default {
  name: 'DepositList',
  components: {
    KakaoMap,
    // DepositProduct,
    DepositOption,
  },
  data() {
    return {
      products: [],
      options: {},
      selectedProduct: null,
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
          this.fetchOptions() // fetchOptions()를 호출하여 options 가져오기
        })
        .catch(error => {
          console.error(error)
        })
    },
    // fetchOptions() {
    //   axios.get('http://127.0.0.1:8000/deposits/products-option/')
    //     .then(response => {
    //       const options = {}
    //       response.data.filter(option => {
    //         const productId = option.fin_prdt_cd_id
    //         if (options[productId]) {
    //           options[productId].push(option)
    //         } else {
    //           options[productId] = [option]
    //         }
    //       })
    //       this.options = options
    //     })
    //     .catch(error => {
    //       console.error(error)
    //     })
    // },
    // getProductOptions(productId) {
    //   return this.options[productId] || []
    // },
    openModal(productId) {
      const selectedProduct = this.products.find(product => product.id === productId)
      this.selectedProduct = selectedProduct
    },
    closeModal() {
      this.selectedProduct = null
    },
  }
}
</script>

<style>
#deposit-page {
  margin-top: 100px;
}

.table-responsive {
  overflow-x: auto;
}

.modal {
  display: flex;
  align-items: center;
  justify-content: center;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 9999;
}

.modal-dialog {
  max-width: 600px;
}

.modal-content {
  background-color: #fff;
  padding: 20px;
  border-radius: 4px;
}

.modal-header {
  display: flex;
  justify-content: flex-end;
}

.close:hover {
  opacity: 1;
  color: #000;
}
</style>
