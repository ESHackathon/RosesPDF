import Vue from 'vue'
import Router from 'vue-router'

import AppLayout from '../components/layout/AppLayout'
import SystematicReviewProtocol from '../components/forms/SystematicReviewProtocol'

// Error Layouts and Views.
import ErrorLayout from '../components/errors/layout/ErrorLayout'
import NotFound from '../components/errors/views/NotFound'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: AppLayout,
      redirect: '/oops/not-found',
      children: [
        {
          path: '/oops',
          component: ErrorLayout,
          redirect: '/not-found',
          children: [
            {
              path: 'not-found',
              name: 'NotFound',
              component: NotFound
            }
          ]
        },
        {
          path: '',
          name: 'Home',
          component: SystematicReviewProtocol
        }
      ]
    }
  ]
})
