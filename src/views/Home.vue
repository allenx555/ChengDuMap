<template>
  <div class="home">
    <Map />
  </div>
</template>

<script>
import Map from "../components/map.vue"
// @ is an alias to /src
export default {
  name: "home",
  components: {
    Map
  }
}
</script>

<style>
.home {
  height: calc(100% - 60px);
  width: 100%;
}
</style>
