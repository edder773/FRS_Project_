<template>
  <div>
    <div v-for="option in options" :key="option.id">
        <p>{{ option.intr_rate }}</p>
        <p>{{ option.intr_rate2 }}</p>
  </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name:'DepositOption',
    props: {
    productId: {
      type: Number,
      required: true,
    },
    data() {
        return {
      options: [],
    }
    },
    created() {
    this.fetchOptions()
  },
  methods: {
    fetchOptions(productId) {
      axios.get('http://127.0.0.1:8000/deposits/products-option/').filter(function(option) {
        return option.fin_prdt_cd === productId
      }).then(response => {
          this.options = response.data
        })
        .catch(error => {
          console.error(error)
        })
    },
  }
}
}
</script>

<style>

</style>