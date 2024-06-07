import axios from "axios";
import {userInfoStore} from "@/stores/userInfo";
import {ElMessage} from "element-plus";
import router from "@/router";

const userInfo = userInfoStore();
const service = axios.create({})

service.defaults.withCredentials = true

if (import.meta.env.MODE === 'production') {
    service.defaults.baseURL = "http://dcqljw.com"
} else {
    service.defaults.baseURL = "http://localhost:8000"
}
// 请求拦截设置token
service.interceptors.request.use(
    config => {
        const token = userInfo.userInfo.token
        token && (config.headers.Authorization = token)
        return config
    },
    error => {
        return Promise.reject(error);
    }
)
service.interceptors.response.use(
    response => {
        if (response.status === 200) {
            if (response.data.code === "4001") {
                console.log(response.data.msg)
                router.push("/login")
                return Promise.resolve(response)
            }
            return Promise.resolve(response)
        } else {
            return Promise.reject(response);
        }
    },
    error => {
        console.log(error)
        return Promise.reject(error);
    }
)

export default service