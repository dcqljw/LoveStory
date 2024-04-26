<script setup lang="ts">
import {RouterLink, RouterView, useRouter} from 'vue-router'
import Header from "@/components/Header.vue";
import {onMounted} from "vue";

const router = useRouter();
router.beforeEach((to, from, next) => {
  document.title = `${<string>to.name} - LoveStory`
  next();
})

</script>

<template>
    <RouterView/>
  <el-backtop :right="100" :bottom="100" />
</template>

<style>
</style>
