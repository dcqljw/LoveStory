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
            component: HomeView,
            children: [
                {
                    path: "",
                    name: 'index',
                    component: () => import("@/views/pages/IndexView.vue")
                }, {
                    path: "timeline",
                    name: "timeline",
                    component: () => import("@/views/pages/TimeLineView.vue")
                }, {
                    path: "chat",
                    name: "chat",
                    component: () => import("@/views/pages/ChatView.vue")
                }, {
                    path: '/userinfo',
                    name: 'userinfo',
                    component: () => import('../views/pages/UserInfoView.vue')
                }
            ]
        }, {
            path: '/login',
            name: 'login',
            component: () => import('../views/LoginView.vue')
        }, {
            path: "/:pathMatch(.*)*",
            name: "NotFound",
            component: () => import('../views/404.vue')
        }
    ]
})

router.beforeEach((to, from, next) => {
    console.log(to, from, next)
    next()
})

export default router
