<script setup lang="ts">
import {RouterView, useRouter} from 'vue-router'
import {onMounted} from "vue";
import {getCookie} from "@/util";
import {userInfoStore} from "@/stores/userInfo";
import {getUserInfoApi} from "@/api/userApi";

const router = useRouter();
router.beforeEach((to, from, next) => {
  document.title = `${<string>to.name} - LoveStory`
  next();
})

const get_user_info = () => {
  const userInfo = userInfoStore();
  let token = getCookie('token');
  console.log(token)
  userInfo.setUserinfo({token: token})
  console.log(userInfo.userInfo)
  getUserInfoApi().then(res => {
    userInfo.setUserinfo({
      uid: res.data.uid,
      username: res.data.username,
      token: token,
      avatar_url: res.data.avatar_url
    })
  })
}

onMounted(() => {
  get_user_info()
})

</script>

<template>
  <RouterView/>
</template>

<style>
</style>
