<template>
  <div>
    <h2>{{ type.split("-")[0] }}列表</h2>
    <el-table :data="tableData" style="width: 100%" height="250">
      <el-table-column fixed prop="date" label="日期" width="80">
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
  </div>
</template>

<script>
export default {
  props: ["type", "id"],
  data() {
    return {
      tableData: []
    }
  },
  mounted() {}
}
</script>
