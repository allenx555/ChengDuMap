<template>
  <div>
    <div class="register-wrapper">
      <div id="register">
        <p class="title">登录</p>
        <el-form
          :model="ruleForm2"
          status-icon
          :rules="rules2"
          ref="ruleForm2"
          label-width="0"
          class="demo-ruleForm"
        >
          <el-form-item prop="tel">
            <el-input
              v-model="ruleForm2.tel"
              auto-complete="off"
              placeholder="请输入手机号"
            ></el-input>
          </el-form-item>
          <el-form-item prop="smscode" class="code">
            <el-input
              v-model="ruleForm2.smscode"
              :disabled="true"
              placeholder="验证码"
            ></el-input>
            <el-button type="primary" :disabled="true" @click="sendCode">{{
              buttonText
            }}</el-button>
          </el-form-item>
          <el-form-item prop="pass">
            <el-input
              type="password"
              v-model="ruleForm2.pass"
              auto-complete="off"
              placeholder="输入密码"
            ></el-input>
          </el-form-item>
          <el-form-item>
            <el-button
              type="primary"
              @click="submitForm('ruleForm2')"
              style="width:100%;"
              >登陆</el-button
            >
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script>
import { APIClient } from "../utils/client.js"

export default {
  name: "Login",
  data() {
    // <!--验证手机号是否合法-->
    let checkTel = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入手机号码"))
        //   } else if (!this.checkMobile(value)) {
        //     callback(new Error("手机号码不合法"))
      } else {
        callback()
      }
    }
    //  <!--验证码是否为空-->
    // let checkSmscode = (rule, value, callback) => {
    //   if (value === "") {
    //     callback(new Error("请输入手机验证码"))
    //   } else {
    //     callback()
    //   }
    // }
    // <!--验证密码-->
    let validatePass = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入密码"))
      } else {
        callback()
      }
    }
    return {
      ruleForm2: {
        pass: "",
        tel: ""
        // smscode: ""
      },
      rules2: {
        pass: [{ validator: validatePass, trigger: "change" }],
        tel: [{ validator: checkTel, trigger: "change" }]
        // smscode: [{ validator: checkSmscode, trigger: "change" }]
      },
      buttonText: "发送验证码",
      isDisabled: true, // 是否禁止点击发送验证码按钮
      flag: true
    }
  },
  methods: {
    // <!--发送验证码-->
    sendCode() {
      let tel = this.ruleForm2.tel
      if (this.checkMobile(tel)) {
        let time = 60
        this.buttonText = "已发送"
        this.isDisabled = true
        if (this.flag) {
          this.flag = false
          let timer = setInterval(() => {
            time--
            this.buttonText = time + " 秒"
            if (time === 0) {
              clearInterval(timer)
              this.buttonText = "重新获取"
              this.isDisabled = false
              this.flag = true
            }
          }, 1000)
        }
      }
    },
    submitForm(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          APIClient.post("/login", {
            phone: this.ruleForm2["tel"],
            password: this.ruleForm2["pass"]
          })
            .then(response => {
              this.$store.commit("setToken", response)
              this.$router.push({
                path: "/"
              })
            })
            .catch(error => {
              this.setState({
                errored: true
              })
              console.log("响应失败:", error)
            })
        } else {
          console.log("error submit!!")
          return false
        }
      })
    },
    // <!--进入登录页-->
    gotoLogin() {
      this.$router.push({
        path: "/login"
      })
    },
    // 验证手机号
    checkMobile(str) {
      let re = /^1\d{10}$/
      if (re.test(str)) {
        return true
      } else {
        return false
      }
    }
  }
}
</script>

<style scoped>
.loading-wrapper {
  position: fixed;
  top: 0;
  right: 0;
  left: 0;
  bottom: 0;
  background: #aedff8;
  display: flex;
  align-items: center;
  justify-content: center;
}
.register-wrapper img {
  position: absolute;
  z-index: 1;
}
.register-wrapper {
  position: fixed;
  top: 0;
  right: 0;
  left: 0;
  bottom: 0;
}
#register {
  max-width: 340px;
  margin: 60px auto;
  background: #fff;
  padding: 20px 40px;
  border-radius: 10px;
  position: relative;
  z-index: 9;
}
.title {
  font-size: 26px;
  line-height: 50px;
  font-weight: bold;
  margin: 10px;
  text-align: center;
}
.el-form-item {
  text-align: center;
}
.login {
  margin-top: 10px;
  font-size: 14px;
  line-height: 22px;
  color: #1ab2ff;
  cursor: pointer;
  text-align: left;
  text-indent: 8px;
  width: 160px;
}
.login:hover {
  color: #2c2fd6;
}
.code >>> .el-form-item__content {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.code button {
  margin-left: 20px;
  width: 140px;
  text-align: center;
}
.el-button--primary:focus {
  background: #409eff;
  border-color: #409eff;
  color: #fff;
}
</style>
