<script setup lang="ts">
import {RouterView, useRouter} from 'vue-router'
import {onMounted} from "vue";

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
