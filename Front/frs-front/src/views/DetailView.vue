<template>
  <div id="detail-page">
    <h1>Detail</h1>
    <div v-if="!editMode && article">
      <p>작성자 : {{ article.user }}</p>
      <p>글 번호: {{ article?.id }}</p>
      <p>제목: {{ article?.title }}</p>
      <p>내용: {{ article?.content }}</p>
      <p>작성시간: {{ article?.created_at }}</p>
      <p>수정시간: {{ article?.updated_at }}</p>
      <button v-if="IsCurrentUser(article.user)" @click="editMode = true">수정하기</button>
      <button v-if="IsCurrentUser(article.user)" @click="deleteArticle">삭제</button>
    </div>

    <form v-if="editMode" @submit.prevent="updateArticle">
      <label for="title">제목:</label>
      <input type="text" id="title" v-model="article.title">
      <br>
      <label for="content">내용:</label>
      <textarea id="content" cols="30" rows="10" v-model="article.content"></textarea>
      <br>
      <button type="submit">수정 완료</button>
      <button @click="cancelEdit">취소</button>
    </form>
    
    

    <h2 v-if="!editMode">댓글</h2>
    <ul v-if="!editMode && comments.length">
      <li v-for="comment in comments" :key="comment.id">
        <div v-if="!comment.editMode">
          {{ comment?.user }} : {{ comment?.content }}
          <button v-if="IsCurrentUser(comment.user)" @click="editComment(comment)">수정</button>
          <button v-if="IsCurrentUser(comment.user)" @click="deleteComment(comment.id)">삭제</button>
        </div>
        <div v-else>
          <input type="text" v-model="comment.editedContent">
          <button @click="updateComment(comment)">수정 완료</button>
          <button @click="cancelEditComment(comment)">취소</button>
        </div>
      </li>
    </ul>
    <p v-if="!editMode && !comments.length">댓글이 없습니다.</p>

    <form v-if="!editMode" @submit.prevent="createComment">
      <label for="comment">댓글 작성:</label>
      <input type="text" id="comment" v-model="newComment">
      <button type="submit">댓글 작성</button>
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
    }
  },
  created() {
    this.getArticleDetail()
  },
  mounted() {
    this.getArticleComments()
  },
  methods: {
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
  
    updateArticle() {
      const token = this.getToken
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
        .then(() => {
          this.editMode = false; // 수정 완료 후 편집 모드 비활성화
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
      // headers: {
      //   'Content-Type': 'application/json',
      // },
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
<style>
#datail-page{
  margin-top: 80px;
}
</style>