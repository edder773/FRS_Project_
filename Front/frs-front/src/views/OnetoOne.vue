<template>
  <div id="onetoone-page" class="container">
    <div class="menu-links">
      <router-link to="/article" class="menu-link">자유게시판</router-link> <div class="menu-link">|</div>
      <router-link to="/question" class="menu-link">자주 묻는 질문</router-link> <div class="menu-link">|</div>
      <router-link to="/onetoone" class="menu-link">1:1 문의</router-link> 
    </div><hr>
      <b-row>
        <b-col class="d-flex align-items-center mt-3">
          <h2 class="section-title">1:1 문의</h2>
          <b-button style="font-family: 'ONE-Mobile-Title';" class="create-button ms-auto" href="/onetoonecreate">문의하기</b-button>
        </b-col>
      </b-row>
      <br><hr>
      <div class="text-danger" style="font-size:18px;">등록된 1:1 문의가 없습니다.</div>
  </div>
</template>

<script>
export default {
    name:'OnetoOne',
}
</script>

<style scoped>

#onetoone-page{
  margin-bottom: 100px;
}
.menu-links {
  display: flex;
  justify-content: center;
}

.menu-link {
  color: #333;
  font-size: 18px;
  text-decoration: none;
  padding: 10px;
  margin-right: 10px;
  transition: color 0.3s;
}

.menu-link:hover {
  border-bottom-color: #555;
}
.menu-link:hover,
.menu-link.active {
  color: #9bb5d1;
}
.menu-link:hover,
.menu-link.active {
  color: #007bff;
}
.section-title {
  font-family: 'TheJamsil5Bold';
  font-size: 30px;
  font-weight: bold;
  margin-bottom: 20px;
}
.create-button {
  background-color: #383838;
  color: #fff;
  cursor: pointer;
}

.create-button:hover {
  background-color: #bdbdbd;
  color: black;
}


</style>