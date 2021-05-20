<template>
<el-button icon="el-icon-question" type="primary" @click="guide">
  Show Guide
</el-button>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Vehicle',
  methods: {
    guide() {
      console.log(1)
      axios.post('http://127.0.0.1:8000/FaceRecog/Hello/').then((res)=>(
        console.log(res.data)
      ))
    }
  }
}
</script>

