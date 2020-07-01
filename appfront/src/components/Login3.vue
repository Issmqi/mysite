<template>
  	<div class="login_page fillcontain">
	  	<transition name="form-fade" mode="in-out">
	  		<section class="form_contianer" v-show="showLogin">
		  		<div class="manage_tip">
		  			<p>elm后台管理系统</p>
		  		</div>
		    	<el-form :model="loginForm" :rules="rules" ref="loginForm">
					<el-form-item prop="username">
						<el-input v-model="loginForm.username" placeholder="用户名"><span>dsfsf</span></el-input>
					</el-form-item>
					<el-form-item prop="password">
						<el-input type="password" placeholder="密码" v-model="loginForm.password"></el-input>
					</el-form-item>
					<el-form-item>
				    	<el-button type="primary" @submit.prevent="submit($event)" class="submit_btn">登录</el-button>
				  	</el-form-item>
				</el-form>
	  		</section>
	  	</transition>
  	</div>
</template>

<script>
	import {login, getAdminInfo} from '@/api/getData'
	import {mapActions, mapState} from 'vuex'

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
			if (!this.adminInfo.id) {
    			this.getAdminData()
    		}
		},


		methods:{
    		submit: function(event) {
 
//         	var formData = new FormData(event.target);

			event.preventDefault();
 
        	let formData = new FormData();
 
			//下面是表单绑定的data 数据
			formData.append('name', this.loginForm.name);
			formData.append('password', this.loginForm.password);



        
        	//vue-resource
        	this.$http.post('http://localhost:8000/api/v1/user/auth/login/', formData).then(res => {
              // success callback
			}, 
			err => {
              // error callback
        	});

			let config = {
				headers: {
            		'Content-Type': 'multipart/form-data'
             	}
         	}

        	//axios
        	axios.post('http://localhost:8000/api/v1/user/auth/login/',obj).then(res => {
            // success callback
        	}).catch(err => {
            // error callback
			});
			}
    	}
		// computed: {
		// 	...mapState(['adminInfo']),
		// },
		// methods: {
		// 	...mapActions(['getAdminData']),
		// 	async submitForm(formName) {
		// 		this.$refs[formName].validate(async (valid) => {
		// 			if (valid) {
		// 				const res = await login({user_name: this.loginForm.username, password: this.loginForm.password})
		// 				if (res.status == 1) {
		// 					this.$message({
		//                         type: 'success',
		//                         message: '登录成功'
		//                     });
		// 					this.$router.push('manage')
		// 				}else{
		// 					this.$message({
		//                         type: 'error',
		//                         message: res.message
		//                     });
		// 				}
		// 			} else {
		// 				this.$notify.error({
		// 					title: '错误',
		// 					message: '请输入正确的用户名密码',
		// 					offset: 100
		// 				});
		// 				return false;
		// 			}
		// 		});
		// 	},
		// },
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









