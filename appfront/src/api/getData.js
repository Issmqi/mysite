
import fetch from '@/config/fetch'

/***
 * 登录
 */

export const login = data => fetch('http://localhost:8000/api/v1/user/auth/login/', data, 'POST')
