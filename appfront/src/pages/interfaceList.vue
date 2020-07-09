<template>
  <el-table
    :data="tableData"
    stripe
    style="width: 100%">
    <el-table-column
      prop="id"
      label="接口id"
      width="180">
    </el-table-column>
    <el-table-column
      prop="name"
      label="接口名称"
      width="180">
    </el-table-column>
    <el-table-column
      prop="project"
      label="所属项目">
    </el-table-column>
    <el-table-column
      prop="model"
      label="所属项目">
    </el-table-column>
    <el-table-column
      prop="method"
      label="所属项目">
    </el-table-column>
    <el-table-column
      prop="datatype"
      label="所属项目">
    </el-table-column>
    <el-table-column
      prop="path"
      label="所属项目">
    </el-table-column>
    <el-table-column
      prop="sign"
      label="所属项目">
    </el-table-column>
    <el-table-column
      prop="desc"
      label="所属项目">
    </el-table-column>

  </el-table>
</template>

<script>
export default {
  data () {
    return {
      tableData: [{
        date: '2016-05-02',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-04',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1517 弄'
      }, {
        date: '2016-05-01',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1519 弄'
      }, {
        date: '2016-05-03',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1516 弄'
      }]
    }
  }
}
</script>
