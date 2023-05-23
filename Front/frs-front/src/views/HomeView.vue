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
      <b-carousel-slide style="height: 500px;" :img-src="getImagePath('chart.jpg')" alt="Image">
        <h2>예금, 적금. 뭐 하지?</h2>
        <p>금융의 최신 동향을 한눈에! 예금 적금 상품 비교를 제공하는 FRS, 지금 확인하세요!</p>
        </b-carousel-slide>
      <b-carousel-slide style="height: 500px;" :img-src="getImagePath('chart1.jpg')" alt="Image">
        <h2>요즘 환율 얼마야?</h2>
        <p>더 나은 금융 선택을 위한 필수 도구! 예금 적금 상품 비교와 업데이트된 환율 정보를 제공하는 FRS, 지금 경험해보세요!</p>
        </b-carousel-slide>
      <b-carousel-slide style="height: 500px;" :img-src="getImagePath('chart2.jpg')" alt="Image">
        <h2>나에게 맞는 상품은?</h2>
        <p>당신의 소비 습관에 맞는 금융 상품을 추천하는 FRS에서 당신의 금융을 관리해보세요!</p>
        </b-carousel-slide>
      <b-carousel-slide style="height: 500px;" :img-src="getImagePath('chartman.jpg')" alt="Image">
        <h2>다른 사람들은 뭐 했으려나?</h2>
        <p>당신과 비슷한 사람들은 이런 상품을 가입했다! 나이, 자산을 입력하고 상품 가입해보세요!</p>
        </b-carousel-slide>
      <b-carousel-slide style="height: 500px;" :img-src="getImagePath('list.jpg')" alt="Image">
        <h2>예금, 적금. 뭐 하지?</h2>
        </b-carousel-slide>
    </b-carousel>
    <footer class="footer mt-auto py-3">
      <div class="text-center">
        <span class="text-muted">© 2023 FRS 금융 추천 페이지. All rights reserved.</span>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
  data() {
    return {
      imageTitles: [
        '예금, 적금. 뭐 하지?', 
        '요즘 환율 얼마야?',
        '나에게 맞는 상품은?', 
        '다른 사람들은 뭐 했으려나?',
       ],
      imageContents: [
        '금융의 최신 동향을 한눈에! 예금 적금 상품 비교를 제공하는 FRS, 지금 확인하세요!',
        '더 나은 금융 선택을 위한 필수 도구! 예금 적금 상품 비교와 업데이트된 환율 정보를 제공하는 FRS, 지금 경험해보세요!', 
        '당신의 소비 습관에 맞는 금융 상품을 추천하는 FRS에서 당신의 금융을 관리해보세요!', 
        '당신과 비슷한 사람들은 이런 상품을 가입했다! 나이, 자산을 입력하고 상품 가입해보세요!',
       ],
    };
  },
  methods: {
    getImagePath(image) {
      return require(`@/views/Image/${image}`);
    },
    getImageTitle(image) {
      const index = this.imageList.indexOf(image);
      return this.imageTitles[index];
    },
    getImageContent(image) {
      const index = this.imageList.indexOf(image);
      return this.imageContents[index];
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
  height: 500px;
}

.sr-only {
  display: none;
}
/* b-carousel-slide {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  text-align: center;
} */
.carousel-caption{
    bottom: 200px;
}
</style>
