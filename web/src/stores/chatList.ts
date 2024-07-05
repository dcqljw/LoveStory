import {defineStore} from "pinia";

interface ChatList {
    uid: string
    username: string
    token: string
    avatar_url: string
}

export const chatListStore = defineStore("chatListStore", {
    state: () => {
        return {
            chatList: [
                {
                    id: "doubao",
                    name: "豆包",
                    icon: "https://lf-flow-web-cdn.doubao.com/obj/flow-doubao/doubao/web/logo-icon.png",
                }, {
                    id: "yiyan",
                    name: "文心一言",
                    icon: "https://nlp-eb.cdn.bcebos.com/static/eb/asset/logo.8a6b508d.png"
                }, {
                    id: "tongyi",
                    name: "通义千问",
                    icon: "https://img.alicdn.com/imgextra/i4/O1CN01FOwagl1XBpyVA2QVy_!!6000000002886-2-tps-512-512.png"
                }
            ]
        }
    },
    actions: {}
})