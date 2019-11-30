<template>
  <div class="amap-wrapper">
    <el-amap
      class="amap-box"
      :center="center"
      :zoom="zoom"
      :amap-manager="amapManager"
      :vid="'amap-vue'"
      mapStyle="amap://styles/whitesmoke"
    >
      <el-amap-marker
        v-for="(node, index) in nodes"
        :position="[node.x, node.y]"
        @click.native="alert(index)"
        :events="marker.events"
        :visible="true"
        :draggable="false"
        :vid="index"
        :key="index"
        :extData="node.eventID"
        :icon="chooseIcon(node.cate)"
      ></el-amap-marker
    ></el-amap>
  </div>
</template>

<script>
import { AMapManager, lazyAMapApiLoaderInstance } from "vue-amap"
import icon0 from "../assets/0.png"
import icon1 from "../assets/1.png"
import icon2 from "../assets/2.png"
import icon3 from "../assets/3.png"
import icon4 from "../assets/4.png"

let amapManager = new AMapManager()

export default {
  data() {
    let self = this
    return {
      zoom: 11, //初始地图级别
      center: [104.079906, 30.666666], //初始地图中心点
      amapManager,
      nodes: [],
      cates: ["演唱会", "话剧歌剧", "动漫", "休闲展览", "科技比赛"],
      marker: {}
    }
  },
  created() {
    this.nodes[0] = {
      eventID: 1,
      name: "知更鸟动漫游戏交流展",
      is_active: "售票中",
      startdate: "2020.01.01 09:30",
      enddate: "2020.01.02 17:00",
      phone: "",
      location: "中国西部国际博览城",
      x: "104.081785",
      y: "30.420097",
      cate: "2",
      description:
        "#知更鸟动漫游戏交流展#我们来了！为所有喜爱ACG的小伙伴们带来最好玩最有趣的漫展体验"
    }
    let that = this
    this.marker = {
      events: {
        click(e) {
          that.markerClick(e)
        }
      }
    }
  },
  methods: {
    markerClick(e) {
      let node = this.searchNode(e.target.getExtData())
      this.$alert(
        "<div style:'overflow-y:auto;'><h3>状态</h3>" +
          node.is_active +
          "<h3>地点</h3>" +
          node.location +
          "<h3>联系电话</h3>" +
          node.phone +
          "<h3>日期</h3>" +
          node.startdate +
          "~" +
          node.enddate +
          "<h3>概述</h3>" +
          node.description +
          "</div>",
        node.name,
        {
          dangerouslyUseHTMLString: true
        }
      )
    },
    searchNode(id) {
      for (let index in this.nodes) {
        if (this.nodes[index].eventID == id) return this.nodes[index]
      }
    },
    chooseIcon(cate) {
      switch (cate) {
        case "0":
          return icon0
        case "1":
          return icon1
        case "2":
          return icon2
        case "3":
          return icon3
        case "4":
          return icon4
      }
    }
  }
}
</script>

<style>
.amap-wrapper {
  width: 100%;
  height: 100%;
}
.v-modal {
  opacity: 0;
}
</style>
