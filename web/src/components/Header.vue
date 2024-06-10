<script setup lang="ts">
import {HamburgerButton} from "@icon-park/vue-next";
import {onMounted, ref} from "vue";
import {useRouter} from "vue-router"

const router = useRouter();
const current_name = ref<string>("首页")

router.beforeEach((to, from, next) => {
  current_name.value = to.meta.cn_name
  next()
})

onMounted(() => {
  console.log("Header")
})

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
          <el-avatar style="outline: none"
                     src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"/>
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item>退出登录</el-dropdown-item>
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