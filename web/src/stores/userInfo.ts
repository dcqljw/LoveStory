import {defineStore} from "pinia";

interface UserInfo {
    uid: string
    username: string
    token: string
    avatar_url: string
}

export const userInfoStore = defineStore("userInfo", {
    state: () => {
        return {userInfo: <UserInfo>{}}
    },
    actions: {
        setUserinfo(state: any) {
            this.userInfo = state
        }
    }
})