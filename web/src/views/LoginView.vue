<script setup lang="ts">
import {ref, reactive, watch, onMounted} from 'vue';
import type {FormInstance, FormRules} from 'element-plus'
import {ElMessage} from "element-plus";
import {useRouter, useRoute} from "vue-router";
import {Github} from "@icon-park/vue-next";
import {loginApi} from '@/api/userApi';

import service from "@/utils/request";
import {getCookie, setCookie} from "@/util";
import {userInfoStore} from "@/stores/userInfo";
import axios from "axios";
import http from "@/utils/request";

const userInfo = userInfoStore();

const login_loading = ref(false);
const router = useRouter();
const route = useRoute();
const ruleFormRef = ref<FormInstance>()
const tips_is_active = reactive<{ email_address: boolean, password: boolean }>({
  email_address: false,
  password: false,
})

const validateUsername = (rule: any, value: any, callback: any) => {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (regex.test(value)) {
    callback()
  } else {
    callback(new Error('请输入正确的邮箱账号'))
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
  email_address: '',
  password: '',
})

const rules = reactive<FormRules<typeof ruleForm>>({
  email_address: [{validator: validateUsername, trigger: 'blur'}],
  password: [{validator: validatePassword, trigger: 'blur'}],
})

const login = async () => {
  login_loading.value = true
  await loginApi(ruleForm.email_address, ruleForm.password).then(res => {
    // await service.post('/api/user/login', ruleForm,).then(res => {
    console.log(res)
    if (res.data.code !== "2000") {
      ElMessage.error(res.data.msg)
    } else {
      console.log(res.data)
      setCookie("token", res.data.data.token)
      userInfo.setUserinfo(res.data.data)
      console.log(userInfo.userInfo)
      router.push('/')
    }
  }).catch(e => {
    ElMessage.error("系统异常")
  })
  login_loading.value = false
}

const submitForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return
  formEl.validate((valid) => {
    console.log(valid)
    if (valid) {
      console.log('submit!')
      login()
    } else {
      console.log('error submit!')
      return false
    }
  })
}

const tips_active_focus = (select: string) => {
  tips_is_active[select] = true
}

const tips_active_blur = (select: string) => {
  if (ruleForm.email_address === "") {
    tips_is_active.email_address = false
  }
  if (ruleForm.password === "") {
    tips_is_active.password = false
  }

}


console.log(import.meta.env)

const github_login = () => {
  const url = "https://github.com/login/oauth/authorize?client_id=Ov23li5BelebTemvlHgp&redirect_uri=http://127.0.0.1:5173/login"
  window.location.href = url
}
const github_callback = async (code: any) => {
  await http.get(`/user/auth/github/callback?code=${code}`).then(res => {
    if (res.data.code !== "2000") {
      ElMessage.error(res.data.msg)
    } else {
      console.log(res.data)
      setCookie("token", res.data.data.token)
      userInfo.setUserinfo(res.data.data)
      console.log(userInfo.userInfo)
      router.push('/')
    }
  })
}

onMounted(() => {
  const code = route.query.code
  if (code) {
    github_callback(code)
  }
})

</script>

<template>
  <div class="LoginView" v-loading.fullscreen.lock="login_loading">
    <img class="bg" src="/src/assets/bg.svg"/>
    <div class="login_form">
      <div class="login_card">
        <div class="title">
          <el-image style="height: 40px" src="/images/logo2.svg"/>
        </div>
        <el-form
            ref="ruleFormRef"
            status-icon
            :rules="rules"
            size="large"
            :model="ruleForm">
          <el-form-item prop="email_address">
            <label class="tips" :class="{'tips_active':tips_is_active['email_address']}">邮&nbsp;箱</label>
            <el-input size="large" @focus="tips_active_focus('email_address')" class="email_input"
                      v-model="ruleForm.email_address"
                      placeholder=""
                      @blur="tips_active_blur('email_address')"/>
          </el-form-item>
          <el-form-item prop="password">
            <label class="tips" :class="{'tips_active':tips_is_active['password']}">密&nbsp;码</label>
            <el-input size="large" @focus="tips_active_focus('password')" class="password_input" type="password"
                      v-model="ruleForm.password" show-password
                      placeholder=""
                      @blur="tips_active_blur('password')"/>
          </el-form-item>
          <el-form-item>
            <el-button style="width: 100%" type="primary" @click="submitForm(ruleFormRef)">登录</el-button>
          </el-form-item>
        </el-form>
        <el-divider>其他登录方式</el-divider>
        <div class="oauth">
          <div @click="github_login">
            <!--            <a href="https://github.com/login/oauth/authorize?client_id=Ov23li5BelebTemvlHgp&redirect_uri=http://127.0.0.1:8000/api/user/auth/github/callback">-->
            <github theme="outline" size="32" fill="#000000"/>
            <!--            </a>-->
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<style scoped>
.login_form {
  display: flex;
  flex-direction: column;
  width: 20%;
  position: fixed;
}

.bg {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.login_card {
  background: white;
  padding: 44px 24px;
  border-radius: 40px;
}

.LoginView {
  width: 100%;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}


.title {
  text-align: center;
  margin-bottom: 20px;
  font-size: 40px;
}

.tips {
  position: relative;
  bottom: -28px;
  z-index: 2;
  left: 10px;
  background: white;
  font-size: 20px;
  padding: 0 4px;
  line-height: 20px;
  animation: tips_close_an 0.15s ease-in-out forwards;
}

.tips_active {
  bottom: -9px;
  animation: tips_an 0.15s ease-in-out forwards;
}

@keyframes tips_close_an {
  from {
    bottom: -9px;
    font-size: 16px;
  }
  to {
    bottom: -28px;
  }
}

@keyframes tips_an {
  from {
    bottom: -28px;
  }
  to {
    bottom: -9px;
    font-size: 16px;
  }
}


.email_input:active::after {
  top: -13px
}

@media (max-width: 700px) {
  .login_form {
    width: 90%;
  }
}

.oauth {
  display: flex;
  justify-content: center;
}
</style>