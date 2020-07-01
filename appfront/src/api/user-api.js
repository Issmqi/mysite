import request from "src/utils/request.js";

export function register(data){
    return request.post('api/v1/user/register/',data);
}