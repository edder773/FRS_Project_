<template>
  <div>
    <div style="text-align: center; margin-top: 2%; margin-bottom: 2%">
     <h1 style="margin: 0;">간단하게 알아보는 M(money)BTI</h1>
    </div>
    <div class="container">
      <div v-if="isMain" class="container">
        <img src="@/views/Image/main.jpg" alt="Image" ><br><br>
          <h4> 나의 소비 유형은?</h4>
          <b-button pill variant="success" @click="gameStart">시작하기!</b-button>
      </div>
    </div>
      
    <div v-if="isStart" class="game-container">
      <div class="image-container">
        <img :src="currentImage" alt="Image"><br><br>
        <div v-if="currentImageIndex === 0">
          <h4>돈을 차근차근 모아 목돈이 생긴 당신! 그 돈으로...</h4><br>
          <b-button variant="outline-primary" @click="selectImage"> 1. 그동안 열심히 모았으니 하고싶었던 소비를 한다. </b-button><br><br>
          <b-button variant="outline-primary" @click="nextStep"> 2. 다시 돈을 더 모으기 위해 저축한다. </b-button>
        </div>

        <div v-if="currentImageIndex === 1">
          <h4>로또에 당첨된 당신! 그 돈으로..</h4><br>
          <b-button variant="outline-primary" @click="selectImage"> 1. 하던 일을 모두 때려치고 사치를 부리며 산다.</b-button><br><br>
          <b-button variant="outline-primary" @click="nextStep"> 2. 나중 일은 어떻게 될지 모르니 저축한다. </b-button>
        </div>

        <div v-if="currentImageIndex === 2">
          <h4>코인으로 한몫 챙겼다는 지인의 말을 들은 당신은..</h4><br>
          <b-button variant="outline-primary" @click="selectImage"> 1. 인생 한 방, 화성 가보자구! </b-button><br><br>
          <b-button variant="outline-primary" @click="nextStep"> 2. 코인은 무슨 코인이야, 쳐다도 안본다. </b-button>
        </div>

        <div v-if="currentImageIndex === 3">
          <h4>열심히 일한 당신에게 오늘은 월급날! 당신은..</h4><br>
          <b-button variant="outline-primary" @click="selectImage"> 1. YOLO! 하고 싶던 쇼핑을 실컷한다.</b-button><br><br>
          <b-button variant="outline-primary" @click="nextStep"> 2. 50%이상 저축하고 나머지로 소비한다 </b-button>
        </div>

        <div v-if="currentImageIndex === 4">
          <h4>평소 신용카드를 사용하는 당신의 소비 습관은..</h4><br>
          <b-button variant="outline-primary" @click="selectImage"> 1. 한도 최대로! 일단 쓰고본다.</b-button><br><br>
          <b-button variant="outline-primary" @click="nextStep"> 2. 고정적으로 쓰는 돈만 확실하게 신용카드로 관리한다. </b-button>
        </div>

        <div v-if="currentImageIndex === 5">
          <h4>오늘 따라 치킨이 땡기는데..</h4><br>
          <b-button variant="outline-primary" @click="selectImage"> 1. 거기 치킨집이죠? 일단 시키고 본다</b-button><br><br>
          <b-button variant="outline-primary" @click="nextStep"> 2. 하지만 돈이 부족하니 치킨은 사치다. </b-button>
        </div>

        <div v-if="currentImageIndex === 6">
          <h4>취업에 성공한 당신! 친구들이 한톡 쏘라는데...</h4><br>
          <b-button variant="outline-primary" @click="selectImage"> 1. 오늘은 내가 다산다. 고급 식당에 데려간다</b-button><br><br>
          <b-button variant="outline-primary" @click="nextStep"> 2. 야 내가 가진돈이 어딨냐.. 저렴한 식당으로 떼운다 </b-button>
        </div>

        <div v-if="currentImageIndex === 7">
          <h4>돈은 저축, 투자로 분할해야 한다는데...</h4><br>
          <b-button variant="outline-primary" @click="selectedFinish"> 1. 주식을 산다.</b-button><br><br>
          <b-button variant="outline-primary" @click="selectFinish"> 2. 채권을 산다. </b-button>
       </div>
      </div>
    </div>

    <div v-if="currentImageIndex === 8" class="centered-container">
      <div v-if="loadingData">
        <h3>당신에게 맞는 상품을 찾는 중...</h3>
        <b-spinner style="width: 10em; height: 10rem;"></b-spinner>
      </div>
      <div v-if="!loadingData">
        <div v-if="this.score === 0">
          <img src="@/views/Image/s0.jpg" alt="Image" ><br><br>
          <h3>당신은 미래의 가치보단 지금 당장이 중요한 사람!</h3>
          <div v-for="product in products" :key="product.id">
            <b-card header="당신에게 맞는 상품은!" header-tag="header" :title="product.kor_co_nm">
              <b-card-text>{{ product.fin_prdt_nm }}</b-card-text>
              <b-button variant="primary" @click="showModal">상품 자세히 보기기</b-button>
              <b-modal size="lg" v-model="modalVisible" title="상품 상세 정보">
                <b-card bg-variant="light" header="상품 정보" class="text-center">
                  <b-card-text>
                    <p>만기시 이자 정보</p>
                    <p>{{product.mtrt_int}}</p>
                    <br>
                    <p>조건에 따른 우대 정보</p>
                    <p>{{product.spcl_cnd}}</p>
                    <br>
                    <p>거래 실적 인정 기간</p>
                    <p>{{product.etc_note}}</p>
                    <b-button variant="success" @click="checkProduct(product)">
                      {{ checkIn(product) ? '해지하기' : '가입하기' }}</b-button>
                    </b-card-text>
                  </b-card>
                </b-modal>
              </b-card>
            </div>
        </div>

        <div v-if="this.score === 1">
          <img src="@/views/Image/s1.jpg" alt="Image" ><br><br>
          <h3>당신은 마음 속 한편으론 절약을 꿈꾸는 사람!</h3>
          <div v-for="product in products" :key="product.id">
            <b-card header="당신에게 맞는 상품은!" header-tag="header" :title="product.kor_co_nm">
              <b-card-text>{{ product.fin_prdt_nm }}</b-card-text>
              <b-button variant="primary" @click="showModal">상품 자세히 보기기</b-button>
              <b-modal size="lg" v-model="modalVisible" title="상품 상세 정보">
                <b-card bg-variant="light" header="상품 정보" class="text-center">
                  <b-card-text>
                    <p>만기시 이자 정보</p>
                    <p>{{product.mtrt_int}}</p>
                    <br>
                    <p>조건에 따른 우대 정보</p>
                    <p>{{product.spcl_cnd}}</p>
                    <br>
                    <p>거래 실적 인정 기간</p>
                    <p>{{product.etc_note}}</p>
                    <b-button variant="success" @click="checkProduct(product)">
                      {{ checkIn(product) ? '해지하기' : '가입하기' }}</b-button>
                    </b-card-text>
                  </b-card>
                </b-modal>
              </b-card>
            </div>
        </div>

        <div v-if="this.score === 2">
          <img src="@/views/Image/s2.jpg" alt="Image" ><br><br>
          <h3>당신은 절약을 시도하지만 주위 환경이 돈을 쓰게 만들고 있군요!</h3>
          <div v-for="product in products" :key="product.id">
            <b-card header="당신에게 맞는 상품은!" header-tag="header" :title="product.kor_co_nm">
              <b-card-text>{{ product.fin_prdt_nm }}</b-card-text>
              <b-button variant="primary" @click="showModal">상품 자세히 보기기</b-button>
              <b-modal size="lg" v-model="modalVisible" title="상품 상세 정보">
                <b-card bg-variant="light" header="상품 정보" class="text-center">
                  <b-card-text>
                    <p>만기시 이자 정보</p>
                    <p>{{product.mtrt_int}}</p>
                    <br>
                    <p>조건에 따른 우대 정보</p>
                    <p>{{product.spcl_cnd}}</p>
                    <br>
                    <p>거래 실적 인정 기간</p>
                    <p>{{product.etc_note}}</p>
                    <b-button variant="success" @click="checkProduct(product)">
                      {{ checkIn(product) ? '해지하기' : '가입하기' }}</b-button>
                    </b-card-text>
                  </b-card>
                </b-modal>
              </b-card>
            </div>
        </div>

        <div v-if="this.score === 3">
          <img src="@/views/Image/s3.jpg" alt="Image" ><br><br>
          <h3>당신은 절약의 중요성을 알지만 정신차리면 돈을 탕진 하는 타입!</h3>
          <div v-for="product in products" :key="product.id">
            <b-card header="당신에게 맞는 상품은!" header-tag="header" :title="product.kor_co_nm">
              <b-card-text>{{ product.fin_prdt_nm }}</b-card-text>
              <b-button variant="primary" @click="showModal">상품 자세히 보기기</b-button>
              <b-modal size="lg" v-model="modalVisible" title="상품 상세 정보">
                <b-card bg-variant="light" header="상품 정보" class="text-center">
                  <b-card-text>
                    <p>만기시 이자 정보</p>
                    <p>{{product.mtrt_int}}</p>
                    <br>
                    <p>조건에 따른 우대 정보</p>
                    <p>{{product.spcl_cnd}}</p>
                    <br>
                    <p>거래 실적 인정 기간</p>
                    <p>{{product.etc_note}}</p>
                    <b-button variant="success" @click="checkProduct(product)">
                      {{ checkIn(product) ? '해지하기' : '가입하기' }}</b-button>
                    </b-card-text>
                  </b-card>
                </b-modal>
              </b-card>
            </div>
        </div>

        <div v-if="this.score === 4">
          <img src="@/views/Image/s4.jpg" alt="Image" ><br><br>
          <h3>어느정도 절약을 하는 당신! 그러나 가끔 사고 싶은게 있으면 참지 못하고 긁는 타입!</h3>
          <div v-for="product in products" :key="product.id">
            <b-card header="당신에게 맞는 상품은!" header-tag="header" :title="product.kor_co_nm">
              <b-card-text>{{ product.fin_prdt_nm }}</b-card-text>
              <b-button variant="primary" @click="showModal">상품 자세히 보기기</b-button>
              <b-modal size="lg" v-model="modalVisible" title="상품 상세 정보">
                <b-card bg-variant="light" header="상품 정보" class="text-center">
                  <b-card-text>
                    <p>만기시 이자 정보</p>
                    <p>{{product.mtrt_int}}</p>
                    <br>
                    <p>조건에 따른 우대 정보</p>
                    <p>{{product.spcl_cnd}}</p>
                    <br>
                    <p>거래 실적 인정 기간</p>
                    <p>{{product.etc_note}}</p>
                    <b-button variant="success" @click="checkProduct(product)">
                      {{ checkIn(product) ? '해지하기' : '가입하기' }}</b-button>
                    </b-card-text>
                  </b-card>
                </b-modal>
              </b-card>
            </div>
        </div>

        <div v-if="this.score === 5">
          <img src="@/views/Image/s5.jpg" alt="Image" ><br><br>
          <h3>사고 싶은걸 참으면서 절약을 할줄 아는 당신!</h3>
          <div v-for="product in products" :key="product.id">
            <b-card header="당신에게 맞는 상품은!" header-tag="header" :title="product.kor_co_nm">
              <b-card-text>{{ product.fin_prdt_nm }}</b-card-text>
              <b-button variant="primary" @click="showModal">상품 자세히 보기기</b-button>
              <b-modal size="lg" v-model="modalVisible" title="상품 상세 정보">
                <b-card bg-variant="light" header="상품 정보" class="text-center">
                  <b-card-text>
                    <p>만기시 이자 정보</p>
                    <p>{{product.mtrt_int}}</p>
                    <br>
                    <p>조건에 따른 우대 정보</p>
                    <p>{{product.spcl_cnd}}</p>
                    <br>
                    <p>거래 실적 인정 기간</p>
                    <p>{{product.etc_note}}</p>
                    <b-button variant="success" @click="checkProduct(product)">
                      {{ checkIn(product) ? '해지하기' : '가입하기' }}</b-button>
                    </b-card-text>
                  </b-card>
                </b-modal>
              </b-card>
            </div>
        </div>

        <div v-if="this.score === 6">
          <img src="@/views/Image/s6.jpg" alt="Image" ><br><br>
          <h3>근검절약하는 당신! 미래에 대한 저축이 확실한 사람!</h3>
          <div v-for="product in products" :key="product.id">
            <b-card header="당신에게 맞는 상품은!" header-tag="header" :title="product.kor_co_nm">
              <b-card-text>{{ product.fin_prdt_nm }}</b-card-text>
              <b-button variant="primary" @click="showModal">상품 자세히 보기기</b-button>
              <b-modal size="lg" v-model="modalVisible" title="상품 상세 정보">
                <b-card bg-variant="light" header="상품 정보" class="text-center">
                  <b-card-text>
                    <p>만기시 이자 정보</p>
                    <p>{{product.mtrt_int}}</p>
                    <br>
                    <p>조건에 따른 우대 정보</p>
                    <p>{{product.spcl_cnd}}</p>
                    <br>
                    <p>거래 실적 인정 기간</p>
                    <p>{{product.etc_note}}</p>
                    <b-button variant="success" @click="checkProduct(product)">
                      {{ checkIn(product) ? '해지하기' : '가입하기' }}</b-button>
                    </b-card-text>
                  </b-card>
                </b-modal>
              </b-card>
            </div>
        </div>
        <div v-if="this.score >= 7">
          <img src="@/views/Image/s7.jpg" alt="Image" ><br><br>
          <h3>절약왕! 돈 저축하는걸 사랑하는 사람!</h3>
          <div v-for="product in products" :key="product.id">
            <b-card header="당신에게 맞는 상품은!" header-tag="header" :title="product.kor_co_nm">
              <b-card-text>{{ product.fin_prdt_nm }}</b-card-text>
              <b-button variant="primary" @click="showModal">상품 자세히 보기기</b-button>
              <b-modal size="lg" v-model="modalVisible" title="상품 상세 정보">
                <b-card bg-variant="light" header="상품 정보" class="text-center">
                  <b-card-text>
                    <p>만기시 이자 정보</p>
                    <p>{{product.mtrt_int}}</p>
                    <br>
                    <p>조건에 따른 우대 정보</p>
                    <p>{{product.spcl_cnd}}</p>
                    <br>
                    <p>거래 실적 인정 기간</p>
                    <p>{{product.etc_note}}</p>
                    <b-button variant="success" @click="checkProduct(product)">
                      {{ checkIn(product) ? '해지하기' : '가입하기' }}</b-button>
                    </b-card-text>
                  </b-card>
                </b-modal>
              </b-card>
            </div>
        </div>
        <br>
        <div v-if="!isMain" class="container">
          <b-button pill variant="danger" @click="restartGame">다시하기</b-button>
        </div>
      </div>
    </div>
  </div>
</template>
  
<script>
import axios from 'axios' 
import { mapGetters } from 'vuex'
export default {
  data() {
    return {
      images: [
      require('@/views/Image/1.png'),
      require('@/views/Image/2.jpg'),
      require('@/views/Image/3.jpg'),
      require('@/views/Image/4.jpg'),
      require('@/views/Image/5.jpg'),
      require('@/views/Image/6.png'),
      require('@/views/Image/7.jpg'),
      require('@/views/Image/8.jpg'),
      ],
      currentImageIndex: 0,
      isStart: false,
      isMain: true,
      loadingData: true,
      score: 0,
      options: [],
      products: [],
      modalVisible: false
    }
  },
  created(){
    this.getArticles()
  },
  computed: {
    ...mapGetters(['getUser', 'getToken']),
    currentImage() {
      return this.images[this.currentImageIndex]
    },
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
    }
  },

  methods: {
    // 로그인 여부
    getArticles() {
      if (this.isLogin) {
        this.$store.dispatch('getArticles')
      } else {
        alert('로그인이 필요한 페이지입니다...')
        this.$router.push({ name: 'home' })
      }
    },
//모달표시
    showModal() {
    this.modalVisible = true
  },
// 이미지 선택할 시 다음 스탭(스코어 증가)
    nextStep(){
      this.selectImage()
      this.score++
    },
// 이미지 선택할 시 다음 스탭(스코어 미증가)
    selectImage() {
      this.currentImageIndex++
      if (this.currentImageIndex === this.images.length) {
        this.isStart = false
        this.loadFinish()
      }
    },
// 게임 시작 버튼
    gameStart(){
      this.isStart = true
      this.isMain = false
    },
// 로딩중 끝
    loadFinish(){
      setTimeout(() => {
        this.loadingData = false
      }, 4000)
    },
// 추천을 위한 알고리즘
    fetchProductOption() { // if문을 통해 짝수 홀수에 따라 예금 or 적금 테이블에서 가져옴
      if (this.score == 0 || this.score == 2 || this.score == 4 || this.score == 6){
        axios.get('http://127.0.0.1:8000/deposits/products-option/')
        .then(response => {
          const options = response.data
          let filteredOptions = null
        if (this.score == 0){
          filteredOptions = options.filter(option => option.save_trm === 6)
        }
        else if (this.score == 2){
          filteredOptions = options.filter(option => option.save_trm === 12)
        }
        else if (this.score == 4){
          filteredOptions = options.filter(option => option.save_trm === 24)
        }
        else if (this.score == 6){
          filteredOptions = options.filter(option => option.save_trm === 36)
        }
    
        let maxIntrRate2Option = null
        let maxIntrRate2 = -Infinity
        for (const option of filteredOptions) {
          if (option.intr_rate2 > maxIntrRate2) {
            maxIntrRate2 = option.intr_rate2
            maxIntrRate2Option = option
          }
        }
        this.options = [maxIntrRate2Option]
        })
        .catch(error => {
          console.error(error)
        })
      } 
      else{
        axios.get('http://127.0.0.1:8000/deposits/savings-option/')
        .then(response => {
        const options = response.data
        let filteredOptions = null
        if (this.score == 1){
          filteredOptions = options.filter(option => option.save_trm === 6)
        }
        else if (this.score == 3){
          filteredOptions = options.filter(option => option.save_trm === 12)
        }
        else if (this.score == 5){
          filteredOptions = options.filter(option => option.save_trm === 24)
        }
        else if (this.score == 7 || this.score == 8){
          filteredOptions = options.filter(option => option.save_trm === 36)
        }

        let maxIntrRate2Option = null
        let maxIntrRate2 = -Infinity
        for (const option of filteredOptions) {
          if (option.intr_rate2 > maxIntrRate2) {
            maxIntrRate2 = option.intr_rate2
            maxIntrRate2Option = option
          }
        }
        this.options = [maxIntrRate2Option]
        })
        .catch(error => {
          console.error(error)
        })
      }
    },
    fetchProduct() {
      if(!(this.score % 2)){
        axios.get('http://127.0.0.1:8000/deposits/products/')
        .then(response => {
          const products = response.data
          const matchedProducts = products.filter(product => product.id === this.options[0].fin_prdt_cd);
          this.products = matchedProducts
        })
        .catch(error => {
          console.error(error)
        })
      }
      else{
        axios.get('http://127.0.0.1:8000/deposits/savings/')
        .then(response => {
          const products = response.data
          const matchedProducts = products.filter(product => product.id === this.options[0].fin_prdt_cd);
          this.products = matchedProducts
        })
        .catch(error => {
          console.error(error)
        })
      }
    },
// 마지막 최종 선택 1
  async selectFinish() {
    this.nextStep()
    try {
      await this.fetchProductOption()
      await this.fetchProduct()
    } catch (error) {
      console.error(error)
    }
  },
// 마지막 최종 선택 2
  async selectedFinish() {
    this.selectImage()
    try {
      await this.fetchProductOption()
      await this.fetchProduct()
    } catch (error) {
      console.error(error)
    }
  },
// 다시 시작하기 기능
  restartGame() {
    this.currentImageIndex = 0
    this.isStart = false
    this.isMain = true
    this.loadingData = true
    this.score = 0
    this.options = []
    this.products = []
    },
// 가입하기 기능
    checkProduct(product) {
  const user = this.getUser
  console.log(user.financial_products)
  const payload = {
    user_id: user.pk,  // 'user_id' 키에 사용자 ID 값을 전달
    product_id: product.id  // 'product_id' 키에 상품 ID 값을 전달
  }
  this.$store.dispatch('addProduct', payload)
},
// 가입여부 확인 기능
checkIn(product){
      return this.getUser.financial_products.includes(product.id)
    },
  },
}
</script>
  
<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.game-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.image-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.centered-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  /* justify-content: center; */
  text-align: center;
}


.image-container {
  width: 48%;
}

img {
  width: 70%;
  cursor: pointer;
}

.centered-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 100px;
  height: 100vh;
}

</style>
