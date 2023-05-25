<template>
  <div class="exchange-page">
    <div id="exchange-page" class="container">
    <div style="height: 800px;" >
    <!-- <h1> 환율 비교 </h1><br> -->
    <div>
      <select id="currency" class="exchange-select" v-model="currency">
        <option v-for="currency in currencies" :key="currency" :value="currency">{{ getCurrencyName(currency) }}</option>
      </select>
      <br><br>
      <b-input-group size="sm" :prepend="getCurrencySymbol(currency)" :append="getCurrencyName(currency)">
        <b-form-input type="number" id="amount" v-model="amount" @input="calculateExchangeRate" />
      </b-input-group>

    </div>
    <br>
    <div>
      <b-input-group size="sm" prepend="₩" append="원">
        <b-form-input type="number" id="amount1" v-model="amount1" @input="calculateExchangeRate1" />
      </b-input-group>

    </div>
      <br>
  </div>
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
      currencies: ['USD', 'EUR', 'JPY', 'GBP', 'HKD', 'VND', 'CAD', 'AUD', 'CNY', 'NZD', 'SEK', 'NOK', 'CHF', 'ZAR', 'BRL', 'INR', 'RUB', 'TRY', 'KRW'], // 사용할 통화 목록 
      result1: null,
      currencySymbols: {
        USD: '$',
        EUR: '€',
        JPY: '¥',
        GBP: '£',
        HKD: 'HK$',
        VND: '₫',
        CAD: 'CA$',
        AUD: 'A$',
        CNY: '¥',
        NZD: 'NZ$',
        SEK: 'kr',
        NOK: 'kr',
        CHF: 'CHF',
        ZAR: 'R',
        BRL: 'R$',
        INR: '₹',
        RUB: '₽',
        TRY: '₺',
        KRW: '₩',
      },
    }
  },
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
        case 'CAD':
          return '캐나다달러'
        case 'AUD':
          return '호주달러'
        case 'CNY':
          return '위안'
        case 'NZD':
          return '뉴질랜드달러'
        case 'SEK':
          return '크로나'
        case 'NOK':
          return '크로네'
        case 'CHF':
          return '프랑'
        case 'ZAR':
          return '랜드'
        case 'BRL':
          return '레알'
        case 'INR':
          return '루피'
        case 'RUB':
          return '루블'
        case 'TRY':
          return '리라'
        case 'KRW':
          return '원'
        default:
          return currency
      }
    },
    getCurrencySymbol(currency) {
  if (Object.prototype.hasOwnProperty.call(this.currencySymbols, currency)) {
    return this.currencySymbols[currency];
  }
  return '';
},

  },
}
</script>

<style scoped>
.exchange-page{
  margin-top: 150px;
}
.exchange-select {
  padding: 6px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #f7f7f7;
  width: 100%;
  flex-direction: row;
}
</style>
