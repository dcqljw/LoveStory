<script setup lang="ts">
import {userInfoStore} from "@/stores/userInfo";

const userInfo = userInfoStore();
</script>

<template>
  <div>{{ userInfo.userInfo   }}</div>
</template>

<style scoped>

</style>