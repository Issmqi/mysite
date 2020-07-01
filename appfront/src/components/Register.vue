<template>
    <div class="register-wrap">
        <ele-form class="register-continer">
            <h1 class="用户注册"></h1>
            <el-form-item label="用户名">
                <el-input type="text" v-model="username" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="密码">
                <el-input type="password" v-model="password" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" style="width:100%;" @click="doSubmit()">注册</el-button>
            </el-form-item>
        </ele-form>
    </div>
</template>