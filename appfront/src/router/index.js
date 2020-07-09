import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Register from '@/components/Register'
import Login from '@/components/Login'
import login2 from '@/components/login2'
import manage from '@/pages/manage'
import home from '@/pages/home'
import addInterface from '@/pages/addInterface'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/api/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/management',
      component: manage,
      name: 'management',
      children: [
        {
          path: '/management/login',
          name: 'Login',
          component: Login
        },
        {
          path: '/management/login2',
          name: 'Login2',
          component: login2
        },
        {
          path: '/management/home',
          name: 'home',
          component: home
        },
        {
          path: '/management/interface_create',
          name: 'addInterface',
          component: addInterface
        }
      ]

    }

  ]
})
