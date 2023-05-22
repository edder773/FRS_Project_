<template>
  <div>
    <h1>예금리스트</h1>
    <ul>
      <li v-for="product in products" :key="product.id">
        <p> 상품명 : {{ product.fin_prdt_nm }}</p>
        <p> 은행명 : {{ product.kor_co_nm }}</p>
        <p> 상품 공시 월 : {{ product.dcls_month }}</p>
        <p> 상품 공시 시작일 : {{ product.dcls_strt_day }}</p>
        <p> 이자율 조건 : {{ product.mtrt_int }}</p>
        <p> 특별 조건 : {{ product.spcl_cnd }}</p>
        <p> 가입 가능 유형 : {{ product.join_member }}</p>
        <p> 가입한도 : {{ product.max_limt }}</p>
        <p> 기타 참고 사항 : {{ product.etc_note }}</p>
        <hr>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'depositList',
  data() {
    return {
      products: []
    }
  },
  created() {
    this.fetchProducts()
  },
  methods: {
    fetchProducts() {
      axios.get('http://127.0.0.1:8000/deposits/products/') // Django 서버의 URL에 맞게 업데이트
        .then(response => {
          this.products = response.data
        })
        .catch(error => {
          console.error(error)
        })
    }
  }
}
</script>
