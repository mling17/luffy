import Vue from 'Vue'
import Vuex from 'Vuex'

Vue.use(Vuex)

let store = new Vuex.Store({
	//三大将
	state:{
		userInfo:{}
	},
	//修改state的唯一方法是提交mutations
	mutations:{
		getUserInfo(state,user){
			state.userInfo=user;
			console.log('==============>',state.userInfo)
		}
	},
	actions:{
		getUserInfo({commit},user){
			commit('getUserInfo',user);
		}
	}
});
export default store;