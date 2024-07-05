<script setup lang="ts">
import 'mavon-editor/dist/css/index.css'
import axios from "axios"
import {ref, render} from "vue";
import {marked} from "marked";

const chat_data = ref("")
const input_data = ref()
const md_value = ref()
const markdownContent = ref("")
const source_text = ref("")

const fromData = {
  data: input_data.value
}
const chatV2 = async () => {
  fromData["data"] = input_data.value
  source_text.value = ""
  markdownContent.value = ""
  let response = await fetch("http://127.0.0.1:8000/chat",
      {
        method: "post",
        responseType: "stream",
        body: JSON.stringify(fromData),
        headers: {
          "Content-Type": "application/json"
        }
      })
  const reader = response.body.getReader();
  // 将流中的字节数据解码为文本字符串
  const textDecoder = new TextDecoder();
  let result = true;
  marked.setOptions({
        highlight: function (code) {
        return hljs.highlightAuto(code).value;
      }
    });
  while (result) {
    // done表示流是否已经完成读取  value包含读取到的数据块
    const {done, value} = await reader.read();
    if (done) {
      result = false;
      break;
    }
    textDecoder.decode(value).split("\n").forEach((v) => {
      if (v !== "") {
        source_text.value += JSON.parse(v.slice(6))['text']
      }
    })
    markdownContent.value = <string>marked(source_text.value)
  }
}
</script>

<template>
  <el-input v-model="input_data"></el-input>
  <el-button @click="chatV2">点击</el-button>
  <div v-html="markdownContent"></div>
</template>

<style scoped>

</style>