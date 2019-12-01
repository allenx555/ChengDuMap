<template>
  <div>
    <el-header id="head">
      <img
        src="../assets/logo.png"
        style="width: 120px;float:left;padding: 6px 0 0px 18px;"
      />
      <el-popover
        placement="bottom"
        width="50"
        trigger="click"
        style="float: left"
      >
        <el-container>
          <el-select v-model="cateValue" multiple placeholder="请选择">
            <el-option
              v-for="item in cateOptions"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            >
            </el-option> </el-select
        ></el-container>

        <el-button slot="reference" type="text"
          ><el-button
            icon="el-icon-menu"
            circle
            style="float: left;margin-left: 50px;margin-top: -10px;"
          ></el-button
        ></el-button>
      </el-popover>

      <el-popover
        placement="bottom"
        width="80"
        trigger="click"
        style="float: left"
      >
        <el-container>
          <el-select v-model="dateValue" clearable placeholder="请选择">
            <el-option
              v-for="item in dateOptions"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            >
            </el-option> </el-select
        ></el-container>
        <el-button slot="reference" type="text"
          ><el-button
            icon="el-icon-time"
            circle
            style="float: left;margin-left: 50px;margin-top: -10px;"
          ></el-button
        ></el-button>
      </el-popover>
      <el-row class="demo-autocomplete">
        <el-col>
          <el-autocomplete
            class="inline-input"
            v-model="search"
            :fetch-suggestions="querySearch"
            placeholder="请输入内容"
            @select="handleSelect"
            style="margin-top: 3px;"
          ></el-autocomplete> </el-col
      ></el-row>
      <div class="avatar">
        <el-popover placement="bottom" width="400" trigger="click">
          <el-container>
            <el-aside width="width: 65px;" style="text-align: center;">
              <el-avatar
                width="100%"
                src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
              ></el-avatar>
              <el-menu
                default-active="1-4-1"
                class="el-menu-vertical-demo"
                :collapse="true"
              >
                <el-menu-item :userIndex="1">
                  <i class="el-icon-message"></i>
                  <span slot="title">消息</span>
                </el-menu-item>
                <el-menu-item :userIndex="2">
                  <i class="el-icon-star-off"></i>
                  <span slot="title">收藏</span>
                </el-menu-item>
                <el-menu-item :userIndex="3">
                  <i class="el-icon-chat-line-square"></i>
                  <span slot="title">评论</span>
                </el-menu-item>
              </el-menu>
            </el-aside>
            <el-main style="padding-left: 20px;">
              <Datalist :type="fetchUserIndex()" />
            </el-main>
          </el-container>

          <el-button slot="reference" type="text"
            ><el-avatar
              style="margin-top: -10px"
              src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
            ></el-avatar
          ></el-button>
        </el-popover>
      </div>
    </el-header>
  </div>
</template>

<script>
import Datalist from "../components/datalist"

export default {
  components: {
    Datalist
  },
  data() {
    return {
      search: "",
      userIndex: 1,
      tableData: [],
      cateOptions: [
        {
          value: "0",
          label: "演唱会"
        },
        {
          value: "1",
          label: "话剧歌剧"
        },
        {
          value: "2",
          label: "休闲展览"
        },
        {
          value: "3",
          label: "二次元"
        },
        {
          value: "4",
          label: "科技比赛"
        }
      ],
      dateValue: this.$store.state.activeDate,
      dateOptions: [
        {
          value: "5",
          label: "一天内"
        },
        {
          value: "6",
          label: "三天内"
        },
        {
          value: "7",
          label: "一周内"
        },
        {
          value: "8",
          label: "一月内"
        }
      ],
      cateValue: this.$store.state.activeCate
    }
  },
  methods: {
    handleSelect() {},
    querySearch(queryString, cb) {
      var options = this.$store.state.nodes
      options = options.map(x => {
        return { value: x.name }
      })
      var results = queryString
        ? options.filter(x => x.value.includes(queryString))
        : options
      // 调用 callback 返回建议列表的数据
      cb(results)
    },
    fetchUserIndex() {
      switch (this.userIndex) {
        case 1:
          return "消息-个人"
        case 2:
          return "收藏-个人"
        case 3:
          return "评论-个人"
      }
    }
  },
  watch: {
    cateValue: function(newVal, oldVal) {
      console.log(newVal)
      this.$store.commit("setCate", newVal)
    },
    dateValue: function(newVal, oldVal) {
      this.$store.commit("setDate", newVal)
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
