<script setup lang="ts">
import {onBeforeMount, onMounted, ref} from "vue";


const clientWidth = ref(0);

const img_list = ref(
    [
      {
        time: "2024/4/26",
        title: "你🐉🐎",
        list: [
          "https://w.wallhaven.cc/full/l8/wallhaven-l87pjy.jpg",
          "https://w.wallhaven.cc/full/5g/wallhaven-5g8335.jpg",
          "https://w.wallhaven.cc/full/m3/wallhaven-m3mekk.jpg"
        ]
      },
      {
        time: "2024/3/1",
        title: "🐕‍🦺📣?",
        list: [
          "https://w.wallhaven.cc/full/2y/wallhaven-2y56l9.jpg",
          "https://w.wallhaven.cc/full/x6/wallhaven-x62g3o.jpg",
          "https://w.wallhaven.cc/full/m3/wallhaven-m3m7y1.png",
          "https://w.wallhaven.cc/full/kx/wallhaven-kx6ow1.png",
          "https://w.wallhaven.cc/full/p9/wallhaven-p9xx39.jpg",
          "https://w.wallhaven.cc/full/85/wallhaven-85117k.jpg"
        ]
      }
    ]
)
window.onresize = () => {
  console.log(document.body.clientWidth)
  clientWidth.value = document.body.clientWidth
}
onBeforeMount(() => {
  clientWidth.value = document.body.clientWidth

})
onMounted(() => {
})
</script>

<template>
  <el-scrollbar max-height="70vh">
    <div>
      <el-timeline style="max-width: 1000px">
        <el-timeline-item v-for="item in img_list" :timestamp="item.time" placement="top">
          <el-card
              style="max-width: 1080px;"
              :style="{width:`${(clientWidth > 500 ?item.list.length * 200:200) + (clientWidth > 500 ? ((item.list.length-1) * 10) + 40: 40)}px`}">
            <div class="title">
              {{ item.title }}
            </div>
            <div class="img_list">
              <el-image
                  fit="cover"
                  :preview-src-list="item.list"
                  :initial-index="idx"
                  style="width: 200px;height: 150px" v-for="(img,idx) in item.list" :key="img" :src="img" lazy>

              </el-image>
            </div>

          </el-card>
        </el-timeline-item>
      </el-timeline>
    </div>
    <el-backtop></el-backtop>
  </el-scrollbar>
</template>

<style scoped>
.img_list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  flex-direction: row;
}

.title {
  padding-bottom: 10px;
  font-size: 16px;
}

:deep(.el-timeline-item__timestamp) {
  font-size: 16px;
}
</style>