<template>

  <el-table :data="tableData" stripe style="width: 100%">
    <el-table-column prop="id" label="接口id" width="180"></el-table-column>
    <el-table-column prop="name" label="接口名称" width="180"></el-table-column>
    <el-table-column prop="path" label="接口路径" width="180"></el-table-column>
    <el-table-column prop="project" label="所属项目"></el-table-column>
    <el-table-column prop="model" label="所属模块"></el-table-column>
    <el-table-column prop="method" label="请求方式"></el-table-column>
    <el-table-column prop="datatype" label="请求参数类型"></el-table-column>
    <el-table-column prop="sign" label="是否签名"></el-table-column>
    <el-table-column prop="desc" label="接口描述"></el-table-column>
    <el-table-column width="100" label="操作" flex="right">
      <template slot-scope="scope">
        <el-button @click="handleClick(scope.row)" type="text" size="small">查看</el-button>
        <el-button type="text" size="small">编辑</el-button>
        <el-button type="text" size="small">复制</el-button>
        <el-button type="text" size="small">删除</el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
export default {
  data () {
    return {
      tableData: [{
        id: '1',
        name: '测试接口',
        path: '/api/v1/test',
        project: '测试项目',
        model: '测试模块',
        method: 'get',
        datatype: '',
        sign: false,
        desc: '这是一个测试接口',
        header: '',
        body: "{'a':1,'b':2}"

      }, {
        id: '2',
        name: '测试接口',
        path: '/api/v1/test',
        project: '测试项目',
        model: '测试模块',
        method: 'get',
        datatype: '',
        sign: false,
        desc: '这是一个测试接口',
        header: '',
        body: "{'a':1,'b':2}"

      }]
    }
  }
}
</script>
