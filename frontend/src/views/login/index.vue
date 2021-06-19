<script src="https://cdn.staticfile.org/vue-resource/1.5.1/vue-resource.min.js"></script>
<template>
  <div class="login-container">
    <el-form ref="loginForm" :model="loginForm" :rules="loginRules" class="login-form" autocomplete="on" label-position="left">

      <div class="title-container">
        <h3 class="title">Modern Agricultural IOT System</h3>
      </div>
      <el-button :loading="loading" type="primary" style="width:100%;margin-bottom:30px;" @click.native.prevent="handleLogin">Login</el-button>

      <div style="position:relative">
        <el-button class="thirdparty-button" type="primary" style="width:100%;" @click="showDialog=true">
          Register
        </el-button>
      </div>
      <h1> </h1>
    </el-form>

    <el-dialog id= "register_id" title="Register" :visible.sync="showDialog">
      <div style ="float:left;size:90px;color:black;margin:10px;">your id:</div>
      <input type="text" v-model="msg">
      <div id = "fp2" v-if = "judge">
        <div style = "float:left;position:absolute;color:black;top:100px;left:10px;">your photo:</div>
        <img :src = "'data:image/png;base64,'+imgStr" alt="图片未上传" style="width:200px;height:200px;margin:10px;" id = "img">
      </div>
      <el-button :loading="loading" type="primary" style="width:35%;margin-bottom:10px;margin-left:10px;" @click.native.prevent="submit" v-if = "judge2">submit</el-button>
      <div style = "margin-left:10px;color:red;font-weight:bold">{{msg2}}</div>
    </el-dialog>
  </div>
</template>

<style>
  #register_id .el-dialog__body{
    padding-top: 0px;
    padding-left: 15px;
    padding-bottom: 18px;
  }
</style>

<script>
import { validUsername } from '@/utils/validate'
import SocialSign from './components/SocialSignin'
const axios = require('axios')
export default {
  name: 'Login',
  components: { SocialSign },
  data() {
    const validateUsername = (rule, value, callback) => {
      if (!validUsername(value)) {
        callback(new Error('Please enter the correct user name'))
      } else {
        callback()
      }
    }
    const validatePassword = (rule, value, callback) => {
      if (value.length < 6) {
        callback(new Error('The password can not be less than 6 digits'))
      } else {
        callback()
      }
    }
    return {
      loginForm: {
        username: 'admin',
        password: '111111'
      },
      loginRules: {
        username: [{ required: true, trigger: 'blur', validator: validateUsername }],
        password: [{ required: true, trigger: 'blur', validator: validatePassword }]
      },
      passwordType: 'password',
      capsTooltip: false,
      loading: false,
      showDialog: false,
      redirect: undefined,
      otherQuery: {},
      msg:'',
      msg2:'',
      imgStr:'',
      judge:false,
      judge2:true
    }
  },
  watch: {
    $route: {
      handler: function(route) {
        const query = route.query
        if (query) {
          this.redirect = query.redirect
          this.otherQuery = this.getOtherQuery(query)
        }
      },
      immediate: true
    }
  },
  mounted() {
    if (this.loginForm.username === '') {
      this.$refs.username.focus()
    } else if (this.loginForm.password === '') {
      this.$refs.password.focus()
    }
  },
  methods: {
    checkCapslock(e) {
      const { key } = e
      this.capsTooltip = key && key.length === 1 && (key >= 'A' && key <= 'Z')
    },
    showPwd() {
      if (this.passwordType === 'password') {
        this.passwordType = ''
      } else {
        this.passwordType = 'password'
      }
      this.$nextTick(() => {
        this.$refs.password.focus()
      })
    },
    submit(){
      this.loading = true
      var dtback = -1
      var dtimg = ""
      var fp = document.getElementById("fp2")
      console.log(fp)
      if (this.msg==="") {
        this.loading = false
        this.msg2 = "your id shouldn't be blank."
      }
      else {
      axios({
        url:'http://localhost:8000/FaceRecog/register/',
        method:'get',
        params:{'id':this.msg}
      })
      .then(function (response){
          dtback = response.data[0].value
          dtimg = response.data[0].pic.toString()
          console.log(dtimg)
        }).catch(function(error){
          console.log(error);
        });
      setTimeout(() => {
        this.loading = false
        if (dtback === 1) {
          this.judge = true
          this.judge2 =false
          this.imgStr = dtimg.slice(0,-1)
          this.msg2 = "register succeed! website will redirect in five seconds."
          setTimeout(() => {
            location.reload()
          }, 5000);
        }
        else {
          this.msg2 = "register failed! Please try again."
        }
      }, 2000);
      }
    },
    handleLogin() {
      var facetoken
      facetoken = -1
      this.loginForm.username = 'false'
      this.loading = true
      var fun1 = async function(){
      await axios.get('http://localhost:8000/FaceRecog/login/').
      then(function (response){
        //console.log(response.data[0].value)
        if (response.data[0].value === 1) facetoken = 1
        else facetoken = 0
        //console.log(facetoken)
        }).catch(function(error){
        console.log(error);
        });
      }
      var fun2 = async function(){
        await fun1()
      }
      // fun2()
      facetoken = 1
      setTimeout(() => {
      if (facetoken === 1) { this.loginForm.username = 'admin' }
      this.$store.dispatch('user/login', this.loginForm)
        .then(() => {
          this.$router.push({ path: this.redirect || '/', query: this.otherQuery })
          this.loading = false
        })
        .catch(() => {
          this.loading = false
        })
      return true
      }, 2000);
    },
    getOtherQuery(query) {
      return Object.keys(query).reduce((acc, cur) => {
        if (cur !== 'redirect') {
          acc[cur] = query[cur]
        }
        return acc
      }, {})
    }
  }
}
</script>

<style lang="scss">
/* 修复input 背景不协调 和光标变色 */
/* Detail see https://github.com/PanJiaChen/vue-element-admin/pull/927 */

$bg:#283443;
$light_gray:#fff;
$cursor: #fff;

@supports (-webkit-mask: none) and (not (cater-color: $cursor)) {
  .login-container .el-input input {
    color: $cursor;
  }
}

/* reset element-ui css */
.login-container {
  .el-input {
    display: inline-block;
    height: 47px;
    width: 85%;

    input {
      background: transparent;
      border: 0px;
      -webkit-appearance: none;
      border-radius: 0px;
      padding: 12px 5px 12px 15px;
      color: $light_gray;
      height: 47px;
      caret-color: $cursor;

      &:-webkit-autofill {
        box-shadow: 0 0 0px 1000px $bg inset !important;
        -webkit-text-fill-color: $cursor !important;
      }
    }
  }

  .el-form-item {
    border: 1px solid rgba(255, 255, 255, 0.1);
    background: rgba(0, 0, 0, 0.1);
    border-radius: 5px;
    color: #454545;
  }
}
</style>

<style lang="scss" scoped>
$bg:#2d3a4b;
$dark_gray:#889aa4;
$light_gray:#eee;

.login-container {
  min-height: 100%;
  width: 100%;
  background-color: $bg;
  overflow: hidden;

  .login-form {
    position: relative;
    width: 520px;
    max-width: 100%;
    padding: 160px 35px 0;
    margin: 0 auto;
    overflow: hidden;
  }

  .tips {
    font-size: 14px;
    color: #fff;
    margin-bottom: 10px;

    span {
      &:first-of-type {
        margin-right: 16px;
      }
    }
  }

  .svg-container {
    padding: 6px 5px 6px 15px;
    color: $dark_gray;
    vertical-align: middle;
    width: 30px;
    display: inline-block;
  }

  .title-container {
    position: relative;

    .title {
      font-size: 26px;
      color: $light_gray;
      margin: 0px auto 40px auto;
      text-align: center;
      font-weight: bold;
    }
  }

  .show-pwd {
    position: absolute;
    right: 10px;
    top: 7px;
    font-size: 16px;
    color: $dark_gray;
    cursor: pointer;
    user-select: none;
  }

  .thirdparty-button {
    position: absolute;
    right: 0;
    bottom: -15px;
  }

  @media only screen and (max-width: 470px) {
    .thirdparty-button {
      display: none;
    }
  }
}
</style>
