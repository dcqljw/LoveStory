import {createRouter, createWebHistory} from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    scrollBehavior(to, from, savedPosition) {
        return {top: 0}
    },
    routes: [
        {
            path: '/',
            name: 'home',
            meta: {
                cn_name: "首页",
            },
            component: HomeView,
            children: [
                {
                    path: "",
                    name: 'index',
                    meta: {
                        cn_name: "首页",
                    },
                    component: () => import("@/views/pages/IndexView.vue")
                }, {
                    path: "timeline",
                    name: "timeline",
                    meta: {
                        cn_name: "时间线",
                    },
                    component: () => import("@/views/pages/TimeLineView.vue")
                }, {
                    path: "chat",
                    name: "chat",
                    meta: {
                        cn_name: "聊天",
                    },
                    component: () => import("@/views/pages/ChatView.vue")
                }, {
                    path: 'userinfo',
                    name: 'userinfo',
                    meta: {
                        cn_name: "用户信息",
                    },
                    component: () => import('../views/pages/UserInfoView.vue')
                }, {
                    path: 'setting',
                    name: 'setting',
                    meta: {
                        cn_name: "设置",
                    },
                    component: () => import('../views/pages/UserInfoView.vue')
                }
            ]
        }, {
            path: '/upload',
            name: 'upload',
            component: () => import('../views/pages/UploadView.vue')
        }, {
            path: '/login',
            name: 'login',
            component: () => import('../views/LoginView.vue')
        },
        // {
        //     path: "/:pathMatch(.*)*",
        //     name: "NotFound",
        //     component: () => import('../views/404.vue')
        // }
    ]
})

router.beforeEach((to, from, next) => {
    console.log(to, from, next)
    next()
})

export default router
