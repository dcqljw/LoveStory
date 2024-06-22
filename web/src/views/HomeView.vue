<script setup lang="ts">
import Header from "@/components/Header.vue";
import {Home, Timeline, Communication, User, SettingOne} from '@icon-park/vue-next'
import {useRouter, useRoute} from "vue-router";
import {onMounted, ref, computed} from "vue";
import http from "@/utils/request";

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


onMounted(() => {
  current_page.value = <string>route.name;

})

</script>

<template>
  <div class="dcq">
    <el-container>
      <el-aside width="14vw" style="padding: 14px 0">

        <div class="nav_left">
          <div class="logo">
            <img src="/images/logo2.svg" alt=""/>
          </div>
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
          <div class="nav_item" @click="toLink('/setting')" :class="{is_active:current_page==='setting'}">
            <setting-one theme="outline" size="30" fill="#000000"/>
            <span class="select">设置</span>
          </div>
        </div>
      </el-aside>
      <el-container>
        <el-header style="height: 70px">
          <Header></Header>
        </el-header>
        <transition name="el-zoom-in-center">
          <el-main style="height: calc(100vh - 70px)">
            <el-scrollbar style="height: 100%">
              <RouterView/>
            </el-scrollbar>
          </el-main>
        </transition>

      </el-container>
    </el-container>
  </div>


  <!--  <div class="nav_bottom">-->
  <!--    <div class="nav_item" @click="toLink('/')" :class="{is_active:current_page==='index'}">-->
  <!--      <home theme="outline" size="30" fill="#000000"/>-->
  <!--    </div>-->
  <!--    <div class="nav_item" @click="toLink('/timeline')" :class="{is_active:current_page==='timeline'}">-->
  <!--      <timeline theme="outline" size="30" fill="#000000"/>-->
  <!--    </div>-->
  <!--    <div class="nav_item" @click="toLink('/chats')" :class="{is_active:current_page==='chat'}">-->
  <!--      <communication theme="outline" size="30" fill="#000000"/>-->
  <!--    </div>-->
  <!--    <div class="nav_item" @click="toLink('/userinfo')" :class="{is_active:current_page==='userinfo'}">-->
  <!--      <user theme="outline" size="30" fill="#000000"/>-->
  <!--    </div>-->
  <!--  </div>-->

</template>
<style scoped>

.dcq {
  width: 90vw;
  margin: 0 auto;
}

.logo {
  text-align: center;
  margin-bottom: 20px;
  font-size: 20px;
}

:deep(main) {
  width: 100%;
}

.container {
  display: flex;
  margin-top: 25px;
}

.nav_card {
  height: 99%;
}

.nav_left {
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
  background: #dedede;
}

.nav_item:hover {
  background: #dedede;
}

.nav_item {
  display: flex;
  margin-bottom: 20px;
  font-size: 20px;
  cursor: pointer;
  border-radius: 50px;
  padding: 10px 20px;
}

.select {
  margin-left: 10px;
}

.main-content {
  margin-left: 20px;
  width: 100%;
}

@media (max-width: 700px) {
  .el-aside {
    display: none;
  }

  .dcq {
    width: 100vw;
  }

  .el-main {
    padding: 0;
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