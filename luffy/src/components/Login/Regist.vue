<template>
    <div class="box">
        <img src="http://pic.netbian.com/uploads/allimg/180826/113958-153525479855be.jpg" alt="">
        <div class="login">
            <div class="login-title">
                <img src="https://hcdn1.luffycity.com/static/frontend/activity/head-logo_1564141048.3435316.svg" alt="">
                <p>帮助有志向的年轻人通过努力学习获得体面的工作和生活!</p>
            </div>
            <div class="login_box">
                <div class="title">
                    <span>新用户注册</span>
                    <!-- <span>短信登录</span> -->
                </div>
                <div class="inp">
                    <input v-model = 'username' type="text"  placeholder="用户名 / 手机号码" class="user">
                    <input v-model = 'password' type="password" name="" class="user pwd" placeholder="密码">
                    <input v-model = 're_password' type="password" name="" class="pwd" placeholder="确认密码">
                    <div id="geetest"></div>
                    <button class="login_btn" @click='resgistHandler'>注册</button>
                    <p class="go_login" >已有账号 <span @click='loginHandler'>立即登陆</span></p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'Login',
  data(){
    return{
        username:'',
        password:'',
        re_password:''
    }
  },
  methods:{
    //
    resgistHandler(){
        if (this.password===this.re_password){
            //发送注册请求
            let params={
                username:this.username,
                pwd:this.password
            }
            this.$http.userRegister(params)
            .then(res=>{
                console.log(res)
                if(res.code===0){

                    this.$router.push({
                        name:'Home'
                    })
                }else{
                    this.$message(res.error)
                }
            })
            .catch(err=>{
                console.log(err)
            })
        }else{
            this.$message('两次密码输入不一致');
            this.password='';
            this.re_password='';
        }
    },
    //跳转到用户登陆页面
    loginHandler(){
        this.$router.push({
            name:'Login'
        })
     }
    }
}
</script>

<style lang="css" scoped>
.box{
    width: 100%;
    position: relative;

}
.box img{
    width: 100%;
}
.box .login {
    position: absolute;
    width: 500px;
    height: 400px;
    top: 50%;
    left: 50%;
    margin-left: -250px;
    margin-top: -300px;
}
.login .login-title{
     width: 100%;
    text-align: center;
}
.login-title img{
    width: 190px;
    height: auto;
}
.login-title p{
    font-family: PingFangSC-Regular;
    font-size: 18px;
    color: #fff;
    letter-spacing: .29px;
    padding-top: 10px;
    padding-bottom: 50px;
}
.login_box{
    width: 400px;
    height: auto;
    background: #fff;
    box-shadow: 0 2px 4px 0 rgba(0,0,0,.5);
    border-radius: 4px;
    margin: 0 auto;
    padding-bottom: 40px;
}
.login_box .title{
    font-size: 20px;
    color: #9b9b9b;
    letter-spacing: .32px;
    border-bottom: 1px solid #e6e6e6;
     display: flex;
        justify-content: space-around;
        padding: 50px 60px 0 60px;
        margin-bottom: 20px;
        cursor: pointer;
}
.login_box .title span:nth-of-type(1){
    color: #4a4a4a;
        /*border-bottom: 2px solid #84cc39;*/
}

.inp{
    width: 350px;
    margin: 0 auto;
}
.inp input{
    border: 0;
    outline: 0;
    width: 100%;
    height: 45px;
    border-radius: 4px;
    border: 1px solid #d9d9d9;
    text-indent: 20px;
    font-size: 14px;
    background: #fff !important;
}
.inp input.user{
    margin-bottom: 16px;
}
.inp .rember{
     display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    margin-top: 10px;
}
.inp .rember p:first-of-type{
    font-size: 12px;
    color: #4a4a4a;
    letter-spacing: .19px;
    margin-left: 22px;
    display: -ms-flexbox;
    display: flex;
    -ms-flex-align: center;
    align-items: center;
    /*position: relative;*/
}
.inp .rember p:nth-of-type(2){
    font-size: 14px;
    color: #9b9b9b;
    letter-spacing: .19px;
    cursor: pointer;
}

.inp .rember input{
    outline: 0;
    width: 30px;
    height: 45px;
    border-radius: 4px;
    border: 1px solid #d9d9d9;
    text-indent: 20px;
    font-size: 14px;
    background: #fff !important;
}

.inp .rember p span{
    display: inline-block;
  font-size: 12px;
  width: 100px;
  /*position: absolute;*/
/*left: 20px;*/

}
#geetest{
    margin-top: 20px;
}
.login_btn{
     width: 100%;
    height: 45px;
    background: #84cc39;
    border-radius: 5px;
    font-size: 16px;
    color: #fff;
    letter-spacing: .26px;
    margin-top: 30px;
}
.inp .go_login{
    text-align: center;
    font-size: 14px;
    color: #9b9b9b;
    letter-spacing: .26px;
    padding-top: 20px;
}
.inp .go_login span{
    color: #84cc39;
    cursor: pointer;
}
</style>
