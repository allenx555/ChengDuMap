import Vue from "vue"
import Vuex from "vuex"

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    activeCate: ["0", "1", "2", "3", "4"],
    activeDate: "8",
    nodes: [],
    token: ""
  },
  mutations: {
    setCate(state, Cate) {
      state.activeCate = Cate
    },
    setDate(state, Date1) {
      state.activeDate = Date1
    },
    setNodes(state, Nodes) {
      state.nodes = Nodes
    },
    setToken(state, token) {
      state.token = token
    }
  },
  actions: {},
  modules: {}
})
