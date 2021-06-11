<template>
  <div class="dashboard-editor-container">
    <panel-group @handleSetLineChartData="handleSetLineChartData" />
    
    <el-row style="background:#fff;padding:16px 16px 0;margin-bottom:32px;">
      <line-chart :chart-data="lineChartData" />
    </el-row>

  </div>
</template>

<script>
import GithubCorner from '@/components/GithubCorner'
import PanelGroup from './components/PanelGroup'
import LineChart from './components/LineChart'
import RaddarChart from './components/RaddarChart'
import PieChart from './components/PieChart'
import BarChart from './components/BarChart'
import TransactionTable from './components/TransactionTable'
import TodoList from './components/TodoList'
import BoxCard from './components/BoxCard'

const lineChartData = {
  temp: {
    expectedData: [20.2, 22.1, 23.4, 24.5, 24.9, 25.3, 25.8],
    dim: '℃',
  },
  light: {
    expectedData: [50.2, 48.2, 49.3, 50.3, 48.2, 50.1, 52.8],
    dim: '%',
  },
  gas: {
    expectedData: [20.11, 18.23, 19.87, 19.99, 20.01, 18.93, 18.24],
    dim: '%',
  },
  humidity: {
    expectedData: [72, 64, 70, 65, 67, 72, 70],
    dim:'%',
  },
  humidity_soil: {
    expectedData: [0.44, 0.45, 0.42, 0.47, 0.44, 0.45, 0.46],
    dim:'%',
  },
  rain: {
    expectedData: [0.30, 0.33, 0.28, 0.28, 0.33, 0.33, 0.34],
    dim:'%',
  }
}

export default {
  name: 'DashboardAdmin',
  components: {
    GithubCorner,
    PanelGroup,
    LineChart,
    RaddarChart,
    PieChart,
    BarChart,
    TransactionTable,
    TodoList,
    BoxCard
  },
  data() {
    return {
      lineChartData: lineChartData.temp
    }
  },
  methods: {
    handleSetLineChartData(type) {
      this.lineChartData = lineChartData[type]
    }
  }
}
</script>

<style lang="scss" scoped>
.dashboard-editor-container {
  padding: 32px;
  background-color: rgb(240, 242, 245);
  position: relative;

  .github-corner {
    position: absolute;
    top: 0px;
    border: 0;
    right: 0;
  }

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
