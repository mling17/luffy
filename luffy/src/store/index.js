import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

let store = new Vuex.Store({
	//三大将
	state:{
		userInfo:null
	},
	//修改state的唯一方法是提交mutations
	mutations:{
		getUserInfo(state,token){
			console.log('token---->',token)	//user=res	res=token
			state.userInfo=token;	//userInfo=res
			// console.log('==============>',state.userInfo)
		}
	},
	actions:{
		getUserInfo({commit},token){
			commit('getUserInfo',token);
		}
	}
});
export default store;