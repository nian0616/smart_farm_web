<template>
<div>
  <el-row :gutter="60" class="panel-group">
    <el-col :xs="16" :sm="16" :lg="8" class="card-panel-col">
      <div class="card-panel" @click="handleSetBarChartData('temp')">
        <div class="card-panel-icon-wrapper icon-people">
          <svg-icon icon-class="temp" class-name="card-panel-icon" />
        </div>
        <div class="card-panel-description">
          <div class="card-panel-text">
          温度
          </div>
        </div>
      </div>
    </el-col>
    <el-col :xs="16" :sm="16" :lg="8" class="card-panel-col">
      <div class="card-panel" @click="handleSetBarChartData('light_intensity')">
        <div class="card-panel-icon-wrapper icon-message">
          <svg-icon icon-class="light" class-name="card-panel-icon" />
        </div>
        <div class="card-panel-description">
          <div class="card-panel-text">
          光强 
          </div>
        </div>
      </div>
    </el-col>
    <el-col :xs="16" :sm="16" :lg="8" class="card-panel-col">
      <div class="card-panel" @click="handleSetBarChartData('CO_concentration')">
        <div class="card-panel-icon-wrapper icon-money">
          <svg-icon icon-class="gas" class-name="card-panel-icon" />
        </div>
        <div class="card-panel-description">
          <div class="card-panel-text">
          CO量
          </div>
        </div>
      </div>
    </el-col>
  </el-row>
  <el-row :gutter="60" class="panel-group">
    <el-col :xs="16" :sm="16" :lg="8" class="card-panel-col">
      <div class="card-panel" @click="handleSetBarChartData('humidity')">
        <div class="card-panel-icon-wrapper icon-people">
          <svg-icon icon-class="humidity" class-name="card-panel-icon" />
        </div>
        <div class="card-panel-description">
          <div class="card-panel-text">
          湿度
          </div>
        </div>
      </div>
    </el-col>
    <el-col :xs="16" :sm="16" :lg="8" class="card-panel-col">
      <div class="card-panel" @click="handleSetBarChartData('soil_humidity')">
        <div class="card-panel-icon-wrapper icon-message">
          <svg-icon icon-class="humidity_soil" class-name="card-panel-icon" />
        </div>
        <div class="card-panel-description">
          <div class="card-panel-text">
          水分
          </div>
        </div>
      </div>
    </el-col>
    <el-col :xs="16" :sm="16" :lg="8" class="card-panel-col">
      <div class="card-panel" @click="handleSetBarChartData('precipitation')">
        <div class="card-panel-icon-wrapper icon-money">
          <svg-icon icon-class="rain" class-name="card-panel-icon" />
        </div>
        <div class="card-panel-description">
          <div class="card-panel-text">
          降水量
          </div>
        </div>
      </div>
    </el-col>
  </el-row>
</div>
</template>

<script>
import CountTo from 'vue-count-to'

export default {
  components: {
    CountTo
  },
  methods: {
    handleSetBarChartData(type) {
      this.$emit('handleSetBarChartData', type)
    }
  },
}
</script>

<style lang="scss" scoped>
.panel-group {
  margin-top: 18px;

  .card-panel-col {
    margin-bottom: 32px;
  }

  .card-panel {
    height: 108px;
    cursor: pointer;
    font-size: 12px;
    position: relative;
    overflow: hidden;
    color: #666;
    background: #fff;
    box-shadow: 4px 4px 40px rgba(0, 0, 0, .05);
    border-color: rgba(0, 0, 0, .05);

    &:hover {
      .card-panel-icon-wrapper {
        color: #fff;
      }

      .icon-people {
        background: #40c9c6;
      }

      .icon-message {
        background: #36a3f7;
      }

      .icon-money {
        background: #f4516c;
      }

      .icon-shopping {
        background: #34bfa3
      }
    }

    .icon-people {
      color: #40c9c6;
    }

    .icon-message {
      color: #36a3f7;
    }

    .icon-money {
      color: #f4516c;
    }
    .card-panel-icon-wrapper {
      float: left;
      margin: 14px 0 0 14px;
      padding: 16px;
      transition: all 0.38s ease-out;
      border-radius: 6px;
    }

    .card-panel-icon {
      float: left;
      font-size: 48px;
    }

    .card-panel-description {
      float: right;
      font-weight: bold;
      margin: 40px 0 0 40px;

      .card-panel-text {
        float: left;
        line-height: 18px;
        color: rgba(0, 0, 0, 0.45);
        font-size: 23px;
        margin-right: 30px;
      }

      .card-panel-num {
        width: 80px;
        float: right;
        font-size: 23px;
        margin-right: 30px;
        line-height: 18px;
      }
    }
  }
}

@media (max-width:550px) {
  .card-panel-description {
    display: none;
  }

  .card-panel-icon-wrapper {
    float: none !important;
    width: 100%;
    height: 100%;
    margin: 0 !important;

    .svg-icon {
      display: block;
      margin: 14px auto !important;
      float: none !important;
    }
  }
}
</style>
