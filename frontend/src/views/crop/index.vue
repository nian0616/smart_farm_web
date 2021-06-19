<template>
<div class="dashboard-editor-container">
  <!-- 界面装饰元素 -->
  <el-row class="demo-avatar demo-basic">
    <el-col :span="3" :offset="3">
      <div class="demo-basic--circle">
        <div class="block"><el-avatar :size="150" :src="require('@/assets/crop_images/01.jpg')"></el-avatar></div>
      </div>
    </el-col>
    <el-col :span="3" :offset="1">
      <div class="demo-basic--circle">
        <div class="block"><el-avatar :size="150" :src="require('@/assets/crop_images/10.jpg')"></el-avatar></div>
      </div>
    </el-col>
    <el-col :span="3" :offset="1">
      <div class="demo-basic--circle">
        <div class="block"><el-avatar :size="150" :src="require('@/assets/crop_images/03.jpg')"></el-avatar></div>
      </div>
    </el-col>
    <el-col :span="3" :offset="1">
      <div class="demo-basic--circle">
        <div class="block"><el-avatar :size="150" :src="require('@/assets/crop_images/02.jpg')"></el-avatar></div>
      </div>
    </el-col>
    <el-col :span="3" :offset="1">
      <div class="demo-basic--circle">
        <div class="block"><el-avatar :size="150" :src="require('@/assets/crop_images/09.jpg')"></el-avatar></div>
      </div>
    </el-col>
  </el-row>

  <!-- 上传文件和展示结果 -->
  <el-col :span="12" :offset="9">
    <el-upload
      class="upload-demo"
      drag
      action="http://127.0.0.1:8000/CropMaturity/upload/"
      multiple
      :show-file-list="false"
      :on-success="handleAvatarSuccess"
      >
      <img v-if="imageUrl" :src="imageUrl" class="avatar" id="uploadImage">
      <i v-else class="el-icon-upload"></i>
      <div class="el-upload__text">
        <em>拖曳</em>或<em>点击</em>上传无人车采集的图像
      </div>
    </el-upload>
  </el-col>

  <el-col :span="4" :offset="10">
    <el-card shadow="hover">
      <span id="maturity_rate"></span>
    </el-card>
  </el-col>
</div>

</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
    }
  },
  methods:{
    handleAvatarSuccess () {
      // handleAvatarSuccess: 上传文件成功后，向后端请求成熟度检测结果
      axios({
         method: 'get',
         url: 'http://127.0.0.1:8000/CropMaturity/test_maturity/',
       })
      .then((response)=>(
        console.log(response.data),
        document.getElementById('maturity_rate').innerText = "成熟率：" + response.data + "%"
      ))
    },
    beforeAvatarUpload (file) {
      // beforeAvatarUpload: 上传图片的操作，包括文件类型、大小检查等
      const isLt1M = file.size / 1024 / 1024 < 1
      if (!isLt1M) {
        this.$message.error('The size of the uploaded file cannot exceed 1MB!')
      }
      return sLt1M
    }
  }
}  
</script>

<style>
.img{
    margin-left:40px;
}
.el_card{
    padding: 0;
}

.avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  width: 350px;
  height: 150px;
}
.avatar-uploader .el-upload:hover {
  border-color: #409EFF;
}
.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  line-height: 178px;
  text-align: center;
}
.avatar {
  width: 360px;
  height: 180px;
  display: block;
}

.upload-demo{
  margin-top:50px;
}

.el-card{
  text-align: center;
  margin-top:50px;
}

.demo-basic--circle{
  margin-top:30px;
}

.dashboard-editor-container {
  padding: 32px;
  background-color: rgb(240, 242, 245);
  position: relative;
}

</style>