import Vue from "vue"
import ElementUI from "element-ui"
import "element-ui/lib/theme-chalk/index.css"
import router from "./router"
import VueAMap from "vue-amap"
import store from "./store"
import App from "./App.vue"

Vue.use(ElementUI)

Vue.use(VueAMap)
VueAMap.initAMapApiLoader({
  key: "d8469339f3206bb942f1b0db2eeebb2c",
  plugin: [
    "AMap.Autocomplete",
    "AMap.PlaceSearch",
    "AMap.Scale",
    "AMap.OverView",
    "AMap.ToolBar",
    "AMap.MapType",
    "AMap.PolyEditor",
    "AMap.CircleEditor"
  ],
  // 默认高德 sdk 版本为 1.4.4
  v: "1.4.4"
})

Vue.config.productionTip = false

new Vue({
  el: "#app",
  router,
  store,
  render: h => h(App)
})
