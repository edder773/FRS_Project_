<template>
  <div>
    <div v-for="product in products" :key="product.id">
        <p>{{ product.kor_co_nm }}
          {{ product.fin_prdt_nm }} </p>

    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name:'DepositProduct',
    data() {
    return {
      products: [],
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
}
}
</script>

<style>

</style>