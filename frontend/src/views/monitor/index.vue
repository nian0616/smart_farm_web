<template>
    <div>
    <el-row :gutter="60">
      <el-col :span="12">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span style="margin-left:250px;font-size:20px">温室监控</span>
          </div>
          <div>
            <img :src="require('@/assets/monitor_videos/monitor_01.gif')">
          </div>
        </el-card>
      </el-col>
      <el-col :span="12">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span style="margin-left:250px;font-size:20px">采摘苹果</span>
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
            <span style="margin-left:250px;font-size:20px">种子培育</span>
          </div>
          <div>
            <img :src="require('@/assets/monitor_videos/monitor_03.gif')">
          </div>
        </el-card>
      </el-col>
      <el-col :span="12">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span style="margin-left:250px;font-size:20px">无水栽培</span>
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
// export default {
//   data() {
//     return {
//       imgUrl:require('@/assets/monitor_videos/monitor_01.gif')
//     }
//   },
//   methods: {
//     give_data(type, data) {
//           this.barChartData.name = data.name;
//     },
//     handleSetBarChartData(type){
//       axios({
//          method: 'get',
//          url: 'http://127.0.0.1:8000/get_videos/',
//          responseType: 'json'
//        })
//       .then((response)=>(
//         console.log(response.data),
//         this.give_data(type, response.data)
//       ))
//     }
//   },
// }  
</script>

<style>
.img{
    display: inline-block;
    margin-left:40px;
}
.el_card{
    padding: 0;
}
</style>