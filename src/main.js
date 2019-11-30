import Vue from "vue"
import ElementUI from "element-ui"
import "element-ui/lib/theme-chalk/index.css"
import router from "./router"
import store from "./store"
import App from "./App.vue"

Vue.use(ElementUI)

Vue.config.productionTip = false

new Vue({
  el: "#app",
  router,
  store,
  render: h => h(App)
})
