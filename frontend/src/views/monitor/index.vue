<template>
<div class="dashboard-editor-container">
  <el-row :gutter="60">
    <el-col :span="12">
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span style="font-size:20px">监控点1</span>
        </div>
        <div>
          <img :src="require('@/assets/monitor_videos/monitor_05.gif')">
        </div>
      </el-card>
    </el-col>
    <el-col :span="12">
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span style="font-size:20px">监控点2</span>
        </div>
        <div>
          <img :src="require('@/assets/monitor_videos/monitor_06.gif')">
        </div>
      </el-card>
    </el-col>
  </el-row>

  <el-row :gutter="60">
    <el-col :span="12">
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span style="font-size:20px">监控点3</span>
        </div>
        <div>
          <img :src="require('@/assets/monitor_videos/monitor_07.gif')">
        </div>
      </el-card>
    </el-col>
    <el-col :span="12">
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span style="font-size:20px">监控点4</span>
        </div>
        <div>
          <img :src="require('@/assets/monitor_videos/monitor_08.gif')">
        </div>
      </el-card>
    </el-col>
  </el-row>

  <el-row :gutter="60">
    <el-col :span="12">
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span style="font-size:20px">温室监控</span>
        </div>
        <div>
          <img :src="require('@/assets/monitor_videos/monitor_01.gif')">
        </div>
      </el-card>
    </el-col>
    <el-col :span="12">
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span style="font-size:20px">采摘苹果</span>
        </div>
        <div>
          <img :src="require('@/assets/monitor_videos/monitor_02.gif')">
        </div>
      </el-card>
    </el-col>
  </el-row>

  <el-row :gutter="60">
    <el-col :span="12">
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span style="font-size:20px">种子培育</span>
        </div>
        <div>
          <img :src="require('@/assets/monitor_videos/monitor_03.gif')">
        </div>
      </el-card>
    </el-col>
    <el-col :span="12">
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span style="font-size:20px">无水栽培</span>
        </div>
        <div>
          <img :src="require('@/assets/monitor_videos/monitor_04.gif')">
        </div>
      </el-card>
    </el-col>
  </el-row> 
 </div>
</template>

<script>
</script>

<style>
.img{
    display: inline-block;
    margin-left:40px;
}
.el_card{
    padding: 0;
}

.dashboard-editor-container {
  padding: 32px;
  background-color: rgb(240, 242, 245);
  position: relative;
}

.el-row{
  margin-bottom: 30px;
}

</style>