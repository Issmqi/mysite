/* eslint-disable no-tabs */
<template>
  <div class="data_section">
    <!-- <div class="account"> -->
      <header class="section_title">欢迎来到接口自动化测试平台</header>
      <!-- <el-row :gutter="20" style="margin-bottom: 10px;">
       <div class="wealcome">
          <span class="data_num head">欢迎来到接口自动化测试平台</span>
        </div>
      </el-row>-->
      <el-row :gutter="20" style="margin-bottom: 30px;">
        <el-col :span="5">
          <div class="data_list">
            <el-col span="12">
              <div class="icon">
                <!-- <i class="icon-activity"></i> -->
                <i class="el-icon-menu"></i>
              </div>
            </el-col>
            <el-col span="12">
              <div class="data_count">
                <el-row gutter="20" style="margin-bottom: 10px;">
                  <span class="data_name">总项目</span>
                </el-row>
                <el-row gutter="20" style="margin-bottom: 10px;">
                  <span class="data_num">{{projectCount}}</span>
                </el-row>
              </div>
            </el-col>
          </div>
        </el-col>

        <el-col :span="5">
          <div class="data_list">
            <el-col span="12">
              <div class="icon">
                <i class="el-icon-document"></i>
              </div>
            </el-col>
            <el-col span="12">
              <div class="data_count">
                <el-row gutter="20" style="margin-bottom: 10px;">
                  <span class="data_name">总接口</span>
                </el-row>
                <el-row gutter="20" style="margin-bottom: 10px;">
                  <span class="data_num">{{apiCount}}</span>
                </el-row>
              </div>
            </el-col>
          </div>
        </el-col>

        <el-col :span="5">
          <div class="data_list">
            <el-col span="12">
              <div class="icon">
                <i class="el-icon-edit"></i>
              </div>
            </el-col>
            <el-col span="12">
              <div class="data_count">
                <el-row gutter="20" style="margin-bottom: 10px;">
                  <span class="data_name">总用例</span>
                </el-row>
                <el-row gutter="20" style="margin-bottom: 10px;">
                  <span class="data_num">{{caseCount}}</span>
                </el-row>
              </div>
            </el-col>
          </div>
        </el-col>

        <el-col :span="5">
          <div class="data_list">
            <el-col span="12">
              <div class="icon">
                <i class="el-icon-tickets"></i>
              </div>
            </el-col>
            <el-col span="12">
              <div class="data_count">
                <el-row gutter="20" style="margin-bottom: 10px;">
                  <span class="data_name">总任务</span>
                </el-row>
                <el-row gutter="20" style="margin-bottom: 10px;">
                  <span class="data_num">{{taskCount}}</span>
                </el-row>
              </div>
            </el-col>
          </div>
        </el-col>
      </el-row>
      <div class="opreation_helper">
        <div class="opreation_tips">
          <p4>操作小助手</p4>
        </div>
        <div class="opreation_step">
          <el-steps :active="1">
            <el-step title="步骤 1" description="建立一个项目和模块"></el-step>
            <el-step title="步骤 2" description="给项目建立一个运行环境"></el-step>
            <el-step title="步骤 3" description="建立一个接口"></el-step>
            <el-step title="步骤 4" description="建立一个用例"></el-step>
            <el-step title="步骤 5" description="新增一个收发邮箱"></el-step>
            <el-step title="步骤 6" description="新增一个定时任务"></el-step>
          </el-steps>
        </div>
      </div>
    <!-- </div> -->
  </div>
</template>
<script>
export default {
  data () {
    return {
      projectCount: '0',
      apiCount: '0',
      caseCount: '0',
      taskCount: '0'
    }
  }
}
</script>

<style lang="less" scoped>
.data_section {
  background-color:#F2F6FA;
  padding: 10px;
  margin-bottom: 30px;
  width: auto;
  height: 460px;
}
// .account{
//   background-color: rgb(231, 231, 227);
// }
.section_title {
  text-align: left;
  font-size: 30px;
  font-weight: bold;
  margin-bottom: 10px;
  color: #666666;

}
.ele-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  }
}
.data_list {
  // text-align: center;
  font-size: 14px;
  // color: #666;
  border-radius: 6px;
  // 圆角边框
  background: #FFFFFF;
  // width: 210px;
  height: 80px;
}
.data_count {
  // text-align: right;
  float: right;
  margin: 10px;
}
.data_name {
  color: #333;
  font-size: 14px;
  text-align: right;
}
.data_num {
  color: #333;
  font-size: 14px;
  font-weight: bolder;
  text-align: right;
}
.opreation_tips {
  text-align: left;
  font-weight: bold;
}
.icon {
  text-align: left;
  margin-top: 20px;
  &:last-child {
    color: #8ee9c4;
    font-size: 35px;
  }
}
</style>
