<script setup lang="ts">
import Header from "@/components/Header.vue";
import {Home, Timeline, Communication, User} from '@icon-park/vue-next'

import {useRouter, useRoute} from "vue-router";
import {onMounted, ref, computed} from "vue";

const router = useRouter();
const route = useRoute();

const current_page = ref('index')

const toLink = (path: string) => {
  router.push(path);
}
router.beforeEach((to, from, next) => {
  current_page.value = <string>to.name
  next();
})
// let cRoute = computed(() => {
//   return router.currentRoute.value.fullPath;
// });
onMounted(() => {
  current_page.value = <string>route.name;
})

</script>

<template>
  <Header></Header>
  <main>
    <div class="container">
      <div class="nav_left">
        <div class="nav_item" @click="toLink('/')" :class="{is_active:current_page==='index'}">
          <home theme="outline" size="30" fill="#000000"/>
          <span class="select">首页</span>
        </div>
        <div class="nav_item" @click="toLink('/timeline')" :class="{is_active:current_page==='timeline'}">
          <timeline theme="outline" size="30" fill="#000000"/>
          <span class="select">时间线</span>
        </div>
        <div class="nav_item" @click="toLink('/chat')" :class="{is_active:current_page==='chat'}">
          <communication theme="outline" size="30" fill="#000000"/>
          <span class="select">聊天</span>
        </div>
      </div>
      <div class="main-content">
        <!--        <el-scrollbar max-height="100vh">-->
        <RouterView/>
        <!--        </el-scrollbar>-->
      </div>
    </div>
    <div class="nav_bottom">
      <div class="nav_item" @click="toLink('/')" :class="{is_active:current_page==='index'}">
        <home theme="outline" size="30" fill="#000000"/>
      </div>
      <div class="nav_item" @click="toLink('/timeline')" :class="{is_active:current_page==='timeline'}">
        <timeline theme="outline" size="30" fill="#000000"/>
      </div>
      <div class="nav_item" @click="toLink('/chats')" :class="{is_active:current_page==='chat'}">
        <communication theme="outline" size="30" fill="#000000"/>
      </div>
      <div class="nav_item" @click="toLink('/userinfo')" :class="{is_active:current_page==='userinfo'}">
        <user theme="outline" size="30" fill="#000000"/>
      </div>
    </div>

  </main>
</template>
<style scoped>
.container {
  display: flex;
  margin-top: 25px;
}

.nav_left {
  width: 300px;
}

.nav_bottom {
  display: flex;
  justify-content: space-around;
  position: fixed;
  bottom: 0;
  width: 100%;
  left: 0;
  background-color: #ffffff;
  align-items: center;
  height: 70px;
}

.is_active {
  background: #f7f7f7;
}

.nav_item:hover {
  background: #f7f7f7;
}

.nav_item {
  display: flex;
  margin-bottom: 20px;
  font-size: 20px;
  cursor: pointer;
  border-radius: 50px;
  padding: 10px 20px;
  width: 200px;
}

.select {
  margin-left: 10px;
}

.main-content {
  margin-left: 20px;
  width: 100%;
}

@media (max-width: 700px) {
  .nav_left {
    display: none;
  }


  .nav_item {
    margin: 0;
    padding: 5px 15px;
    width: 30px;
  }

  .container {
    padding-bottom: 70px;
  }

  .main-content {
    margin: 0;
  }
}

@media (min-width: 700px) {
  .nav_bottom {
    display: none;
  }
}

</style>