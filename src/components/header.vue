<template>
  <div>
    <el-header id="head">
      <el-button
        icon="el-icon-menu"
        circle
        style="float: left;margin-left: 50px;"
      ></el-button>
      <el-row class="demo-autocomplete">
        <el-col>
          <el-autocomplete
            class="inline-input"
            v-model="state1"
            :fetch-suggestions="querySearch"
            placeholder="请输入内容"
            :trigger-on-focus="false"
            @select="handleSelect"
          ></el-autocomplete> </el-col
      ></el-row>
      <div class="avatar">
        <el-popover placement="right" width="400" trigger="click">
          <el-container>
            <el-aside width="125px" style="text-align: center;">
              <el-avatar
                width="100%"
                src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
              ></el-avatar>
            </el-aside>
            <el-main>Main</el-main>
          </el-container>

          <el-button slot="reference" type="text"
            ><el-avatar
              style="margin-top: -13px"
              src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
            ></el-avatar
          ></el-button>
        </el-popover>
      </div>
    </el-header>
  </div>
</template>

<script>
export default {
  data() {
    return {
      gridData: [
        {
          date: "2016-05-02",
          name: "王小虎",
          address: "上海市普陀区金沙江路 1518 弄"
        },
        {
          date: "2016-05-04",
          name: "王小虎",
          address: "上海市普陀区金沙江路 1518 弄"
        },
        {
          date: "2016-05-01",
          name: "王小虎",
          address: "上海市普陀区金沙江路 1518 弄"
        },
        {
          date: "2016-05-03",
          name: "王小虎",
          address: "上海市普陀区金沙江路 1518 弄"
        }
      ]
    }
  }
}
</script>

<style lang="scss">
#head {
  .demo-autocomplete {
    float: left;
    margin-left: 50px;
  }
  .el-select {
    width: 300px;
  }
  .el-input {
    width: 300px;
  }
  .avatar {
    float: right;
    margin-right: 50px;
  }
}
</style>
