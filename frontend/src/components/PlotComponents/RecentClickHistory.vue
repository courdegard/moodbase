<template>
  <div id="clickHistory" >
    <ul v-for="(dataPoint,i) in allData" :key="i">
    On {{dataPoint.timeStamp}}, you were feeling
    {{dataPoint.happiness.severity}} {{dataPoint.happiness.mood}} and
    {{dataPoint.calm.severity}} {{dataPoint.calm.mood}}
    </ul>
  </div>
</template>

<script>
import VisualizationService from '@/services/visualization.service'
import { reactive } from 'vue'

export default {
  name: 'RecentClickHistory',
  data () {
    return {
      bottom: false,
      mostRecentEight: reactive([]),
      allData: reactive([]),
      beginSlice: 0,
      endSlice: 0,
      uid: '',
      previousHeight: 0
    }
  },
  computed: {
    addPointToList () {
      return this.$store.state.plotData.newPoint
    }
  },
  watch: {
    addPointToList: function (pointVal) {
      this.allData.unshift(pointVal)
      this.beginSlice = this.beginSlice + 1
      this.endSlice = this.endSlice + 1
      this.mostRecentEight = this.allData.slice(this.beginSlice, this.endSlice)
    }
  },
  // methods: {
  //     loadData(e){
  //         const {target}=e;
  //         console.log(target.scrollTop)
  //         console.log(target.scrollHeight)
  //         console.log(target.offsetHeight)
  //     },
  // },
  async mounted () {
    // happy is z and calm is y
    this.uid = this.$store.state.auth.user.id
    this.allData = await VisualizationService.getAndClassifyClickHistory(this.uid)
    this.allData = this.allData.slice().reverse()
    this.endSlice = this.allData.length - 1
    this.beginSlice = this.endSlice - 9
    this.mostRecentEight = this.allData.slice(this.beginSlice, this.endSlice)
  }
}
</script>

<style>
#clickHistory{
  height: 190px;
  width:600px;
  overflow-y: scroll;
}
</style>
