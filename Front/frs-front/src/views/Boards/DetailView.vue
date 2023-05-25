<template>
  <div id="detail-page" class="container">
    <div class="menu-links  text-center">
      <router-link to="/article" class="menu-link">자유게시판</router-link> <div class="menu-link">|</div>
      <router-link to="/question" class="menu-link">자주 묻는 질문</router-link> <div class="menu-link">|</div>
      <router-link to="/onetoone" class="menu-link">1:1 문의</router-link> 
    </div>
    <hr>
    <div v-if="!editMode && article">
      <b-card>
        <template #header>
          <br>
          <h3 class="mb-0 text-right" style="font-family: 'ONE-Mobile-Title';font-weight: 600;">
            {{ article?.title }}
          </h3><br>
          <p style="font-family: 'ONE-Mobile-Title';text-align: right;font-weight: 200;">{{ article?.user }} </p>
          <p style="font-family: 'ONE-Mobile-Title';text-align: right;font-weight: 200;">{{ new Date(article?.created_at).toLocaleString('ko-KR', { year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit' }) }} </p>
          <div class="button-group">
          <b-button class="create-button" v-if="IsCurrentUser(article.user)" @click="editMode = true">수정하기</b-button>
          <b-button class="create-button" v-if="IsCurrentUser(article.user)" @click="deleteArticle">삭제</b-button>
          </div>
        </template>
        <b-card-text style="font-family: 'ONE-Mobile-Title';font-weight: 100;">{{ article?.content }}</b-card-text>
        <br><br><br><br><br><br><br><br>
        <template #footer>
          <p v-if="!editMode" style="font-family: 'TheJamsil5Bold';">댓글</p>
          <ul v-if="!editMode && comments.length">
            <li v-for="comment in comments" :key="comment.id">
              <div v-if="!comment.editMode">
                <p style="font-family: 'ONE-Mobile-Title';text-align: right;font-weight: 200;"> {{ comment?.user }}</p>
                <p> {{ comment?.content }} </p>
                <p> {{ new Date(comment?.updated_at).toLocaleString('ko-KR', { year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit' }) }} </p>
                <div class="button-group">
                <b-button class="create-button" v-if="IsCurrentUser(comment.user)" @click="editComment(comment)">수정</b-button>
                <b-button class="create-button" v-if="IsCurrentUser(comment.user)" @click="deleteComment(comment.id)">삭제</b-button>
              </div>
            </div>
              <div v-else>
                <p style="font-family: 'ONE-Mobile-Title';text-align: right;font-weight: 200;"> {{ comment?.user }}</p>
                <input type="text" v-model="comment.editedContent">
                <p> {{ new Date(comment?.updated_at).toLocaleString('ko-KR', { year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit' }) }} </p>
                <div class="button-group">
                <b-button class="create-button" @click="updateComment(comment)">수정 완료</b-button>
                <b-button class="create-button" @click="cancelEditComment(comment)">취소</b-button>
              </div>
              </div>
            </li>
          </ul>
          <p v-if="!editMode && !comments.length" style="font-family: 'GangwonEdu_OTFBoldA';">댓글이 없습니다.</p>
          <div v-if="!editMode">
            <b-card :header="isUser">
              <form @submit.prevent="createComment">
                <div class="button-group1">
                <input type="text" id="comment" v-model="newComment" style="width: 500px;">
                <b-button class="create-button" style="cursor: pointer;" @click="submitForm">등록</b-button>
              </div>
              </form>
            </b-card>
          </div>
        </template>
      </b-card>
    </div>
    <form v-if="editMode" @submit.prevent="updateArticle">
      <div>
        <h2>커뮤니티 글 작성하기</h2>
        <b-card>
          <template #header>
            <input placeholder="제목을 입력하세요" style="width: 100%;" type="text" id="title" v-model.trim="article.title"><br>
          </template>
          <textarea placeholder="내용을 입력하세요" style="width: 100%;" id="content" cols="50" rows="30" v-model="article.content"></textarea><br>
          <p style="cursor: pointer;" @click="submitChangeForm">등록</p>
        </b-card>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import { mapGetters } from 'vuex'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailView',
  data() {
    return {
      article: null,
      comments: [],
      newComment: '',
      editMode: false,
      original: null
    }
  },
  computed:{
    ...mapGetters(['getUser','getToken']),
    IsCurrentUser() {
      return(user) => {
        return user === this.getUser.username
      }
    },
    isUser(){
      return this.getUser.username
    }
  },
  created() {
    this.getArticleDetail()
  },
  mounted() {
    this.getArticleComments()
  },
  methods: {
    submitChangeForm(){
      this.updateArticle()
    },
    getArticleDetail() {
      const token = this.getToken
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/`,
        headers: {
          Authorization: `Token ${token}`
        }
      })
      .then((res) => {
        this.article = res.data
        this.original = { ...res.data }
      })
      .catch((error) => {
        console.log(error)
      })
    },
    submitForm(){
      this.createComment()
    },
    // 댓글 가져오기
    getArticleComments() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/comments/`,
      })
      .then((res) => {
        this.comments = res.data.map(comment => ({
          ...comment,
          editMode: false,
          editedContent: comment.content
        }))
      })
      .catch((error) => {
        console.log(error)
      })
    },
    // 댓글 생성 부분
    createComment() {
      if (this.newComment.trim() === '') {
        alert('댓글을 입력하세요.')
        return
      }
      const token = this.getToken
      const commentData = {
        content: this.newComment,
        user: this.getUser.username,
        article : this.$route.params.id
      }
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/comments/`,
        data: commentData,
        headers: {
          Authorization: `Token ${token}`
        }
      })
      .then((res) => {
        console.log(res)
        this.newComment = ''
        this.getArticleComments() // 댓글 목록 다시 불러오기
      })
      .catch((error) => {
        console.log(error)
      })
    },
    // 댓글 삭제 부분
    deleteComment(commentId) {
      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/comments/${commentId}/`,
      })
      .then(() => {
        this.comments = this.comments.filter(comment => comment.id !== commentId)
      })
      .catch((error) => {
        console.log(error)
      })
    },
    // 댓글 편집 부분
    editComment(comment) {
      comment.editMode = true
      comment.editedContent = comment.content
    },
    updateComment(comment) {
      const token = this.getToken
      const updatedCommentData = {
        content: comment.editedContent,
        article : this.$route.params.id
      }
      axios({
        method: 'put',
        url: `${API_URL}/api/v1/comments/${comment.id}/`,
        data: updatedCommentData,
        headers: {
          Authorization: `Token ${token}`
        }
      })
      .then((res) => {
        console.log(res)
        comment.content = comment.editedContent
        comment.editMode = false
      })
      .catch((error) => {
        console.log(error)
      })
    },
    cancelEditComment(comment) {
      comment.editMode = false
    },
    // 게시글 수정 부분
    updateArticle() {
      const token = this.getToken
      if (!this.article.title){
        alert('제목을 입력해주세요')
        return
      }
      else if(!this.article.content){
        alert('내용을 입력해주세요')
        return
      }  
      axios({
        method: 'put',
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/`,
        data: {
          title: this.article.title,
          content: this.article.content,
        },
        headers: {
          Authorization: `Token ${token}`
        }
      })
      .then((res) => {
        this.original = { ...res.data }
        this.editMode = false
      })
      .catch((error) => {
        console.log(error)
      })
    },
    cancelEdit() {
      this.article.title = this.original.title
      this.article.content = this.original.content
      this.editMode = false
    },
    deleteArticle() {
      const articleId = this.article.id
      const apiUrl = `http://127.0.0.1:8000/api/v1/articles/${articleId}`
      fetch(apiUrl, {
        method: 'DELETE',
        })
        .then(response => {
          this.$router.push({ name: 'article' })
          console.log(response)
        })
        .catch(error => {
          console.error(error)
        })
      }
    }
  }
</script>


<style scoped>
#detail-page{
  margin-bottom: 100px;
}
h3{
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'ONE-Mobile-Title';
  font-weight: 500;
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
.button-group {
  display: flex;
  justify-content: center;
  width: 100%;
  max-width: 700px;
  margin-top: 20px;
  border: none;
}
.button-group1 {
  display: flex;
  justify-content: center;
  width: 100%;
  max-width: 700px;
  border: none;
}
</style>