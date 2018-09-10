import Vue from 'vue'
import Router from 'vue-router'
import notebook from '@/components/notebook'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'notebook',
      component: notebook
    }
  ]
})
