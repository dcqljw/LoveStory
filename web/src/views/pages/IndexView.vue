<script setup lang="ts">
import {ref} from "vue";

const current_data = ref()
const show_dialog = ref(false)

const img_list = ref([
    {
  'src': 'https://w.wallhaven.cc/full/m3/wallhaven-m3m5vy.jpg',
  'desc': 'Anime 2732x5412 anime boys Son Goku Dragon Ball outdoors nature dragonflies trees smiling',
  'h': 4
}, {
  'src': 'https://w.wallhaven.cc/full/x6/wallhaven-x62wko.jpg',
  'desc': 'General 3963x2972 Russia nature snow winter clouds sea landscape cliff coast monochrome low light',
  'h': 4
}, {
  'src': 'https://w.wallhaven.cc/full/yx/wallhaven-yxrkdl.jpg',
  'desc': 'Anime 1200x2411 bodysuit mask latex',
  'h': 4
}, {
  'src': 'https://w.wallhaven.cc/full/2y/wallhaven-2y57e6.jpg',
  'desc': 'Anime 1000x2000 Neon Genesis Evangelion anime girls portrait display Katsuragi Misato pouring jean shorts purple hair looking at viewer thighs big boobs yellow tank top kneeling watermarked signature bare midriff long hair brown eyes can beer drink Jason Liang drawing shorts bright background',
  'h': 4
}, {
  'src': 'https://w.wallhaven.cc/full/7p/wallhaven-7pkgjy.jpg',
  'desc': 'General 2165x3849 Fallout Vault Dweller vault girl portrait display digital art women',
  'h': 4
}, {
  'src': 'https://w.wallhaven.cc/full/ex/wallhaven-ex1rvl.jpg',
  'desc': 'General 3954x2965 Russia sea winter forest landscape nature',
  'h': 4
}, {
  'src': 'https://w.wallhaven.cc/full/ex/wallhaven-ex11jo.jpg',
  'desc': 'Anime 1593x1200 landscape natural light trees branch nature night clouds',
  'h': 4
}, {
  'src': 'https://w.wallhaven.cc/full/x6/wallhaven-x62g3o.jpg',
  'desc': 'General 2160x3840 Mary Mushkin NoPixel digital art red dress high heels redhead hairbun necklace tattoo looking at viewer red eyes mask red nails women',
  'h': 4
}, {
  'src': 'https://w.wallhaven.cc/full/5g/wallhaven-5g8383.png',
  'desc': 'Anime 1500x2667 Acheron (Honkai: Star Rail) Honkai: Star Rail illustration character design ',
  'h': 4
}, {
  'src': 'https://w.wallhaven.cc/full/2y/wallhaven-2y5me6.png',
  'desc': 'General 3606x2404 neon nature synthwave dark river satellite aerial view',
  'h': 4
}, {
  'src': 'https://w.wallhaven.cc/full/kx/wallhaven-kx6jzq.png',
  'desc': 'Anime 2157x3844 anime girls schoolgirl Uzawa Reisa school uniform portrait display Blue Archive fan art video game characters',
  'h': 4
}, {
  'src': 'https://w.wallhaven.cc/full/p9/wallhaven-p9xp1e.jpg',
  'desc': 'General 7008x4672 clouds blue nature',
  'h': 4
}, {
  'src': 'https://w.wallhaven.cc/full/kx/wallhaven-kx6re7.jpg',
  'desc': 'General 4730x3153 iceberg ice sea nature landscape aerial view Greenland Ilulissat Icefjord fjord sunset',
  'h': 4
}, {
  'src': 'https://w.wallhaven.cc/full/m3/wallhaven-m3m5p8.jpg',
  'desc': 'General 4032x3024 nature mountains clouds trees',
  'h': 4
}, {'src': "", 'desc': "", 'h': 4}, {
  'src': "",
  'desc': "",
  'h': 4
}, {
  'src': 'https://w.wallhaven.cc/full/5g/wallhaven-5g8987.jpg',
  'desc': 'General 4800x3600 landscape coast cliff sea California forest cypress clouds nature USA cumulus',
  'h': 4
}, {'src': "", 'desc': "", 'h': 4}, {'src': "", 'desc': "", 'h': 4}, {
  'src': "",
  'desc': "",
  'h': 4
}, {
  'src': 'https://w.wallhaven.cc/full/we/wallhaven-wer2x7.jpg',
  'desc': 'General 4000x2667 clouds nature landscape mountain chain snow North Cascades National Park USA mountains sunset',
  'h': 4
}, {'src': "", 'desc': "", 'h': 4}, {'src': "", 'desc': "", 'h': 4}, {
  'src': "",
  'desc': "",
  'h': 4
}, {
  'src': 'https://w.wallhaven.cc/full/x6/wallhaven-x62ogo.jpg',
  'desc': 'General 2000x1334 landscape nature starry night forest lake water low light',
  'h': 4
}, {
  'src': 'https://w.wallhaven.cc/full/85/wallhaven-851q61.jpg',
  'desc': 'General 3333x2500 JeffHoly artwork military uniform Military Hat peaked cap epaulettes tie leather shoes smiling men nature trees watch blonde dark hair leather boots USSR Soviet Army military propaganda',
  'h': 4
}, {
  'src': 'https://w.wallhaven.cc/full/zy/wallhaven-zyr7jw.jpg',
  'desc': 'General 3840x3840 Forever (artist) CGI women Asian portrait glasses',
  'h': 4
}, {
  'src': 'https://w.wallhaven.cc/full/x6/wallhaven-x62wvl.jpg',
  'desc': 'Anime 850x1518 Sousou No Frieren Frieren portrait display anime girls looking at viewer flowers flower crown pointy ears mountains long sleeves elves women outdoors pantyhose twintails closed mouth clouds Ryo E petals sky',
  'h': 4
}, {
  'src': 'https://w.wallhaven.cc/full/l8/wallhaven-l875wl.jpg',
  'desc': 'General 4240x2832 landscape nature snow Canada British Columbia fog mist clouds mountain view winter',
  'h': 4
}, {
  'src': 'https://w.wallhaven.cc/full/gp/wallhaven-gplo3l.jpg',
  'desc': 'Anime 1080x1920 Sousou No Frieren flowers portrait display anime girls Fern (Sousou No Frieren) purple hair purple eyes looking at viewer leaves purple flowers long hair Liu Liaoliao closed mouth',
  'h': 4
}, {
  'src': 'https://w.wallhaven.cc/full/we/wallhaven-wer9gq.png',
  'desc': 'General 2601x1732 sky space eclipse  nature Canada',
  'h': 4
}, {
  'src': 'https://w.wallhaven.cc/full/jx/wallhaven-jxop2q.jpg',
  'desc': 'Anime 1080x1920 anime anime girls Fern (Sousou No Frieren) Sousou No Frieren purple Bara big boobs snow',
  'h': 4
}, {
  'src': 'https://w.wallhaven.cc/full/x6/wallhaven-x62rez.jpg',
  'desc': 'General 4032x3024 mountains nature landscape',
  'h': 4
}, {
  'src': 'https://w.wallhaven.cc/full/3l/wallhaven-3lep7d.jpg',
  'desc': 'Anime 5200x3900 classroom desk teachers world history globes',
  'h': 4
}, {
  'src': 'https://w.wallhaven.cc/full/p9/wallhaven-p9x183.jpg',
  'desc': 'General 4032x3024 mountains nature clouds trees road aerial view',
  'h': 4
}, {
  'src': 'https://w.wallhaven.cc/full/rr/wallhaven-rrz5jm.png',
  'desc': 'General 3000x3000 humor animals bull birds',
  'h': 4
}, {
  'src': 'https://w.wallhaven.cc/full/gp/wallhaven-gpk89e.jpg',
  'desc': 'General 5400x3600 snow winter Colorado landscape mountain view mountains cliff forest nature',
  'h': 4
}, {
  'src': 'https://w.wallhaven.cc/full/d6/wallhaven-d6qrql.png',
  'desc': 'Anime 2499x3995 portrait display sitting aqua eyes open mouth looking at viewer night starred sky starry night purple flowers flowers hair over one eye sky smiling water drops Sainome blue shorts purple hair short hair choker women outdoors thighs orb water stars shorts leaves',
  'h': 4
}, {
  'src': 'https://w.wallhaven.cc/full/kx/wallhaven-kx6qrq.jpg',
  'desc': 'Anime 2160x3840 room anime boys dark night rain music relaxation city',
  'h': 4
}, {
  'src': 'https://w.wallhaven.cc/full/ex/wallhaven-ex1jvw.jpg',
  'desc': 'People 9504x6336 Umeko J women model Asian cosplay Viper (Valorant) Valorant video games video game girls ass',
  'h': 4
}, {
  'src': 'https://w.wallhaven.cc/full/2y/wallhaven-2y5wv9.jpg',
  'desc': 'General 1280x960 pixel art nature outdoors landscape digital art video game art mountains lake reflection Mark Ferrari',
  'h': 4
}])
const show_img_list = ref([
  [],
  [],
  [],
  [],
  [],
])

const generate_img = () => {
  for (let i = 450; i < 550; i++) {
    let h = Math.floor(Math.random() * (5 - 2 + 1)) + 2;
    console.log(h)
    let temp = `https://picsum.photos/seed/${i}/200/${h}00`
    img_list.value.push({src: temp, height: h, desc: '这是一张图片'})
  }
}
// generate_img()

const compute_img = () => {
  console.log(show_img_list.value)
  let start_idx = 0
  for (let i = 1; i < 5; i++) {
    if (show_img_list.value[i] < show_img_list.value[i + 1]) {
      start_idx = i
    }
  }
  while (img_list.value.length > 0) {
    console.log(img_list.value)
    show_img_list.value[start_idx].push(img_list.value[0])
    if (start_idx == 4) {
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

const preview = (data) => {
  console.log(data)
  current_data.value = data
  show_dialog.value = true
}

</script>

<template>
  <el-scrollbar max-height="90vh">
    <div class="img_list">
      <div class="item-col" v-for="item in show_img_list" :key="item">
        <el-card class="item" v-for="img in item" :key="img" @click="preview(img)">
          <el-image fit="cover" style="width: 100%" :style="{height:`${img.height}00px`}" :src="img.src" lazy>
          </el-image>
          <div class="desc">
            {{ img.desc }}
          </div>

        </el-card>
      </div>

    </div>
  </el-scrollbar>
  <el-dialog
      v-model="show_dialog"
      title="Tips"
      width="500"
      align-center
  >
    <div class="detail">
      <el-image :src="current_data.src"/>
      <div>
        <div class="desc_detail">
          {{ current_data.desc }}
        </div>
      </div>
    </div>

    <template #footer>
      <div class="dialog-footer">
        <el-button @click="show_dialog = false">Cancel</el-button>
        <el-button type="primary" @click="show_dialog = false">
          Confirm
        </el-button>
      </div>
    </template>
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
  //width: 220px;
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
  font-size: 14px;
  padding: 10px;
}

.detail {
  display: flex;
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