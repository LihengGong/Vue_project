<template>
  <div class="container">
    <h1 class="text-center">Welcome to Chat</h1>
    <div id="auth-container" class="row">
      <div class="col-sm-4 offset-sm-4">
        <ul class="nav nav-tabs nav-justified" id="myTab" role="tablist">
          <li class="nav-item">
            <a class="nav-link active" id="signup-tab" data-toggle="tab" href="#signup" role="tab" aria-controls="signup" aria-selected="true">Sign up</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" id="signin-tab" data-toggle="tab" href="#signin" role="tab" aria-controls="signin" aria-selected="false">Sign In</a>
          </li>
        </ul>
        <div class="tab-content" id="myTabContent">
          <div class="tab-pane fade show active" id="signup" role="tabpanel" aria-labelledby="signin-tab">
            <form @submit.prevent="signUp">
              <div class="form-group">
                <input v-model="email" type="email" class="form-control" id="email" placeholder="Email Address" required/>
              </div>
              <div class="form-row">
                <div class="form-group col-md-6">
                  <input v-model="username" type="text" class="form-control" id="username" placeholder="Username" required/>
                </div>
                <div class="form-group col-md-6">
                  <input v-model="password" type="password" class="form-control" id="password" placeholder="Password" required/>
                </div>
              </div>
              <div class="form-group">
                <div class="form-check">
                  <input class="form-check-input" type="checkbox" id="gridCheck" required>
                  <label class="form-check-label" for="gridCheck">Accept Terms and Conditions</label>
                </div>
              </div>
              <button type="submit" class="btn btn-block btn-primary">Sign up</button>
            </form>
          </div>

          <div class="tab-pane fade" id="signin" role="tabpanel" aria-labelledby="signin-tab">
            <form @submit.prevent="signIn">
              <div class="form-group">
                <input v-model="username" type="text" class="form-control" id="username" placeholder="Username" required>
              </div>
              <div class="form-group">
                <input v-model="password" type="password" class="form-control" id="password" placeholder="Password" required>
              </div>
              <button type="submit" class="btn btn-block btn-primary">Sign in</button>
            </form>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
// const $ = window.jQuery
import axios from 'axios'
const baseURL = 'http://localhost:8000/'
// const Instaxios = require('axios')
// const axios = new Instaxios()

export default {
  // name: 'UserAuth',
  data () {
    return {
      email: '', username: '', password: ''
    }
  },

  methods: {
    signUp () {
      // $.post(baseURL + 'auth/users/create/', this.$data, (data) => {
      //   alert('Your account has been created. You will be assigned in automatically')
      //   this.signIn()
      // })
      //   .fail((response) => {
      //     alert(response.responseText)
      //   })
      axios.post(baseURL + 'auth/users/create/', this.$data)
        .then((response) => {
          console.log('The account has been created. Will sign in now')
          this.signIn()
        })
        .catch((response) => {
          console.log(response.responseText)
        })
    },

    signIn () {
      const credentials = {username: this.username, password: this.password}

      // $.post(baseURL + 'auth/token/create/', credentials, (data) => {
      //   sessionStorage.setItem('authToken', data.token)
      //   sessionStorage.setItem('username', this.username)
      //   this.$router.push('/chats')
      // })
      //   .fail((response) => {
      //     alert(response.responseText)
      //   })
      axios.post(baseURL + 'auth/token/create/', credentials)
        .then((response) => {
          console.log('received response')
          sessionStorage.setItem('authToken', response.token)
          sessionStorage.setItem('username', this.username)
          this.$router.push('/chats')
        })
        .catch((response) => {
          alert(response.responseText)
        })
    }
  }
}
</script>

<style scoped>
  #auth-container {
    margin-top: 50px;
  }

  .tab-content {
    padding-top: 20px;
  }
</style>
