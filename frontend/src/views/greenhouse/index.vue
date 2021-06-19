<template>
  <div class="dashboard-editor-container">
    <panel-group @handleSetBarChartData="handleSetBarChartData" />
    
    <el-row style="background:#fff;padding:16px 16px 0;margin-bottom:32px;">
      <line-chart :chart-data="barChartData" />
    </el-row>

  </div>
</template>

<script>
import PanelGroup from './components/PanelGroup'
import LineChart from './components/LineChart'
import axios from 'axios'

export default {
  name: 'DashboardAdmin',
  components: {
    PanelGroup,
    LineChart
  },
  data() {
    return {
      barChartData: {
        hour: 1,
        expectedData: [],
        dim: '',
        color: '',
      }
    }
  },
  methods: {
    give_data(type, data) {
      var monthstr = (data.month[0]).toString();
      var datestr = monthstr.concat('月',(data.day[0]).toString());
      this.barChartData.hour = data.hour;
      switch(type){
      case 'temp':
        this.barChartData.expectedData = data.temp;
        this.barChartData.dim = datestr.concat('温度');
        this.barChartData.color = 'pink';
        break;
      case 'light_intensity':
        this.barChartData.expectedData = data.light_intensity;
        this.barChartData.dim = datestr.concat('光强');
        this.barChartData.color = 'blue';
        break;
      case 'CO_concentration':
        this.barChartData.expectedData = data.CO_concentration;
        this.barChartData.dim = datestr.concat('CO浓度');
        this.barChartData.color = 'green';
        break;
      case 'humidity':
        this.barChartData.expectedData = data.humidity;
        this.barChartData.dim = datestr.concat('湿度');
        this.barChartData.color = 'red';
        break;
      case 'soil_humidity':
        this.barChartData.expectedData = data.soil_humidity;
        this.barChartData.dim = datestr.concat('水分');
        this.barChartData.color = 'purple';
        break;
      case 'precipitation':
        this.barChartData.expectedData = data.precipitation;
        this.barChartData.dim = datestr.concat('降水量');
        this.barChartData.color = 'orange';
        break;
      }
    },// give_data
    handleSetBarChartData(type){
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/Monitor/get_envir_info/',
        responseType: 'json'
      })
      .then((response)=>(
        console.log(response.data),
        this.give_data(type, response.data)
      ))
    } // handleSetBarChartData
  }
}
</script>

<style lang="scss" scoped>
.dashboard-editor-container {
  padding: 32px;
  background-color: rgb(240, 242, 245);
  position: relative;

  .chart-wrapper {
    background: #fff;
    padding: 16px 16px 0;
    margin-bottom: 32px;
  }
}

@media (max-width:1024px) {
  .chart-wrapper {
    padding: 8px;
  }
}
</style>
