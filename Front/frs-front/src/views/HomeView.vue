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
      interval="3000"
      controls
      indicators
      background="#f8f9fa"
      style="margin-bottom: 2rem;"
    >
      <!-- 이미지 슬라이드 아이템들 -->
      <b-carousel-slide
        v-for="(image, index) in imageList"
        :key="index"
        :img-src="getImagePath(image)"
        alt="Image"
        style="height: 700px;"
      ></b-carousel-slide>
    </b-carousel>
    <footer class="footer mt-auto py-3">
      <div class="text-center">
        <span class="text-muted">© 2023 금융 추천 페이지. All rights reserved.</span>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
  data() {
    return {
      imageList: ['chart.jpg', 'chart1.jpg', 'chart2.jpg', 'chartman.jpg'],
    };
  },
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
  height: 500px;
}
</style>
