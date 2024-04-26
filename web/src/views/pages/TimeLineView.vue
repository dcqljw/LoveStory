<script setup lang="ts">
import {onBeforeMount, onMounted, ref} from "vue";


const clientWidth = ref(0);

const img_list = ref(
    [
      {
        time: "2024/4/26",
        title: "第一次",
        list: [
          "https://th.wallhaven.cc/small/3l/3lepy9.jpg",
          "https://th.wallhaven.cc/small/9d/9dyeex.jpg",
          "https://th.wallhaven.cc/small/yx/yxrkm7.jpg"
        ]
      },
      {
        time: "2024/3/1",
        title: "第一次",
        list: [
          "https://th.wallhaven.cc/small/1p/1pmoy3.jpg",
          "https://th.wallhaven.cc/small/m3/m3mmq9.jpg",
          "https://th.wallhaven.cc/small/m3/m3m5vy.jpg",
          "https://th.wallhaven.cc/small/qz/qz8pqd.jpg",
          "https://th.wallhaven.cc/small/1p/1pmo7g.jpg",
          "https://th.wallhaven.cc/small/zy/zyrv6g.jpg"
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
              :style="{width:`${(item.list.length > 5) ? 1080:(clientWidth > 500 ?item.list.length * 200:200) + (clientWidth > 500 ? ((item.list.length-1) * 10) + 40: 40)}px`}">
            <div class="title">
              {{ item.title }}
            </div>
            <div class="img_list">
              <el-image
                  :preview-src-list="item.list"
                  :initial-index="idx"
                  style="width: 200px" v-for="(img,idx) in item.list" :key="img" :src="img" lazy>

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
}

:deep(.el-timeline-item__timestamp) {
  font-size: 16px;
}
</style>