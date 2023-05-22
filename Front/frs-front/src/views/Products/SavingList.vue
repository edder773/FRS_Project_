<template>
    <div id="saving-page">
      <a href="/deposit">예금비교</a> |
      <a href="/saving">적금비교</a> |
      <h2>정기적금</h2>
      <!-- <li v-for="option in options" :key="option.id">
      <p>이자율 유형: {{ option.intr_rate_type_nm }}</p>
      <p>기본 금리: {{ option.intr_rate }}</p>
      <p>우대 금리: {{ option.intr_rate2 }}</p>
      <p>저축 기간: {{ option.save_trm }}</p>
      <p>저축 유형: {{ option.rsrv_type_nm }}</p>
    </li> -->
      <div class="table-container">
    <table class="main_table content">
      <colgroup>
        <col>
        <col>
        <col>
        <col>
        <col>
      </colgroup>
      <thead class="table-head">
        <th scope="col">번호</th>
        <th scope="col">상품 공시 시작일</th>
        <th scope="col">가입한도</th>
        <th scope="col">금융기관</th>
        <th scope="col">상품</th>
      </thead>
      <tbody class="table-content">
        <tr v-for="product in products" :key="product.id" @click="openModal(product)">
          <td class="table-content">{{ product.id }}</td>
          <td class="table-content">{{ product.dcls_strt_day }}</td>
          <td class="table-content">{{ product.max_limt }}</td>
          <td class="table-content">{{ product.kor_co_nm }}</td>
          <td class="table-content">{{ product.fin_prdt_nm }}</td>
        </tr>
      </tbody>
    </table>
    <div class="modal" v-if="selectedProduct" @click.self="closeModal">
      <!-- <div class="modal-header">

      </div> -->
      <div class="modal-content">
        <div class="modal-header">
          <button style="float: right;" @click="closeModal">
            <span aria-hidden="true" >X</span>
          </button>
        </div>
        <h2>{{selectedProduct.fin_prdt_nm}}</h2>
        <h3>{{selectedProduct.kor_co_nm}}</h3><hr>
        <KakaoMap/>
        <p>가입 가능 유형:{{ selectedProduct.join_member }}</p>
        <p> {{ selectedProduct.etc_note }}</p>
        <!-- <button @click="closeModal">닫기</button> -->
      </div>
    </div>
  </div>
        <!-- <ul>
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
      </ul> -->

    </div>
  </template>
  
  <script>
  import axios from 'axios'
  import KakaoMap from '@/components/KakaoMap.vue'

  export default {
    name: 'SavingList',
    components: {
    KakaoMap
    },
    data() {
      return {
        products: [],
        options: [],
      selectedProduct: null
      }
    },
    created() {
      this.fetchProducts()
      this.fetchOptions()
    },
    methods: {
      fetchProducts() {
        axios.get('http://127.0.0.1:8000/deposits/savings/') 
          .then(response => {
            this.products = response.data
          })
          .catch(error => {
            console.error(error)
          })
      },
      openModal(product) {
      this.selectedProduct = product
    },
    fetchOptions() {
      axios.get('http://127.0.0.1:8000/deposits/savings-option/')
        .then(response => {
          this.options = response.data
        })
        .catch(error => {
          console.error(error)
        })
    },
    closeModal() {
      this.selectedProduct = null
    },
    }
  }
  </script>
  <style>
  .table-container{
    display: flex;
    justify-content: center;
    font-family: "Spoqa Han Sans", Malgun Gothic, "맑은 고딕", dotum, "돋움", -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
    font-size: 16px;
    line-height: 1.5;
    color: #555;
  }
  .table-content{
    padding-top: 10px;
    padding-bottom: 10px;
  }
  .table-head{
    font-size: 20px;
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
  
  .modal-content {
    background-color: #fff;
    padding: 20px;
    border-radius: 4px;
    width: 600px;
    overflow-y: auto; /* 내용이 모달 크기를 초과할 경우 스크롤 생성 */
    /* height: 600px; */
    
  }
  .modal-header {
    display: flex;
    justify-content: flex-end;
    /* align-items: flex-start; */
  }
  
  
  .close:hover {
    opacity: 1;
    color: #000;
  }


  #saving-page{
  margin-top: 80px;
}
  </style>