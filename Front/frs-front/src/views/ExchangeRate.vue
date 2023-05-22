<template>
  <div id="exchange-page">
    <div>
      <label for="amount">해외 -> 한국 : </label>
      <input type="number" id="amount" v-model="amount" @input="calculateExchangeRate" />
      <select id="currency" v-model="currency">
        <option v-for="currency in currencies" :key="currency" :value="currency">{{ getCurrencyName(currency) }}</option>
      </select>
      <br>
      <p v-if="result">한국 돈: {{ result }} 원</p>
    </div>
    <br>
    <div>
      <label for="amount">한국 -> 해외 : </label>
      <input type="number" id="amount1" v-model="amount1" @input="calculateExchangeRate1" />
      <select id="currency1" v-model="currency1">
        <option v-for="currency1 in currencies" :key="currency1" :value="currency1">{{ getCurrencyName(currency1) }}</option>
      </select>
      <br>
      <p v-if="result1">{{ getCurrencyName(currency) }}: {{ result1 }} 원</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      amount: 0,
      amount1: 0,
      currency: 'USD',
      currency1: 'USD',
      result: null,
      currencies: ['USD', 'EUR', 'JPY', 'GBP', 'HKD', 'VND'], // 사용할 통화 목록 
      result1: null,
    }
  },
  // computed: {
  //   result() {
  //     return this.result
  //   },
  //   result1() {
  //     return this.result1
  //   },
  // },
  methods: {
    async calculateExchangeRate() {
      try {
        const response = await axios.get('https://api.exchangerate-api.com/v4/latest/KRW')
        const rates = response.data.rates
        const exchangeRate = rates[this.currency]
        this.amount1 = (this.amount / exchangeRate).toFixed(2)
      } catch (error) {
        console.error(error)
      }
    },
    async calculateExchangeRate1() {
      try {
        const response = await axios.get('https://api.exchangerate-api.com/v4/latest/KRW')
        const rates = response.data.rates
        const exchangeRate = rates[this.currency1]
        this.amount = (this.amount1 * exchangeRate).toFixed(2)
      } catch (error) {
        console.error(error)
      }
    },
    getCurrencyName(currency) {
      switch (currency) {
        case 'USD':
          return '달러'
        case 'EUR':
          return '유로'
        case 'JPY':
          return '엔'
        case 'GBP':
          return '파운드'
        case 'HKD':
          return '홍콩달러'
        case 'VND':
          return '동'
        default:
          return currency
      }
    },
  },
}
</script>
<style>

</style>