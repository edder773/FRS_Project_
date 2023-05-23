<template>
<div>
  <h1>Home</h1>

<header class="jumbotron">
      <div class="container">
        <h1 class="display-4">금융 추천 페이지</h1>
        <p class="lead">당신에게 가장 적합한 금융 상품을 추천해드립니다.</p>
      </div>
    </header>

    <section class="container">
      <div class="row">
        <div class="col-md-4">
          <div class="card">
            <img src="'@/views/Homeimage/computer.jpg'" class="card-img-top" alt="Image 1">
            <div class="card-body">
              <h5 class="card-title">추천 상품 1</h5>
              <p class="card-text">이 상품은 ...</p>
              <a href="#" class="btn btn-primary">상세 정보</a>
            </div>
          </div>
        </div>
        <div class="col-md-4">
          <div class="card">
            <img src="image2.jpg" class="card-img-top" alt="Image 2">
            <div class="card-body">
              <h5 class="card-title">추천 상품 2</h5>
              <p class="card-text">이 상품은 ...</p>
              <a href="#" class="btn btn-primary">상세 정보</a>
            </div>
          </div>
        </div>
        <div class="col-md-4">
          <div class="card">
            <img src="image3.jpg" class="card-img-top" alt="Image 3">
            <div class="card-body">
              <h5 class="card-title">추천 상품 3</h5>
              <p class="card-text">이 상품은 ...</p>
              <a href="#" class="btn btn-primary">상세 정보</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <footer class="footer mt-auto py-3">
      <div class="container text-center">
        <span class="text-muted">© 2023 금융 추천 페이지. All rights reserved.</span>
      </div>
    </footer>
  </div>
</template>
<script>
export default {
  name: 'HomeView',
}
</script>

<style>
.jumbotron {
  background-color: #f8f9fa;
  padding: 2rem;
  margin-bottom: 2rem;
}

.card {
  margin-bottom: 2rem;
}
</style>
