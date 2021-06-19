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
    LineChart,
  },
  data() {
    return {
      barChartData: {
        name: [],
        expectedData: [],
        dim: '',
        color: ''
      }
    }
  },

  methods: {
    give_data(type, data) {
      this.barChartData.name = data.name;
      switch(type){
      case 'price':
        this.barChartData.expectedData = data.price;
        this.barChartData.dim = '农作物价格/元';
        this.barChartData.color = 'pink';
        break;
      case 'change_num':
        this.barChartData.expectedData = data.change_num;
        this.barChartData.dim = '涨跌数值/%';
        this.barChartData.color = 'blue';
        break;
      case 'change_ratio':
        this.barChartData.expectedData = data.change_ratio;
        this.barChartData.dim = '涨跌幅度/%';
        this.barChartData.color = 'green';
        break;
      case 'trading_volumes':
        this.barChartData.expectedData = data.trading_volumes;
        this.barChartData.dim = '成交量';
        this.barChartData.color = 'red';
        break;
      }
    }, //give_data
    handleSetBarChartData(type){
      // handleSetBarChartData：向后端数据库请求数据
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/ProdInfo/get_data/',
        responseType: 'json'
      })
      .then((response)=>(
        this.give_data(type, response.data)
      ))
    } // handleSetBarChartData
  },
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
