<template>
  <div>
    <!-- <header class="jumbotron">
      <div class="container">
        <h1 class="display-4">금융 추천 페이지</h1>
        <p class="lead">당신에게 가장 적합한 금융 상품을 추천해드립니다.</p>
      </div>
    </header> -->
    <b-carousel
      id="my-carousel"
      :interval="3000"
      controls
      indicators
      background="#f8f9fa"
      style="margin-bottom: 2rem;"
    >
      <!-- 이미지 슬라이드 아이템들 -->
      <a href="/deposit">
        <b-carousel-slide style="height: 800px;" :img-src="getImagePath('chart.jpg')" alt="Image">
          <div class="title-font">예금, 뭐 하지?</div>
          <div class="mt-4 content-font">금융의 최신 동향을 한눈에!<br>예금 적금 상품 비교를 제공하는 FRS, 지금 확인하세요!</div>
          </b-carousel-slide>
      </a>
      <a href="/exchange">
        <b-carousel-slide style="height: 800px;" :img-src="getImagePath('chart1.jpg')" alt="Image">
          <div class="title-font" style="color: #000;">요즘 환율 얼마야?</div>
          <div class="mt-4 content-font" style="color: #000;">더 나은 금융 선택을 위한 필수 도구!<br> 예금 적금 상품 비교와 실시간 환율 정보 제공하는 FRS, 지금 경험해보세요!</div>
          </b-carousel-slide>
      </a>
      <a href="/recommend">
        <b-carousel-slide style="height: 800px;" :img-src="getImagePath('chart2.jpg')" alt="Image">
          <div class="title-font" style="color: #000;">나에게 맞는 상품은?</div>
          <div class="mt-4 content-font" style="color: #000;">당신의 소비 습관에 맞는 금융 상품을 추천하는 FRS에서<br> 당신의 금융을 관리해보세요!</div>
          </b-carousel-slide>
      </a>
      <a href="/similar">
        <b-carousel-slide style="height: 800px;" :img-src="getImagePath('chartman.jpg')" alt="Image">
          <div class="title-font">다른 사람들은 뭐 했으려나?</div>
          <div class="mt-4 content-font">당신과 비슷한 사람들은 이런 상품을 가입했다!<br> 나이, 자산을 입력하고 상품 가입해보세요!</div>
          </b-carousel-slide>
      </a>
      <a href="/saving">
        <b-carousel-slide style="height: 800px;" :img-src="getImagePath('list.jpg')" alt="Image">
          <div class="title-font" style="color: #4d4d4d;">적금, 뭐 하지?</div>
          <div class="mt-4 content-font" style="color: #4d4d4d;">금융 선택의 완벽한 파트너!<br> 적금 상품 비교해보고 가입하세요. 당신의 금융 결정을 지지합니다!</div>
          </b-carousel-slide>
      </a>
    </b-carousel>
      

  </div>
</template>

<script>
// import Vue from 'vue';
// import KakaoMap from '@/views/KakaoMap.vue';
// import ExchangeRate from '@/views/ExchangeRate.vue'
export default {
  name: 'HomeView',
  // components: {
  //   ExchangeRate,
  //   KakaoMap
    
  //   },
    methods: {
      getImagePath(image) {
        return require(`@/views/Image/${image}`);
      },
      
    },
}
</script>

<style>
.jumbotron {
  background-color: #f8f9fa;
  padding: 2rem;
  margin-bottom: 2rem;
}
#home-page {
  height: 600px;
}

.sr-only {
  display: none;
}

.carousel-caption{
    bottom: 400px !important;
}
.title-font {
  font-family: 'MBC1961GulimM';
  font-size: 60px;
}
.content-font {
  font-family: 'TheJamsil5Bold';
  font-size: 20px;
}
</style>
