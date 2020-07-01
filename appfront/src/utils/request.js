import axios from 'axios'
const service=axios.create({
    baseURL:'http://localhost',
    withCredentials: true,
    timeout:5000
}
)

//添加响应拦截器
service.interceptors.response.use(response=>{
    const res=response.data;
    //如果返回状态码不是200就报错
    if (res.status!=200){
       return Promise.reject(res.message || 'error') 
    }
    return response;   
},error=>{
    return Promise.reject(error.response.data);//返回接口报错信息
})

export default service