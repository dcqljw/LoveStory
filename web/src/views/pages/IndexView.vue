<script setup lang="ts">
import {onBeforeMount, type Ref, ref} from "vue";
import {useRouter} from "vue-router";
import {ErrorPicture, CloseOne} from '@icon-park/vue-next'

const router = useRouter()
const current_data = ref()
const show_dialog = ref(false)
const clientWidth = ref(0)
const col = ref(5)
const start_idx_end = ref(4)

interface img_list {
  src: string
  desc: string
  h: number
}

// const img_list: Ref<{ src: string     desc: string     h: number }[]>
const img_list = ref<img_list[]>([
  {
    'src': 'https://w.wallhaven.cc/full/l8/wallhaven-l87pjy.jpg',
    'desc': 'General 3840x1921 Helldivers 2 fan art robot space battle video games PlayStation video game art soldier Democracy video game characters animatronic spaceship boys with guns',
    'h': 4
  }, {
    'src': 'https://w.wallhaven.cc/full/5g/wallhaven-5g8335.jpg',
    'desc': 'Anime 2370x1000 Genshin Impact kimono Chiori (Genshin Impact) black gloves white socks cherry blossom mountains dog clouds petals spring wboss doll qianzhi',
    'h': 4
  }, {
    'src': 'https://w.wallhaven.cc/full/m3/wallhaven-m3mekk.jpg',
    'desc': 'Anime 1972x3000 anime anime girls Nishikigi Chisato Lycoris Recoil Inoue Takina rifles anime girls with guns',
    'h': 4
  }, {
    'src': 'https://w.wallhaven.cc/full/2y/wallhaven-2y56l9.jpg',
    'desc': 'General 4724x3307 digital art artwork illustration painting landscape clouds sea water boat sailing ship sunset sky sailboats',
    'h': 4
  }, {
    'src': 'https://w.wallhaven.cc/full/x6/wallhaven-x62g3o.jpg',
    'desc': 'General 2160x3840 Mary Mushkin NoPixel digital art red dress high heels redhead hairbun necklace tattoo looking at viewer red eyes mask red nails women',
    'h': 4
  }, {
    'src': 'https://w.wallhaven.cc/full/m3/wallhaven-m3m7y1.png',
    'desc': 'General 1920x1080 distortion digital art CGI abstract 3D Abstract glitch art space station astronaut Moon Base Moon synthwave Blender night artwork science fiction 1980s vaporwave retro style space space art retrowave retro theme',
    'h': 4
  }, {
    'src': 'https://w.wallhaven.cc/full/kx/wallhaven-kx6ow1.png',
    'desc': 'General 2560x1440 8-bit spaceship Asian architecture alien invasion',
    'h': 4
  }, {
    'src': 'https://w.wallhaven.cc/full/qz/wallhaven-qzedkq.png',
    'desc': 'Anime 2894x4328 two women pantyhose portrait display blushing flight attendant blue skirt airplane interior Benevole mole under eye black hair group of people sweatdrop yuri moles gloves',
    'h': 4
  }, {
    'src': 'https://w.wallhaven.cc/full/p9/wallhaven-p9xx39.jpg',
    'desc': 'Anime 5640x2400 anime sky Gracile artwork anime girls',
    'h': 4
  }, {
    'src': 'https://w.wallhaven.cc/full/9d/wallhaven-9dywpx.jpg',
    'desc': 'Anime 3840x2160 anime girls looking at viewer short hair indoors',
    'h': 4
  }, {
    'src': 'https://w.wallhaven.cc/full/6d/wallhaven-6dzvzw.jpg',
    'desc': 'Anime 3840x2160 animation anime Studio Ghibli illustration field nature rock formation sky 4K Spirited Away clouds',
    'h': 4
  }, {
    'src': 'https://w.wallhaven.cc/full/kx/wallhaven-kx6j57.jpg',
    'desc': 'General 3508x2480 digital art artwork illustration landscape field mountains forest nature river clouds plants women yellow skirt skirt drawing',
    'h': 4
  }, {
    'src': 'https://w.wallhaven.cc/full/yx/wallhaven-yxr3wg.png',
    'desc': 'Anime 2560x1440 Honkai: Star Rail Acheron (Honkai: Star Rail) anime games',
    'h': 4
  }, {
    'src': 'https://w.wallhaven.cc/full/5g/wallhaven-5g8383.png',
    'desc': 'Anime 1500x2667 Acheron (Honkai: Star Rail) Honkai: Star Rail illustration character design ',
    'h': 4
  }, {
    'src': 'https://w.wallhaven.cc/full/kx/wallhaven-kx6yqm.png',
    'desc': 'General 2560x1440 Christian Benavides digital art Japanese landscape nature torii outdoors',
    'h': 4
  }, {
    'src': 'https://w.wallhaven.cc/full/2y/wallhaven-2y5xly.jpg',
    'desc': 'Anime 5160x2160 anime girls shadow silhouette',
    'h': 4
  }, {
    'src': 'https://w.wallhaven.cc/full/1p/wallhaven-1pm2g9.png',
    'desc': 'General 2560x1440 Cyberpunk 2077 city lights digital art video games low light',
    'h': 4
  }, {
    'src': 'https://w.wallhaven.cc/full/85/wallhaven-85117k.jpg',
    'desc': 'Anime 5640x2400 sky Gracile grass poles fog artwork',
    'h': 4
  }, {
    'src': 'https://w.wallhaven.cc/full/7p/wallhaven-7pqvdy.png',
    'desc': 'General 3840x2160 genskc cherry trees cherry blossom stairs bicycle utility pole digital art artwork dandelion',
    'h': 4
  }, {
    'src': 'https://w.wallhaven.cc/full/yx/wallhaven-yxrd7k.jpg',
    'desc': 'Anime 3360x1440 Honkai: Star Rail artwork Sparkle (Honkai: Star Rail) anime anime girls brunette red eyes white stockings kimono goldfish twintails Asian architecture lantern hair blowing in the wind void_0',
    'h': 4
  }])
const show_img_list = ref([
  [],
  [],
  [],
  [],
  [],
])

const compute_img = () => {
  console.log(show_img_list.value)
  let start_idx = 0
  for (let i = 1; i < col.value; i++) {
    if (show_img_list.value[i] < show_img_list.value[i + 1]) {
      start_idx = i
    }
  }
  while (img_list.value.length > 0) {
    console.log(img_list.value)
    show_img_list.value[start_idx].push(img_list.value[0])
    if (start_idx === start_idx_end.value) {
      start_idx = 0
    } else {
      start_idx++
    }
    img_list.value.shift()
  }
  console.log(show_img_list.value.length)
  console.log(show_img_list.value)
}
compute_img()

const preview = (data: any) => {
  console.log(data)
  let cw = document.body.clientWidth
  if (cw < 700) {
    router.push("/test")
  } else {
    current_data.value = data
    show_dialog.value = true
  }
}

onBeforeMount(() => {
  clientWidth.value = document.body.clientWidth
  if (clientWidth.value < 1000) {
    col.value = 2
    start_idx_end.value = 1
  }
})


</script>

<template>
    <div class="img_list">
      <div class="item-col" v-for="item in show_img_list" :key="item">
        <el-card class="item" v-for="img in item" :key="img" @click="preview(img)">
          <el-image fit="cover" style="width: 100%" :style="{height:`${img.height}00px`}"
                    :src="img.src" lazy>
            <template #placeholder>
              <el-skeleton animated style="width: 100%">
                <template #template>
                  <el-skeleton-item variant="image" style="width: 100%; height: 240px"/>
                </template>
              </el-skeleton>
            </template>
            <template #error>
              <div class="image-slot">
                <error-picture theme="outline" size="36" fill="#888888"/>
              </div>
            </template>
          </el-image>
          <div class="desc">
            <div class="desc_text">
              {{ img.desc }}
            </div>
          </div>
        </el-card>
      </div>

    </div>
  <el-dialog
      v-model="show_dialog"
      width="900"
      align-center
      :close-icon="CloseOne"
  >
    <div class="detail">
      <el-image
          fit="cover"
          :initial-index="0"
          :preview-src-list="[current_data.src]"
          :src="current_data.src"/>
      <div>
        <div class="desc_detail">
          <div class="desc">
            {{ current_data.desc }}
          </div>
        </div>
      </div>
    </div>
  </el-dialog>

</template>

<style scoped>
.img_list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: space-around;
}

.item {
  min-height: 400px;
}

.item-col {
  width: 200px;
  display: flex;
  gap: 10px;
  flex-direction: column;
}

:deep(.el-card__body) {
  padding: 0;
  width: 100%;
}

:deep(.el-image) {
  display: block;
}

.desc {
  padding: 10px;
}

.image-slot {
  display: flex;
  justify-content: center;
  height: 200px;
  align-items: center;
  background: #f7f7f7;
}

.desc_text {
  font-size: 14px;
  display: -webkit-box;
  -webkit-line-clamp: 3; /* 限制显示的行数，这里以3行为例 */
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
  width: 200px; /* 设置容器宽度 */
  white-space: normal;
}

.desc_text::after {
  content: "...";
  position: absolute;
  bottom: 0;
  right: 0;
  padding-left: 4px; /* 根据需要调整省略号与文本之间的间距 */
  background-color: white;
}

.detail {
  display: flex;
  height: 80vh;
}

.desc_detail {
  padding: 0 20px;
}

@media (max-width: 500px) {
  .img_list {
    gap: 0;
  }

  .item-col {
    width: calc(100vw / 2 - 10px);
  }
}

@media (max-width: 900px)and (min-width: 500px) {
  .item-col {
    width: calc(534px / 2 - 10px);
  }
}

@media (min-width: 900px) {
  .item-col {
    width: calc(1340px / 5 - 10px);
  }
}
</style>