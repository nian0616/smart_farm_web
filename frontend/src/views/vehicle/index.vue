<template>
    <baidu-map class="map" :center="map.center" :zoom="map.zoom" @ready="handler">
        <!--缩放-->
        <bm-navigation anchor="BMAP_ANCHOR_TOP_LEFT"></bm-navigation>
        <!--定位-->
        <bm-geolocation anchor="BMAP_ANCHOR_BOTTOM_RIGHT" :showAddressBar="true" :autoLocation="true"></bm-geolocation>
        <!--点-->
        <bm-marker
            v-for="(marker,index) of markers"
            :key="index"
            :position="{lng: marker.lng, lat: marker.lat}"
            :icon="marker.markerIcon"
            @click="infoWindowOpen(index, marker)"
        >
            <bm-info-window
            :show="marker.show"
            @close="infoWindowClose(index, marker)"
            @open="infoWindowOpen(index, marker)"
            >
          <slot>{{marker.value}}</slot>
        </bm-info-window>
      </bm-marker>
    </baidu-map>
</template>
 
<script>
    export default {
        name: "vehicle",
        data: () => ({
            map:{
                center: {lng: 121.448615 , lat: 31.037968},
                zoom: 17,
                show: true,
                dragging: true
            },
            content:"",
            markers:[
                {
                lng: '121.448615',
                lat: '31.037968',
                value: '无人车1，运行状态良好'
                },
                {
                lng: '121.448015',
                lat: '31.037068',
                value: '无人车2，运行状态良好'
                },
                ]
        }),
          created () {
            this.markerAddAttr();
        },
        methods: {
            handler ({BMap, map}) {
                let me = this;
                console.log(BMap, map)
                // 鼠标缩放
                map.enableScrollWheelZoom(true);
                // 点击事件获取经纬度
                map.addEventListener('click', function (e) {
                    console.log(e.point.lng, e.point.lat)
                })
            },
            infoWindowOpen (index, marker) {//打开窗口
            marker.show = true;
            this.$set(this.markers, index, marker);
            this.$emit("on-change",marker);
            },
            infoWindowClose (index, marker) {//关闭窗口
            marker.show = false;
            this.$set(this.markers, index, marker);
            },
            markerAddAttr () {//添加默认值：标记点图标、show显示隐藏控制属性
            this.markers.map((item, index) => {
                item = Object.assign({
                ... !item.markerIcon && {markerIcon: {
                    url: 'http://api0.map.bdimg.com/images/marker_red_sprite.png', 
                    size: {
                        width: 30, 
                        height: 40
                    }
                    }
                },
                ... !item.show && {show: index>0?false: true},
                }, item);
                this.$set(this.markers, index, item);
            })
            },
        }
    }
</script>
 
<style scoped>
    .map {
        width: 100%;
        height: 100vh;
    }
</style>