<script setup lang="ts">
import {useRouter, useRoute} from "vue-router";
import {Plus} from "@element-plus/icons-vue";
import {chatListStore} from "@/stores/chatList";

const router = useRouter();
const route = useRoute();
const chatList = chatListStore();
console.log(chatList.chatList)
if (!route.params.chat_type) {
  console.log("没有选择")
  router.push("/chat/豆包")
}
</script>

<template>
  <div class="common-layout">
    <el-container>
      <el-aside>
        <div class="select_model">
          <div class="select_item">
            <el-button style="width: 100%" size="large" type="primary" plain>
              <el-icon :size="20">
                <Plus/>
              </el-icon>
              &nbsp;新对话
            </el-button>
          </div>
          <div v-for="item in chatList.chatList" :key="item.name" class="select_item"
               @click="router.push('/chat/' + item.id)">
            <el-image style="width: 30px;" :src="item.icon"></el-image>
            <span>{{ item.name }}</span>
          </div>
        </div>
        <div class="login">
          <el-button size="large" type="primary" round style="width: 100%">登录</el-button>
        </div>
      </el-aside>
      <el-main>
        <router-view/>
      </el-main>
    </el-container>
    <div class="chat"></div>
  </div>
</template>

<style scoped>
.select_item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 30px;
  cursor: pointer;
}

.el-aside {
  display: flex;
  flex-direction: column;
  background: #f3f4f6;
  height: 100vh;
  justify-content: space-between;
}

.login {
  margin-left: 14px;
  margin-right: 14px;
  margin-bottom: 24px;
}
</style>