<script setup lang="ts">
import {HamburgerButton} from "@icon-park/vue-next";
import {onMounted, ref} from "vue";
import {useRouter} from "vue-router"
import {userInfoStore} from "@/stores/userInfo";

const router = useRouter();
const userInfo = userInfoStore();
const current_name = ref<string>("首页")

router.beforeEach((to, from, next) => {
  current_name.value = to.meta.cn_name
  next()
})

onMounted(() => {
  console.log("Header")
  console.log(userInfo.userInfo.avatar_url)
})
const logout = () => {
  document.cookie = "token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
  userInfo.setUserinfo({})
  window.location.reload()
}

</script>

<template>
  <div class="nav-bg">
    <div class="nav-bar">
      <div class="current_title">
        <!--        <hamburger-button theme="outline" size="32" fill="#8d8d8d"/>-->
        <div>{{ current_name }}</div>
      </div>
      <div class="user">
        <el-dropdown>
          <el-avatar style="outline: none;background: none"
                     :src="userInfo.userInfo.avatar_url"/>
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item @click="logout">退出登录</el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
      </div>
    </div>
  </div>
</template>

<style scoped>

.current_title {
  display: flex;
  align-items: center;
  font-size: 24px;
  justify-content: space-between;
  width: 100px;
}


.nav-bar, .nav-bg {
  height: 100%;
}

.nav-bg {
  background: #fff;
}

.nav-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
}


:deep(.el-input__wrapper) {
  width: 400px;
  border-radius: 20px;
}

.user {
  cursor: pointer;
}

@media (max-width: 700px) {
  .search {
    display: none;
  }

  .nav-bg {
    padding: 0 10px;
  }
}

</style>