import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Register from '@/components/Register'
import Test from '@/components/Test'
import Login from '@/components/Login'
import login2 from '@/components/login2'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/test',
      name: 'Test',
      component: Test
    },
    {
      path: '/api/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/management/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/management/login2',
      name: 'Login2',
      component: login2
    }
  ]
})
