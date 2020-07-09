<template>
  <div class="add_interface_page">

    <!-- <el-form ref="interfaceForm" :model="interfaceForm" label-width="80px"> -->
    <el-form :model="interfaceForm" :rules="rules" ref="interfaceForm" label-width="100px">
      <el-form-item label="接口名称">
        <el-input v-model="interfaceForm.name" class="input"></el-input>
      </el-form-item>
      <el-form-item label="接口路径">
        <el-input v-model="interfaceForm.path" class="input"></el-input>
      </el-form-item>
      <el-form-item label="所属项目">
        <el-select v-model="interfaceForm.project" placeholder="请选择所属项目" >
          <el-option label="渠道云" value="channelcloud"></el-option>
          <el-option label="友零售" value="retail"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="所属模块">
        <el-select v-model="interfaceForm.model" placeholder="请选择所属模块">
          <el-option label="b2b订单" value="b2b"></el-option>
          <el-option label="采购" value="purchase"></el-option>
          <el-option label="调拨" value="transer"></el-option>
          <el-option label="库存中心" value="stock"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="请求方式">
        <el-select v-model="interfaceForm.method" placeholder="请选择请求方式">
          <el-option label="get" value="get"></el-option>
          <el-option label="post" value="post"></el-option>
          <el-option label="put" value="put"></el-option>
          <el-option label="delete" value="delete"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="数据传输方式">
        <el-select v-model="interfaceForm.datatype" placeholder="请选择数据传输方式">
          <el-option label="form-data" value="form-data"></el-option>
          <el-option label="json" value="json"></el-option>
          <el-option label="parameter" value="parameter"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="是否需要签名">
        <el-switch v-model="interfaceForm.sign"></el-switch>
      </el-form-item>
      <el-form-item label="接口描述">
        <el-input type="textarea" v-model="interfaceForm.desc"></el-input>
      </el-form-item>
      <el-form-item label="header">
        <el-input type="textarea" v-model="interfaceForm.header"></el-input>
      </el-form-item>
      <el-form-item label="body">
        <el-input type="textarea" v-model="interfaceForm.body"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm('interfaceForm')">立即创建</el-button>
        <el-button>取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  data () {
    return {
      interfaceForm: {
        name: '',
        path: '',
        project: '',
        model: '',
        method: '',
        datatype: '',
        sign: false,
        desc: '',
        header: '',
        body: ''

      },
      rules: {
        name: [
          {required: true, message: '请输入接口名称', trigger: 'blur'},
          {min: 1, max: 30, message: '请输入1到30个字符', trigger: 'blur'}
        ],
        path: [
          {required: true, message: '请输入接口路径', trigger: 'blur'}
        ],
        method: [
          {required: true, message: '请选择请求方式', trigger: 'change'}
        ],
        datatype: [
          {required: true, message: '请选择请求参数类型', trigger: 'change'}
        ]
      }

    }
  },
  method: {
    submitForm (formName) {
      this.$refs[formName].validdata(valid => {
        if (valid) {
          alert('保存成功')
        } else {
          console.log('保存失败')
          return false
        }
      })
    }

  }
}
</script>

<style scoped>
.add_interface_page{
width: 620px;
}
</style>
