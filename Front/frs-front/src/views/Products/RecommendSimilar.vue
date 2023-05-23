<template>
    <div>
      <h1>나와 비슷한 조건의 다른 사람이 선택한 상품!</h1>
        <div v-for="product in productresult" :key="product.id">
            <p>상품명: {{ product.fin_prdt_nm }} </p>
            <p>상세 정보:{{ product.mtrt_int }}</p>
            <hr>
        </div>
    </div>
  </template>
  
  <script>
  import { mapGetters } from 'vuex'
  import axios from 'axios'
  export default {
    data() {
      return {
        recommendedProducts: [],
        recommendProducts: [],
        productresult: []
      };
    },
    computed:{
    ...mapGetters(['getUser','getToken']),
    },
    methods: {
      fetchRecommendedProducts() {
        const token = this.getToken
        axios.get('http://127.0.0.1:8000/deposits/similar/', {
          headers: {
            Authorization: `Token ${token}`,
          },
        })
          .then(response => {
            this.recommendedProducts = response.data.recommended_products;
          })
          .catch(error => {
            console.error(error);
          });
      },
      fetchrecommendProducts() {
        axios.get(`http://127.0.0.1:8000/deposits/products/`)
        .then(response => {
        this.recommendProducts = response.data
      })
      .catch(error => {
        console.error(error);
      });
    },
    findProducts(){
        for (let product of this.recommendedProducts){
            for (let result of this.recommendProducts){
                if (product == result.fin_prdt_cd){
                    this.productresult.push(result)
                }
            }
        }
    }
    },
    created(){
        this.fetchrecommendProducts()
        this.fetchRecommendedProducts()
        setTimeout(() => {
        this.findProducts();
    }, 5000);
    }
  }
  </script>
  
  <style>
  
  </style>
  