import Vue from 'vue'
import Router from 'vue-router'

import Auth from '@/components/pages/Auth'
import Registration from '@/components/pages/Registration'
import OneOne from '@/components/pages/OneOne'
import DashBorad from '@/components/pages/DashBorad'
import Top from '@/components/pages/Top'
import Lp from '@/components/pages/Lp'

Vue.use(Router)

export default new Router({

  routes: [
    {
      path: '/OneOne',
      name: 'OneOne',
      component: OneOne
    },
    {
      path: '/',
      name: 'Top',
      component: Top
    },
    {
      path: '/dashboard',
      name: 'DashBorad',
      component: DashBorad
    },
    {
      path: '/registration',
      name: 'Registration',
      component: Registration
    },
    {
      path: '/auth',
      name: 'Auth',
      component: Auth
    },
    {
      path: '/lp',
      name: 'Lp',
      component: Lp
    }
  ]
})