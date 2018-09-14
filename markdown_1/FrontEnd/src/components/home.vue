<template>
  <div class="container">
    <!--<h1 class="text-center">Welcome to Chat</h1>-->
    <div id="auth-container" class="row">
      <div>
        <b-tabs>
          <b-tab title="Sign up" active>
            <b-form @submit.prevent="signUp">
              <b-form-group id="form-group-email"
                            label="Email address:"
                            label-for="email-input">
                <b-form-input v-model="email"
                              type="email"
                              class="form-control"
                              id="email-input"
                              placeholder="Email Address"
                              required/>
              </b-form-group>
              <div class="form-row">
                <b-form-group id="form-group-signup-username"
                              label="user name"
                              label-for="signup-username">
                  <b-form-input v-model="username"
                                type="text"
                                class="form-control"
                                id="signup-username"
                                placeholder="Username"
                                autocomplete="off"
                                required/>
                </b-form-group>
                <b-form-group id="form-group-signup-password"
                              label="password"
                              label-for="enter password">
                  <b-form-input v-model="password"
                                type="password"
                                class="form-control"
                                id="signup-password"
                                placeholder="Password"
                                autocomplete="off"
                                required/>
                </b-form-group>
              </div>
              <b-form-group id="checkbox-form-group">
                <div class="form-check">
                  <b-form-checkbox id="accept-terms-check"
                                   required>
                    Accept Terms and Conditions
                  </b-form-checkbox>
                </div>
              </b-form-group>
              <b-button type="submit"
                        size="lg"
                        variant="primary">Sign up</b-button>
            </b-form>
          </b-tab>
          <b-tab title="Sign in">
            <b-form @submit.prevent="signIn">
              <b-form-group id="form-group-signin-username"
                            label-for="signin-username"
                            label="user name">
                <b-form-input v-model="username"
                              type="text"
                              class="form-control"
                              id="signin-username"
                              placeholder="Username"
                              autocomplete="off"
                              required/>
              </b-form-group>
              <b-form-group id="form-group-signin-password"
                            label="password"
                            label-for="signin-password">
                <b-form-input v-model="password"
                              type="password"
                              class="form-control"
                              id="signin-password"
                              placeholder="Password"
                              autocomplete="off"
                              required/>
              </b-form-group>
              <b-button type="submit"
                        size="lg"
                        variant="primary">
                Sign in
              </b-button>
            </b-form>
          </b-tab>
        </b-tabs>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Vue from 'vue'
import Bootstrap from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import bButton from 'bootstrap-vue/es/components/button/button'
import bTabs from 'bootstrap-vue/es/components/tabs/tabs'
import bTab from 'bootstrap-vue/es/components/tabs/tab'
import bCard from 'bootstrap-vue/es/components/card/card'
import bForm from 'bootstrap-vue/es/components/form/form'
import bFormInput from 'bootstrap-vue/es/components/form-input/form-input'
import bFormGroup from 'bootstrap-vue/es/components/form-group/form-group'
import bFromCheckBox from 'bootstrap-vue/es/components/form-checkbox/form-checkbox'

const baseURL = 'http://localhost:8000/'
Vue.use(Bootstrap)
Vue.component('b-button', bButton)
Vue.component('b-tabs', bTabs)
Vue.component('b-tab', bTab)
Vue.component('b-card', bCard)
Vue.component('b-form', bForm)
Vue.component('b-form-input', bFormInput)
Vue.component('b-form-group', bFormGroup)
Vue.component('b-form-checkbox', bFromCheckBox)

// const $ = window.jQuery

export default {
  name: 'home',
  data () {
    return {
      // Sign up
      email: '',
      username: '',
      password: ''
    }
  },

  methods: {
    signUp () {
      console.log('this.$data=' + this.$data)
      axios.post(baseURL + 'auth/users/create/', this.$data)
        .then((response) => {
          console.log('The account has been created. Will sign in now')
          console.log('response is ' + response)
          this.signIn()
        })
        .catch((response) => {
          console.log('error: ' + response.responseText)
        })
    },

    signIn () {
      const credentials = {username: this.username, password: this.password}

      axios.post(baseURL + 'auth/token/login/', credentials)
        .then((response) => {
          let authToken = JSON.stringify(response.data.auth_token)
          console.log('received response. token is ' + authToken)
          localStorage['token'] = authToken
          sessionStorage.setItem('authToken', authToken)
          sessionStorage.setItem('username', this.username)
          this.$router.push('/notebook/' + this.username)
        })
        .catch((response) => {
          console.log('error: ' + response.responseText)
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
