<template>
  <div class="header_container">
    <el-breadcrumb separator="/">
      <el-breadcrumb-item :to="{ path: '/management/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item v-for="(item, index) in $route.meta" :key="index">{{item}}</el-breadcrumb-item>
    </el-breadcrumb>
    <el-dropdown @command="handleCommand" menu-align="start">
      <img :src="baseImgPath + adminInfo.avatar" class="avator" />
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item command="home">首页</el-dropdown-item>
        <!-- <el-dropdown-item command="signout">退出</el-dropdown-item> -->
      </el-dropdown-menu>
    </el-dropdown>
  </div>
</template>

<script>
import {baseImgPath} from '@/config/env'

export default {
  data () {
    return baseImgPath
  }
}
</script>
