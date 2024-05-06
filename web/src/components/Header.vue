<script setup lang="ts">
import {ref} from 'vue';
import {Search} from '@element-plus/icons-vue'

const input = ref("")
</script>

<template>
  <div class="nav-bg">
    <div class="nav-bar">
      <div class="logo">
        <div>L S</div>
        <div>LoveStory</div>
      </div>
      <div class="search">
        <el-input v-model="input" size="large" :suffix-icon="Search" placeholder="输入查询内容"/>
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
.logo > div:nth-child(1) {
  font-size: 28px;
  font-family: "JetBrains Mono";
}

.logo > div:nth-child(2) {
  font-size: 16px;
  font-family: "MV Boli";
  color: #852fff;
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