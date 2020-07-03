<template>
  	<div class="login_page fillcontain">
	  	<transition name="form-fade" mode="in-out">
	  		<section class="form_contianer" v-show="showLogin">
		  		<div class="manage_tip">
		  			<p>自动化测试平台</p>
		  		</div>
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
	  		</section>
	  	</transition>
  	</div>
</template>

<script>
	import {login} from '@/api/getData'
	// import {mapState} from 'vuex'
	// import {login, getAdminInfo} from '@/api/getData'
	// import {mapActions, mapState} from 'vuex'

	export default {
	    data(){
			return {
				loginForm: {
					username: '',
					password: '',
				},
				rules: {
					username: [
			            { required: true, message: '请输入用户名', trigger: 'blur' },
			        ],
					password: [
						{ required: true, message: '请输入密码', trigger: 'blur' }
					],
				},
				showLogin: false,
			}
		},
		mounted(){
			this.showLogin = true;
			// if (!this.adminInfo.id) {
    		// 	this.getAdminData()
    		// }
		},
		// computed: {
		// 	...mapState(['adminInfo']),
		// },
		methods: {
			// ...mapActions(['getAdminData']),
			async submitForm(formName) {
				this.$refs[formName].validate(async (valid) => {
					if (valid) {
						// console.log('username',this.loginForm.username)
						console.log(this.loginForm.username)
						console.log(this.loginForm.password)
						let jsonData = {
							'username':this.loginForm.username,
							'password':this.loginForm.password
							};
						// let param=JSON.stringify(jsonData);
						let formdata = new FormData();
						formdata.append('username',this.loginForm.username);
						formdata.append('password',this.loginForm.password);
						console.log(formdata)
						fetch('http://localhost:8000/api/v1/user/auth/login/', {
							method: 'POST',
							headers: {
								'Content-Type': 'application/json'
								// 'Authorization': 'Bearer ' + localStorage.access_token,
							},
							body:JSON.stringify(jsonData)
    						
						}).then(function(res){
							res.json().then(function(obj){
								if(obj.errcode == '200'){
									alert('登录成功')
									_this.$router.push('/')
								}
							})
						})
						
						// const res = await login({'user_name': this.loginForm.username, 'password': this.loginForm.password})

						// if (res.status == 1) {
						// 	this.$message({
		                //         type: 'success',
		                //         message: '登录成功'
		                //     });
						// 	this.$router.push('manage')
						// }else{
						// 	this.$message({
		                //         type: 'error',
		                //         message: res.message
		                //     });
						// }
					} else {
						this.$notify.error({
							title: '错误',
							message: '请输入正确的用户名密码',
							offset: 100
						});
						return false;
					}
				});
			},
		},
		// watch: {
		// 	adminInfo: function (newValue){
		// 		if (newValue.id) {
		// 			this.$message({
        //                 type: 'success',
        //                 message: '检测到您之前登录过，将自动登录'
        //             });
		// 			this.$router.push('manage')
		// 		}
		// 	}
		// }
	}
</script>


// 
// <style lang="less" scoped>
// 	@import '../style/mixin';
// 	.login_page{
// 		background-color: #324057;
// 	}
// 	.manage_tip{
// 		position: absolute;
// 		width: 100%;
// 		top: -100px;
// 		left: 0;
// 		p{
// 			font-size: 34px;
// 			color: #fff;
// 		}
// 	}
// 	.form_contianer{
// 		.wh(320px, 210px);
// 		.ctp(320px, 210px);
// 		padding: 25px;
// 		border-radius: 5px;
// 		text-align: center;
// 		background-color: #fff;
// 		.submit_btn{
// 			width: 100%;
// 			font-size: 16px;
// 		}
// 	}
// 	.tip{
// 		font-size: 12px;
// 		color: red;
// 	}
// 	.form-fade-enter-active, .form-fade-leave-active {
// 	  	transition: all 1s;
// 	}
// 	.form-fade-enter, .form-fade-leave-active {
// 	  	transform: translate3d(0, -50px, 0);
// 	  	opacity: 0;
// 	}
// </style>
