<template>
  <div class="amap-wrapper">
    <el-amap
      class="amap-box"
      :center="center"
      :zoom="zoom"
      :amap-manager="amapManager"
      :vid="'amap-vue'"
      mapStyle="amap://styles/whitesmoke"
    ></el-amap>
  </div>
</template>

<script>
import { AMapManager, lazyAMapApiLoaderInstance } from "vue-amap"

let amapManager = new AMapManager()

export default {
  data() {
    let self = this
    return {
      zoom: 11, //初始地图级别
      center: [104.079906, 30.666666], //初始地图中心点
      amapManager,
      events: {
        events: {
          init() {
            lazyAMapApiLoaderInstance.load().then(() => {
              self.initSearch()
            })
          }
        }
      }
    }
  },
  mounted() {},
  methods: {
    console1() {
      let map = this.amapManager.getMap()
      let marker = new AMap.Marker({
        position: [104.079906, 30.666666]
      })
      let bounds = map.getBounds()
      map.setLimitBounds(bounds)
      marker.setMap(map)
    }
  }
}
</script>

<style>
.amap-wrapper {
  width: 100%;
  height: 100%;
}
</style>
