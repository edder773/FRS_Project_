<template>
    <div>
      <h1> 간단하게 알아보는 M(money)BTI</h1>
      <div class="game-container">
        <div class="image-container">
          <img :src="currentImage" alt="Image"><br><br>
          <div v-if="currentImageIndex === 0">
            <h4>돈을 차근차근 모아 목돈이 생긴 당신! 그 돈으로...</h4><br>
            <b-button variant="outline-primary" @click="selectImage"> 1. 다시 돈을 더 모으기 위해 저축한다.</b-button><br><br>
            <b-button variant="outline-primary" @click="selectImage"> 2. 그동안 열심히 모았으니 하고싶었던 소비를 한다.</b-button>
          </div>

          <div v-if="currentImageIndex === 1">
            <h4>로또에 당첨된 당신! 그 돈으로..</h4><br>
            <b-button variant="outline-primary" @click="selectImage"> 1. 하던 일을 모두 때려치고 사치를 부리며 산다.</b-button><br><br>
            <b-button variant="outline-primary" @click="selectImage"> 2. 나중 일은 어떻게 될지 모르니 저축한다. </b-button>
          </div>

          <div v-if="currentImageIndex === 2">
            <h4>코인으로 한몫 챙겼다는 지인의 말을 들은 당신은..</h4><br>
            <b-button variant="outline-primary" @click="selectImage"> 1. 인생 한 방, 화성 가보자구! </b-button><br><br>
            <b-button variant="outline-primary" @click="selectImage"> 2. 코인은 무슨 코인이야, 쳐다도 안본다. </b-button>
          </div>

          <div v-if="currentImageIndex === 3">
            <h4>열심히 일한 당신에게 오늘은 월급날! 당신은..</h4><br>
            <b-button variant="outline-primary" @click="selectImage"> 1. YOLO! 하고 싶던 쇼핑을 실컷한다.</b-button><br><br>
            <b-button variant="outline-primary" @click="selectImage"> 2. 50%이상 저축하고 나머지로 소비한다 </b-button>
          </div>

          <div v-if="currentImageIndex === 4">
            <h4>평소 신용카드를 사용하는 당신의 소비 습관은..</h4><br>
            <b-button variant="outline-primary" @click="selectImage"> 1. 한도 최대로! 일단 쓰고본다.</b-button><br><br>
            <b-button variant="outline-primary" @click="selectImage"> 2. 고정적으로 쓰는 돈만 확실하게 신용카드로 관리한다. </b-button>
          </div>

          <div v-if="currentImageIndex === 5">
            <h4>오늘 따라 치킨이 땡기는데..</h4><br>
            <b-button variant="outline-primary" @click="selectImage"> 1. 거기 치킨집이죠? 일단 시키고 본다</b-button><br><br>
            <b-button variant="outline-primary" @click="selectImage"> 2. 하지만 돈이 부족하니 치킨은 사치다. </b-button>
          </div>

          <div v-if="currentImageIndex === 6">
            <h4>취업에 성공한 당신! 친구들이 한톡 쏘라는데...</h4><br>
            <b-button variant="outline-primary" @click="selectImage"> 1. 오늘은 내가 다산다. 고급 식당에 데려간다</b-button><br><br>
            <b-button variant="outline-primary" @click="selectImage"> 2. 야 내가 가진돈이 어딨냐.. 저렴한 식당으로 떼운다 </b-button>
          </div>

          <div v-if="currentImageIndex === 7">
            <h4>돈은 저축, 투자로 분할해야 한다는데...</h4><br>
            <b-button variant="outline-primary" @click="selectImage"> 1. 주식을 산다.</b-button><br><br>
            <b-button variant="outline-primary" @click="selectImage"> 2. 채권을 산다. </b-button>
          </div>

        </div>
      </div>
    </div>
  </template>
  
  <script>
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
        currentImageIndex: 0
      };
    },
    computed: {
      currentImage() {
        return this.images[this.currentImageIndex];
      }
    },
    methods: {
      selectImage() {
        // 이미지 선택 시 다음 이미지로 이동
        this.currentImageIndex++;
        
        // 마지막 이미지일 경우 다시 처음 이미지로 되돌아감
        if (this.currentImageIndex === this.images.length) {
          this.currentImageIndex = 0;
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .game-container {
    display: flex;
    justify-content: center; /* 가운데 정렬 */
    height: 100vh; /* 화면 전체 높이로 설정 */
  }
  
  .image-container {
    width: 48%; /* 좌우 이미지 컨테이너 너비 조정 */
  }
  
  img {
    width: 70%;
    cursor: pointer;
  }
  </style>
  