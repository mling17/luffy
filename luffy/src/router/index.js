import Vue from 'vue'
import Router from 'vue-router'

import Course from '@/components/Course/Course'
import LightCourse from '@/components/LightCourse/LightCourse'
import Micro from '@/components/Micro/Micro'
import Home from '@/components/Home/Home'
import CourseDetail from '@/components/Course/CourseDetail'
import Login from '@/components/Login/Login'
import Regist from '@/components/Login/Regist'
import Carte from '@/Carte/Carte'

Vue.use(Router)

//配置路由规则
export default new Router({
	mode:'history',
	linkActiveClass:'is-active',
  routes: [
    {
      path: '/',
      redirect: '/home'
    },
    {
      path: '/home',
      name: 'Home',
      component: Home
    },
    {
      path: '/course',
      name: 'Course',
      component: Course
    },
    {
      path: '/LightCourse',
      name: 'LightCourse',
      component: LightCourse
    },
    {
      path: '/Micro',
      name: 'Micro',
      component: Micro
    },
     {
      path: '/course/detail/:detailId',
      name: 'CourseDetail',
      component: CourseDetail
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/regist',
      name: 'Regist',
      component: Regist
    },
    {
      path:'/purchase/shopping_cart',
      name:'purchase.shop',
      component:Carte
    },
  ]
})
