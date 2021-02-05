import Vue from 'vue'
import Router from 'vue-router'

import Auth from '@/components/pages/Auth'
import OneOne from '@/components/pages/OneOne'
import DashBorad from '@/components/pages/DashBorad'


Vue.use(Router)

export default new Router({

  routes: [
    {
      path: '/',
      name: 'OneOne',
      component: OneOne
    },
    {
      path: '/dashboard',
      name: 'DashBorad',
      component: DashBorad
    },
    {
      path: '/auth',
      name: 'Auth',
      component: Auth
    }
  ]
})