<template>
  <div id="similar-page">
    <div class="d-flex flex-column align-items-center">
      <h1 style="margin: 0;font-family: 'TheJamsil5Bold';">나와 비슷한 조건의 다른 사람이 선택한 상품!</h1>
      <br><br><br>
      <div v-for="product in productresult" :key="product.id">
        <b-card style="width: 1000px;font-family: 'TheJamsil5Bold';" border-variant="secondary" :header="product.fin_prdt_nm" header-border-variant="secondary" align="center">
          
          <div class="card-body">
            <b-card-text style="height: 100%;font-family: 'GangwonEdu_OTFBoldA'; font-weight: 200;">{{ product.mtrt_int }}</b-card-text>
          </div>
          <div class="d-flex justify-content-end mt-2">
            <b-button variant="primary" @click="checkProduct(product)">
           {{ checkIn(product) ? '해지하기' : '가입하기' }}
          </b-button>
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
      productresult: [],
    };
  },
  computed: {
    ...mapGetters(['getUser', 'getToken']),
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
    }
  },
  methods: {
    ...mapActions(['addFinancialProduct']),
    getArticles() {
      if (this.isLogin) {
        this.$store.dispatch('getArticles')
      } else {
        alert('로그인이 필요한 페이지입니다...')
        this.$router.push({ name: 'home' })
      }
    },
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
    checkIn(product){
      return this.getUser.financial_products.includes(product.id)
    },
  checkProduct(product) {
  const user = this.getUser
  console.log(user.financial_products)
  const payload = {
    user_id: user.pk,  // 'user_id' 키에 사용자 ID 값을 전달
    product_id: product.id  // 'product_id' 키에 상품 ID 값을 전달
  }
  this.$store.dispatch('addProduct', payload)
}
},
  created() {
    this.getArticles()
    this.fetchrecommendProducts();
    this.fetchRecommendedProducts();
    setTimeout(() => {
      this.fetchSavingProducts();
    }, 5000);
  }
}
</script>

<style scoped>
#similar-page{
  font-family: 'GangwonEdu_OTFBoldA';
  margin-top: 70px;
}
</style>
