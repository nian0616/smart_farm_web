<template>
    <div>
    <el-row :gutter="60">
      <el-col :span="12">
        <el-card class="box-card">
          <div>
            <img :src="require('@/assets/crop_images/06.jpg')">
          </div>
          <div slot="header" class="clearfix">
            <span style="margin-left:250px;font-size:20px">成熟率：5%</span>
          </div>
        </el-card>
      </el-col>
      <el-col :span="12">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span style="margin-left:250px;font-size:20px">成熟率：90%</span>
          </div>
          <div>
            <img :src="require('@/assets/crop_images/02.jpg')">
          </div>
        </el-card>
      </el-col>
    </el-row>
    </div>

</template>

<script>
export default {
  data() {
    return {
    }
  }
}  
</script>

<style>
.img{
    margin-left:40px;
    /* width: 300px;
    height: 150px; */
}
.el_card{
    padding: 0;
}
</style>