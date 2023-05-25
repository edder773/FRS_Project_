<template>
  <div id="create-page">
    <div style="display: flex; flex-direction: column; align-items: center; margin-top: 50px;">
      <h2>커뮤니티 글 작성하기</h2>
      <b-card style="width: 90%" header-tag="header" border-variant="secondary" header-border-variant="secondary">
        <template #header>
          <input placeholder="제목을 입력하세요" style="width: 100%;" type="text" id="title" v-model.trim="title"><br>
        </template>
        <textarea placeholder="내용을 입력하세요" style="width: 100%;" id="content" cols="50" rows="30" v-model="content"></textarea><br>
        <p style="cursor: pointer;" @click="submitForm">등록</p>
      </b-card>
    </div>
  </div>
</template>


<script>
import axios from 'axios'
import { mapGetters } from 'vuex'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CreateView',
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
        alert('제목 입력해주세요')
        return
      } else if (!content){
        alert('내용 입력해주세요')
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

<style>

</style>