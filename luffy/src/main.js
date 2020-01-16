import Vue from 'vue'
import App from './App'
import router from './router'
// store的引入
import store from '@/store'
// elementUI 导入
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
// 调用插件
Vue.use(ElementUI);
import '../static/global/global.css'
// import '../static/global/gt.js'
// 导入axios

import * as api from './restful/api'
Vue.prototype.$http = api;



// 全局守卫
router.beforeEach((to, from, next) => {
if (localStorage.getItem('token')) {
	// 用户登录过
	let token =localStorage.getItem('token');
	console.log('7777777777777',token)
	store.dispatch('getUserInfo',token);
}
  // ...
  next();
})


Vue.config.productionTip = false
/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  router,
  components: { App },
  template: '<App/>'
})

