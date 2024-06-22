import request from "@/utils/request";
import API from "@/api/index";

export const loginApi = (email_address: string, password: string) => {
    return request.post(API.login, {email_address: email_address, password: password})
}

export const getUserInfoApi = () => {
    return request.get(API.userInfo)
}
