<template>
  <div style="height: 100%;">
    <div class="amap-wrapper">
      <el-amap
        class="amap-box"
        :center="center"
        :zoom="zoom"
        :amap-manager="amapManager"
        :vid="'amap-vue'"
        mapStyle="amap://styles/macaron"
      >
        <el-amap-marker
          v-for="(node, index) in activeNodes"
          :position="[node.x, node.y]"
          @click.native="alert(index)"
          :events="marker.events"
          :visible="true"
          :draggable="false"
          :vid="index"
          :key="index"
          :extData="node.id"
          :icon="chooseIcon(node.cate)"
        ></el-amap-marker
      ></el-amap>
    </div>
    <el-card class="box-card" v-show="eventShow">
      <div slot="header" class="clearfix">
        <div style="width:60%">
          <span
            ><b>{{ event.name }}</b></span
          >
        </div>

        <el-button
          icon="el-icon-close"
          circle
          style="float:right;margin-top: -4px;margin-left: 10px;"
          @click="eventClose()"
        ></el-button>
        <el-popover placement="right" width="400" trigger="click">
          <Datalist type="评论-活动" :id="event.id" />
          <el-button
            type="info"
            icon="el-icon-chat-line-square"
            circle
            style="float:right;margin-top: -4px;margin-left: 10px;"
            slot="reference"
          ></el-button>
        </el-popover>
        <el-button
          type="warning"
          icon="el-icon-star-off"
          circle
          style="float:right;margin-top: -4px;margin-left: 10px;"
        ></el-button>
        <el-button
          type="primary"
          icon="el-icon-share"
          circle
          style="float:right;margin-top: -4px;margin-left: 10px;"
        ></el-button>
      </div>
      <div style="overflow-y:auto;">
        <p><b>状态</b></p>
        {{ event.is_active }}
        <p><b>地点</b></p>
        {{ event.location }}
        <p><b>日期</b></p>
        {{ event.startdate }}
        ~
        {{ event.enddate }}
        <p><b>概述</b></p>
        {{ event.description }}
      </div>
    </el-card>
  </div>
</template>

<script>
import { AMapManager, lazyAMapApiLoaderInstance } from "vue-amap"
import icon0 from "../assets/0.png"
import icon1 from "../assets/1.png"
import icon2 from "../assets/2.png"
import icon3 from "../assets/3.png"
import icon4 from "../assets/4.png"
import Datalist from "../components/datalist"
import { APIClient } from "../utils/client.js"

let amapManager = new AMapManager()

export default {
  components: {
    Datalist
  },
  data() {
    let self = this
    return {
      zoom: 11, //初始地图级别
      center: [104.079906, 30.666666], //初始地图中心点
      amapManager,
      nodes: [],
      activeNodes: [],
      cates: ["演唱会", "话剧歌剧", "动漫", "休闲展览", "科技比赛"],
      marker: {},
      event: {},
      eventShow: false
    }
  },
  created() {
    APIClient.get("/geteventlist")
      .then(response => {
        this.nodes = response.data.eventlist
        this.activeNodes = this.nodes
        this.$store.commit("setNodes", this.nodes)
      })
      .catch(error => {
        console.log("响应失败:", error)
      })
    // this.nodes[0] = {
    //   eventID: 1,
    //   name: "知更鸟动漫游戏交流展",
    //   is_active: "售票中",
    //   startdate: "2020.01.01 09:30",
    //   enddate: "2020.01.02 17:00",
    //   phone: "",
    //   location: "中国西部国际博览城",
    //   x: "104.081785",
    //   y: "30.420097",
    //   cate: "2",
    //   description:
    //     "#知更鸟动漫游戏交流展#我们来了！为所有喜爱ACG的小伙伴们带来最好玩最有趣的漫展体验"
    // }
    let that = this
    this.marker = {
      events: {
        click(e) {
          that.markerClick(e)
        }
      }
    }
  },
  watch: {
    "$store.state.activeCate": function(newVal, oldVal) {
      this.activeNodes = this.nodes
        .map(node => {
          if (newVal.includes(node.cate)) return node
        })
        .filter(res => {
          return res != undefined
        })
    }
  },
  methods: {
    eventClose() {
      this.eventShow = false
    },
    markerClick(e) {
      this.event = this.searchNode(e.target.getExtData())
      this.eventShow = true
    },
    searchNode(id) {
      for (let index in this.nodes) {
        if (this.nodes[index].id == id) return this.nodes[index]
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
.box-card {
  width: 500px;
  position: absolute;
  top: 80px;
  left: 30px;
  transform-origin: center top;
  z-index: 2001;
  text-align: left;
  max-height: 600px;
  overflow: auto;
}
</style>
