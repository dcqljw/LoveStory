<script setup lang="ts">
import {useRoute} from 'vue-router';
import {nextTick, onMounted, reactive, ref, render, watch} from "vue";
import {marked} from "marked";
import {chatListStore} from "@/stores/chatList";
import {Promotion} from "@element-plus/icons-vue"


interface ChatList {
  id: string
  name: string
  icon: string
}

interface ChatHistory {
  id: string,
  data: string,
  type: string,
  time: string,
  user: string,
  icon: string
}


const route = useRoute();
const chatList = chatListStore();
const markdownContent = ref("")
const source_text = ref("")
const current_chat_data = ref<ChatList>()
const send_data = ref("")
const messageViewRef = ref()
const innerRef = ref()
const is_send = ref(true)
const chat_history = reactive<ChatHistory[]>([
  {
    id: "1",
    data: "aaa",
    type: "",
    time: "2023-07-04 11:49",
    user: "qwe",
    icon: "https://lf-flow-web-cdn.doubao.com/obj/flow-doubao/doubao/web/logo-icon.png"
  }, {
    id: "2",
    data: "1234",
    type: "",
    time: "2023-07-04 11:49",
    user: "dcq",
    icon: "https://lf-flow-web-cdn.doubao.com/obj/flow-doubao/doubao/web/logo-icon.png"
  }, {
    id: "3",
    data: "1234",
    type: "",
    time: "2023-07-04 11:49",
    user: "asd",
    icon: "https://lf-flow-web-cdn.doubao.com/obj/flow-doubao/doubao/web/logo-icon.png"
  }
])


const fromData = {
  input_data: ""
}
const chatV2 = async (input_data: string) => {
  // fromData["data"] = input_data.value
  fromData["input_data"] = input_data

  source_text.value = ""
  markdownContent.value = ""
  chat_history.push(
      {
        id: "3",
        data: "*",
        type: "",
        time: "2023-07-04 11:49",
        user: "asd",
        icon: "https://lf-flow-web-cdn.doubao.com/obj/flow-doubao/doubao/web/logo-icon.png"
      }
  )
  let response = await fetch("http://127.0.0.1:8000/api/chat/doubao",
      // let response = await fetch("http://127.0.0.1:8000/chat",
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
  let cache_height = 0
  let result = true;
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
    if (!(cache_height === innerRef.value!.clientHeight)) {
      await setScrollToBottom()
      cache_height = innerRef.value!.clientHeight
    }
    chat_history[chat_history.length - 1].data = <string>marked(source_text.value)
  }
  is_send.value = true
}

const find_current_chat = () => {
  let current_chat_id = <string>route.params.chat_type
  current_chat_data.value = chatList.chatList.find((data) => {
    return data['id'] === current_chat_id ? data : ""
  })
}
const SendHandle = (event: any) => {
  event.preventDefault();
  if (!is_send.value) {
    return
  }
  is_send.value = false
  chat_history.push({
    id: "4",
    data: send_data.value,
    type: "",
    time: "2023-07-04 11:49",
    user: "dcq",
    icon: "https://lf-flow-web-cdn.doubao.com/obj/flow-doubao/doubao/web/logo-icon.png"
  })
  chatV2(send_data.value)

  send_data.value = ""

}

find_current_chat()
watch(() => route.params.chat_type, (newId, oldId) => {
  find_current_chat()
})

async function setScrollToBottom() {
  // 注意：需要通过 nextTick 以等待 DOM 更新完成
  await nextTick()
  const max = innerRef.value!.clientHeight
  messageViewRef.value!.setScrollTop(max)
}

onMounted(() => {
})

</script>

<template>
  <el-container style="height: 100%" class="chat_main">
    <div class="chat_header">
      <div class="chat_title">
        <el-image style="width: 24px" :src="current_chat_data?.icon"></el-image>
        <span class="name">{{ current_chat_data?.name }}</span>
      </div>
    </div>
    <div class="history_view">
      <el-scrollbar height="100%" ref="messageViewRef">
        <div class="message_data" ref="innerRef">
          <div class="message_item" :class="{ 'message_item_right': item.user === 'dcq'}" v-for="item in chat_history"
               :key="item.id">
            <div class="avatar_item">
              <el-image style="width: 24px" :src="item.icon"></el-image>
            </div>
            <div class="message_text">
              <div v-highlight v-html="item.data"></div>
            </div>
          </div>
        </div>
      </el-scrollbar>
    </div>
    <div class="input_view">
      <div class="submit_view">
        <textarea v-model="send_data" style="width: 100%;height: 100px" @keydown.enter="SendHandle"/>
        <el-button type="primary" size="large" class="submit_button" circle>
          <el-icon>
            <Promotion/>
          </el-icon>
        </el-button>
      </div>
    </div>
  </el-container>
</template>

<style scoped>
.chat_main {
  display: flex;
  flex-direction: column;
}

.chat_title {
  display: flex;
  align-items: center;
}

.chat_header {
  display: flex;
  height: 6vh;
}

.history_view {
  height: 70vh;
}

.name {
  margin-left: 10px;
}

.submit_view {
  display: flex;
  align-items: flex-end;
  flex-direction: column;
}

.input_view {
  border: 2px solid #409eff;
  padding: 10px 20px;
  border-radius: 10px;
}

textarea {
  border: none;
  background-color: transparent;
  font-family: inherit;
  font-size: inherit;
  resize: none;
  outline: none;
}

.submit_button {
  align-items: flex-end;
  margin-left: 20px;
}

.message_data {
  padding: 14px;
}

.message_item {
  display: flex;
  margin-bottom: 10px;
}

.message_item_right {
  flex-direction: row-reverse;

  .message_text {
    margin-right: 10px;
  }
}

.message_text {
  border: 2px solid #409eff;
  border-radius: 10px;
  margin-left: 10px;
  padding: 10px;
  max-width: 70%;
}
</style>