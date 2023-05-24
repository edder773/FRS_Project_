<template>
  <div>
    <div v-for="option in options" :key="option.id">
      <div v-if="option.save_trm === 6">{{ option.intr_rate }}</div>
      <!-- <div v-else>-</div> -->
      <!-- <div v-if="!option.length">false</div> -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'DepositOption6',
  props: {
    productId: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      options: [],
    }
  },
  created() {
    this.fetchOptions(this.productId)
  },
  methods: {
    fetchOptions(productId) {
      axios
        .get('http://127.0.0.1:8000/deposits/products-option/')
        .then(response => {
          // Filter options based on productId
          this.options = response.data.filter(option => option.fin_prdt_cd === productId)
        })
        .catch(error => {
          console.error(error)
        })
    },
  },
}
</script>

<style>
</style>
