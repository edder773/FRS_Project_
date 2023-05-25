<template>
  <div id="onetoonecreate-page" class="container">
    <div class="menu-links  text-center">
      <router-link to="/article" class="menu-link">자유게시판</router-link> <div class="menu-link">|</div>
      <router-link to="/question" class="menu-link">자주 묻는 질문</router-link> <div class="menu-link">|</div>
      <router-link to="/onetoone" class="menu-link">1:1 문의</router-link> 
    </div>
    <hr>
    <div style="display: flex; flex-direction: column; align-items: center; margin-top: 50px;">
     <h2 class="section-title">1:1 문의 작성하기</h2>
      <div class="input-box">
        <label for="title" class="label-text">제목:</label>
        <input placeholder="제목을 입력하세요." type="text" id="title" class="create-input" v-model.trim="title">
      </div><br>
      <div class="input-box">
        <label for="content" class="label-text">내용:</label>
        <textarea placeholder="문의 내용을 입력하세요." id="content" class="create-input content-input" v-model.trim="content"></textarea>
      </div><br>
      <div class="button-group">
        <b-button class="create-button" @click="submitForm">등록하기</b-button>
        <b-button class="create-button" href="/onetoone" style="margin-left: 3px;">취소</b-button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapGetters } from 'vuex'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'OnetoOneCreate',
  data() {
    return {
      title: null,
      content: null,
    }
  },
  computed:{
    ...mapGetters(['getUser','getToken'])
  },
  methods: {
    submitForm(){
      this.createArticle()
    },
    createArticle() {
      const title = this.title
      const content = this.content
      const user = this.getUser.username
      const token = this.getToken
      console.log(token)
      if (!title) {
        alert('제목을 입력해주세요')
        return
      } else if (!content){
        alert('내용을 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/articles/`,
        data: {user, title, content},
        headers: {
          Authorization: `Token ${token}`
        }
      })
      .then((res) => {
        console.log(res)
        this.$router.push({name: 'article'})
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
}
</script>

<style scoped>
#onetoonecreate-page{
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
.section-title {
  font-family: 'TheJamsil5Bold';
  font-size: 30px;
  font-weight: bold;
  margin-bottom: 20px;
  text-align: start;
}
.create-input {
  padding: 6px;
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 700px;
}
.content-input{
  height: 300px;
}
.input-box {
    font-family: 'ONE-Mobile-Title';
  display: flex;
  flex-direction: row;
  align-items: start;
}
.label-text {
  font-family: 'ONE-Mobile-Title';
  font-size: 20px;
  margin-right: 10px;
}
.create-button {
  background-color: #383838;
  color: #fff;
  cursor: pointer;
    font-family: 'ONE-Mobile-Title';
      display: flex;
  align-items: center;
  justify-content: center;
}

.create-button:hover {
  background-color: #bdbdbd;
  color: black;
}
.title-box{
    font-family: 'ONE-Mobile-Title';
    font-size: 20px;
}
.content-box{
    font-family: 'ONE-Mobile-Title';
    font-size: 20px;

}

.button-group {
  display: flex;
  justify-content: center;
  width: 100%;
  max-width: 700px;
  margin-top: 20px;
  border: none;
}

</style>
