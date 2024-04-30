<script setup lang="ts">
import {ref, reactive} from 'vue';
import type {FormInstance, FormRules} from 'element-plus'
import axios from 'axios'

const bg = [
  "/src/assets/images/download/共同协同.png",
  "/src/assets/images/download/发散创意.png",
  "/src/assets/images/download/快速入门.png",
  "/src/assets/images/download/成功秘籍.png",
  "/src/assets/images/download/数据分析.png",
  "/src/assets/images/download/数据报表.png",
]
const ruleFormRef = ref<FormInstance>()

const validateUsername = (rule: any, value: any, callback: any) => {
  if (value === '') {
    callback(new Error('请输入账号'))
  } else {
    callback()
  }
}
const validatePassword = (rule: any, value: any, callback: any) => {
  if (value === '') {
    callback(new Error('请输入密码'))
  } else {
    callback()
  }
}

const ruleForm = reactive({
  username: '',
  password: '',
})

const rules = reactive<FormRules<typeof ruleForm>>({
  username: [{validator: validateUsername, trigger: 'blur'}],
  password: [{validator: validatePassword, trigger: 'blur'}],
})

const submitForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return
  formEl.validate((valid) => {
    console.log(valid)
    if (valid) {
      console.log('submit!')
    } else {
      console.log('error submit!')
      return false
    }
  })
}

// const date = new Date();
// date.setTime(date.getTime() + (7 * 24 * 60 * 60 * 1000));
// const expires = `expires=${date.toUTCString()}`;
// console.log(expires)
// document.cookie = `token=123;${expires};path=/`;

axios.get("/").then((res) => {
  console.log(res)
})

console.log(import.meta.env)

</script>

<template>
  <div class="LoginView">
    <div class="login_left">
      <div class="logo">LS</div>
      <div class="carousel">
        <el-carousel height="600px" motion-blur>
          <el-carousel-item v-for="item in bg" :key="item">
            <el-image :src="item"></el-image>
          </el-carousel-item>
        </el-carousel>
      </div>
    </div>
    <div class="login_right">
      <div class="logo">LS</div>
      <div class="login_form">
        <el-card style="width: 500px">
          <div class="title">Love Story</div>
          <el-form
              ref="ruleFormRef"
              status-icon
              :rules="rules"
              size="large"
              :model="ruleForm"
              label-width="auto"
              style="max-width: 600px">
            <el-form-item prop="username">
              <el-input v-model="ruleForm.username" placeholder="账号"/>
            </el-form-item>
            <el-form-item prop="password">
              <el-input type="password" v-model="ruleForm.password" show-password placeholder="密码"/>
            </el-form-item>
            <el-form-item>
              <el-button style="width: 100%" type="primary" @click="submitForm(ruleFormRef)">登录</el-button>
            </el-form-item>
          </el-form>
        </el-card>

      </div>
    </div>
  </div>

</template>

<style scoped>
.logo {
  position: fixed;
  left: 20px;
  top: 20px;
  border: 4px solid #f19dff;
  border-radius: 10px;
  font-size: 26px;
  padding: 0 9px;
}

.LoginView {
  width: 100%;
  height: 100vh;
  display: flex;
}

.LoginView > div {
  width: 100%;
}

.login_left {
  background: #e6e6fa;
}

.login_right {
  background: white;
}


.carousel, .login_form {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.el-carousel {
  width: 90%;
}

.title {
  text-align: center;
  margin-bottom: 20px;
  font-size: 40px;
}

@media (max-width: 1000px) {
  .login_left {
    display: none;
  }

  .login_right {
    background: #e6e6fa;
  }
}
</style>