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
  height: 99%;
  width: 99%;
  position: absolute;
  z-index: 0;
}
</style>
