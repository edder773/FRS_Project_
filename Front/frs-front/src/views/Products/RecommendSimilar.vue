<template>
  <div>
    <h1 style="text-align: center;">나와 비슷한 조건의 다른 사람이 선택한 상품!</h1>
    <div class="d-flex flex-column align-items-center">
      <div v-for="product in productresult" :key="product.id">
        <b-card style="width: 1000px" border-variant="secondary" :header="product.fin_prdt_nm" header-border-variant="secondary" align="center">
          <div class="card-body">
            <b-card-text style="height: 100%">{{ product.mtrt_int }}</b-card-text>
          </div>
          <div class="d-flex justify-content-end mt-2">
            <b-button variant="primary" @click="addProduct(product)">가입하기</b-button>
          </div>
        </b-card>
        <hr>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import axios from 'axios'

export default {
  data() {
    return {
      recommendedProducts: [],
      recommendProducts: [],
      recommendSaving: [],
      productresult: []
    };
  },
  computed: {
    ...mapGetters(['getUser', 'getToken']),
  },
  methods: {
    ...mapActions(['addFinancialProduct']),
    fetchRecommendedProducts() {
      const token = this.getToken
      axios.get('http://127.0.0.1:8000/deposits/similar/', {
        headers: {
          Authorization: `Token ${token}`,
        },
      })
        .then(response => {
          this.recommendedProducts = response.data.recommended_products
          this.findProducts();
        })
        .catch(error => {
          console.error(error);
        });
    },
    fetchrecommendProducts() {
      axios.get(`http://127.0.0.1:8000/deposits/products/`)
        .then(response => {
          this.recommendProducts = response.data;
          this.findProducts();
        })
        .catch(error => {
          console.error(error);
        });
    },
    fetchSavingProducts() {
      axios.get(`http://127.0.0.1:8000/deposits/savings/`)
        .then(response => {
          this.recommendSaving = response.data;
          this.findProducts();
        })
        .catch(error => {
          console.error(error);
        });
    },
    findProducts() {
      this.productresult = [];
      for (let product of this.recommendedProducts) {
        for (let result of this.recommendProducts) {
          if (product == result.fin_prdt_cd) {
            this.productresult.push(result);
          }
        }
      }
      for (let product of this.recommendSaving) {
        for (let result of this.recommendProducts) {
          if (product == result.fin_prdt_cd) {
            this.productresult.push(result);
          }
        }
      }
    },
    addProduct(product) {
      const finPrdtCd = product.fin_prdt_cd;
      const fin_prdt_nm = product.fin_prdt_nm;
      this.addFinancialProduct({ finPrdtCd, fin_prdt_nm });
    }
  },
  created() {
    this.fetchrecommendProducts();
    this.fetchRecommendedProducts();
    setTimeout(() => {
      this.fetchSavingProducts();
    }, 5000);
  }
}
</script>

<style>
</style>
