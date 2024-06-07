<script setup lang="ts">
import {RouterLink, RouterView, useRouter} from 'vue-router'
import {onBeforeMount, onMounted} from "vue";
import {getCookie} from "@/util";
import service from "@/http";
import {userInfoStore} from "@/stores/userInfo";

const useInfo = userInfoStore();

const router = useRouter();
router.beforeEach((to, from, next) => {
  document.title = `${<string>to.name} - LoveStory`
  next();
})



onMounted(() => {

})

</script>

<template>
  <RouterView/>
  <el-backtop :right="100" :bottom="100"/>
</template>

<style>
</style>
