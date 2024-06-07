<script setup lang="ts">
import axios from 'axios'


axios.get('http://127.0.0.1:5000/test', {
  headers: {
    authorization: "123123",

  }
},).then(res => {
  console.log(res)
})
</script>
<template>
  <div>
    UserInfo
    <!--    <el-image :src="'http://localhost:8000/api/images/home_data'"/>-->
  </div>
</template>

<style scoped>

</style>