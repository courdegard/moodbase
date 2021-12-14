import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from '../views/LoginPage.vue'
import RegPage from '../views/RegPage.vue'
import UserHomePage from '../views/UserHomePage.vue'
import PublicHomePage from '../views/PublicHomePage.vue'
import PlotPage from '../views/PlotPage.vue'
import WeightPage from '../views/WeightPage.vue'
import ForgotEmailPage from '../views/ForgotEmailPage.vue'
import ResetPasswordPage from '../views/ResetPasswordPage.vue'
import ActivatePage from '../views/ActivatePage.vue'
import GroupPage from '../views/GroupPage.vue'
const routes = [

  {
    path: '/',
    name: 'PublicHomePage',
    props: true,
    component: PublicHomePage
  },
  {
    path: '/login',
    name: 'LoginPage',
    component: LoginPage
  },
  {
    path: '/register',
    name: 'RegPage',
    component: RegPage
  },
  {
    path: '/home',
    name: 'UserHomePage',
    component: UserHomePage
  },
  {
    path: '/plot',
    name: 'PlotPage',
    component: PlotPage
  },
  {
    path: '/allot',
    name: 'WeightPage',
    component: WeightPage
  },
  {
    path: '/forgot',
    name: 'ForgotEmailPage',
    component: ForgotEmailPage
  },
  {
    path: '/reset/:token',
    props: true,
    name: 'ResetPasswordPage',
    component: ResetPasswordPage
  },
  {
    path: '/activate/:token',
    props: true,
    name: 'ActivatePage',
    component: ActivatePage
  },
  {
    path: '/groups',
    name: 'GroupPage',
    component: GroupPage
  }

]

const router = createRouter({
  history: createWebHistory('/'),
  routes
})

export default router
