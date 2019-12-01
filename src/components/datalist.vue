<template>
  <div>
    <h2>{{ type.split("-")[0] }}列表</h2>
    <el-table :data="tableData" style="width: 100%" height="250">
      <el-table-column
        v-if="type.split('-')[1] == '活动'"
        prop="userid"
        label="用户id"
        width="70"
      >
      </el-table-column>
      <el-table-column fixed prop="date" label="日期" width="100">
      </el-table-column>
      <el-table-column
        v-if="type.split('-')[1] !== '活动'"
        prop="name"
        label="活动"
        width="100"
      >
      </el-table-column>
      <el-table-column prop="content" label="内容"> </el-table-column>
    </el-table>
    <el-form
      ref="form"
      :model="form"
      label-width="80px"
      style="margin-top:10px;"
    >
      <el-form-item style="width:80%;float:left;" label="添加评论:">
        <el-input v-model="form.input"></el-input>
      </el-form-item>
      <el-button type="primary" @click="onSubmit" style="float: right;"
        >评论</el-button
      >
    </el-form>
  </div>
</template>

<script>
import { APIClient } from "../utils/client.js"

export default {
  props: ["type", "id"],
  data() {
    return {
      tableData: [],
      form: { input: "" }
    }
  },
  watch: {
    id(newVal, oldVal) {
      if (this.type.split("-")[1] == "活动")
        APIClient.post("/geteventcomment", { eventid: this.id })
          .then(response => {
            this.tableData = response.data.eventlist
          })
          .catch(error => {
            console.log("响应失败:", error)
          })
    }
  },
  methods: {
    onSubmit() {
      APIClient.post("/createcomment", {
        eventid: this.id,
        content: this.form.input
      })
        .then(response => {
          this.tableData = response.data.eventlist
        })
        .catch(error => {
          console.log("响应失败:", error)
        })
    }
  }
}
</script>

<style>
.el-form-item {
  margin-bottom: 0;
}
</style>
