import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import home from '../components/home'
import notebook from '../components/notebook'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/notebook/:username',
      name: 'notebook',
      component: notebook
    },
    {
      path: '/home',
      name: 'home',
      component: home
    }
  ]
})

router.beforeEach((to, from, next) => {
  if (sessionStorage.getItem('authToken') !== null || to.path === '/home') {
    console.log('in next()')
    next()
  } else {
    console.log('in next(/home)')
    next('/home')
  }
})

export default router
