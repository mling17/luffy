//导入axios
import Axios from 'axios'
//挂载axios
Axios.defaults.baseURL='http://127.0.0.1:8888/'
Axios.interceptors.request.use(function (config) {
    // 在发送请求之前做些什么
    if (localStorage.getItem('token')) {
    	// Axios.defaults.headers.common['Authorization'] = localStorage.getItem('access_token');
    	config.headers.AUTHORIZATION = localStorage.getItem('token')
    }
    return config;
  }, function (error) {
    // 对请求错误做些什么
    return Promise.reject(error);
  });
//分类列表API
export const categoryList=()=> {
	// body...
	return Axios.get('api/course/category/').then((res)=>{
		return res.data
	})
}
// 获取所有的分类信息
export const allCategoryList=(categoryId)=>{
	return Axios.get(`api/course/list/?categoryId=${categoryId}`).then((res)=>{
		return res.data
	})
}


// 课程详情页
export const courseDetail=(courseId)=>{
	return Axios.get(`api/course/detail/${courseId}`).then((res)=>{
		return res.data
	})
}

// 获取课程章节
export const courseChapter=(courseId)=>{
	return Axios.get(`api/course/chapter/${courseId}`).then((res)=>{
		return res.data
	})
}

//登陆接口
export const userLogin=(params)=>{
	// return Axios.post('https://api.growingio.com/v2/a6067de96ab40585/web/action?stm=1579057651181',params).then((res)=>{
	return Axios.post('api/login/',params).then((res)=>{
		return res.data
	})
}

//注册接口
export const userRegister=(params)=>{
	return Axios.post('api/register/',params).then((res)=>{
		return res.data
	})
}
//加入购物车
export const shopCart=(params)=>{
	return Axios.post('api/shop/shopping_car/',params).then(res=>res.data)
}

//购物车数据
export const shopCartList=()=>{
	return Axios.get('api/shop/shopping_car/').then(res=>res.data)
}
