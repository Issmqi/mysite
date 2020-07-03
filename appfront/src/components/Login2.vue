<template>
    <div class="login_page ">
	  	<transition name="form-fade" mode="in-out">
	  		<div class="form_contianer" v-show="showLogin">
		  		<div class="manage_tip">
		  			<p>自动化测试平台</p>
		  		</div>
                <!-- <h4 class="">
                    <strong>欢迎登录自动测测试平台</strong>
                </h4> -->
		    	<el-form :model="loginForm" :rules="rules" ref="loginForm">
					<el-form-item prop="username">
						<el-input v-model="loginForm.username" placeholder="用户名"><span>dsfsf</span></el-input>
					</el-form-item>
					<el-form-item prop="password">
						<el-input type="password" placeholder="密码" v-model="loginForm.password"></el-input>
					</el-form-item>
					<el-form-item>
				    	<el-button type="primary" @click="submitForm('loginForm')" class="submit_btn">登录</el-button>
				  	</el-form-item>
				</el-form>
	  		</div>
	  	</transition>
  	</div>
</template>


<script>
import {login} from '@/api/getData'

export default {
    data(){
        return{
            loginForm:{
                username:'',
                password:'',
            },
            rules:{
                username:[
                    {required:true,message:'请输入用户名',trigger:'blur'}
                ],
                password:[
                    {required:true,message:'请输入密码',trigger:'blur'}
                ]
            },
            showLogin: false,
        }
    },
    mounted(){
        this.showLogin=true
    },
    methods:{
        async submitForm(formName) {
            this.$refs[formName].validate(async (valid) => {
                if (valid) {
                    const res=await login({
                        'username':this.loginForm.username,
                        'password':this.loginForm.password
                    })
                    if (res.code==1){
                        this.$message({
                            'type':'success',
                            'message':'登录成功'
                        });
                        this.$router.push('index')
						}else{
							this.$message({
                                type: 'error',
                                title:'',
		                        message: res.message
		                    });
                    }
                }else{
                    this.$notify.error({
							title: '错误',
							message: '请输入正确的用户名密码',
							offset: 100
						});
						return false;
                }

            })
            
        }
    }
}
</script>


<style lang="less" scoped>
	// @import '../style/mixin';
	.login_page{
		background-color: #acb7bf;
	}
	.manage_tip{
		position: absolute;
		width: 100%;
		top: -100px;
		left: 0;
		p{
			font-size: 24px;
			color: #c9b286;
		}
	}
	.form_contianer{
		// .wh(320px, 210px);
        // .ctp(320px, 210px);
        width: 320px;
        height:210h;
        position: absolute;
	    top: 50%;
        left: 50%;
        margin-top: 210px/2;
        margin-left: -320px/2;
		padding: 25px;
		border-radius: 5px;
		text-align: center;
		background-color: #fff;
		.submit_btn{
			width: 100%;
            font-size: 16px;
            background-color: #c9b286;
            border: none;
		}
	}
	.tip{
		font-size: 12px;
		color: red;
	}
	.form-fade-enter-active, .form-fade-leave-active {
	  	transition: all 1s;
	}
	.form-fade-enter, .form-fade-leave-active {
	  	transform: translate3d(0, -50px, 0);
	  	opacity: 0;
	}
</style>
