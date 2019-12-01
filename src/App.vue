<template>
  <div id="app">
    <Header />
    <router-view />
  </div>
</template>

<script>
import Header from "@/components/header.vue"

export default {
  components: {
    Header
  }
}
</script>

<style lang="scss">
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: rgba(243, 248, 255, 0.8);
  width: 100%;
  height: 100%;
  #head {
    position: absolute;
    z-index: 99;
    width: 99%;
    background-color: rgba(243, 248, 255, 0.6);
  }
}
#nav {
  padding: 30px;
  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
