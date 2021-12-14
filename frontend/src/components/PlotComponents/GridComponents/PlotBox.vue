<template>
  <div @click="collectPlotData($event)" :style="gradients" />
</template>

<script>
// box we will be using to collect data from click

import PlotFunctions from '@/services/plot.functions.js'
import ColorFunctions from '@/services/color.functions.js'
import _ from 'lodash'

export default {
  name: 'PlotBox',
  computed: {

    quadrantData () {
      return this.$store.getters['plotPage/organizeColorsByQuadrant']
    },
    gradients () {
      return {
        '--h': 'linear-gradient(to ' + this.xDir + this.xColor + ', transparent)',
        '--v': 'linear-gradient(to ' + this.yDir + this.yColor + ', transparent)'
      }
    },
    xColor () {
      const baseColor = this.$store.state.plotPage.colorProfile[this.quadrantData.x]
      return ColorFunctions.createGradientString(baseColor, [7, 100]) + baseColor + ' 100%'
    },
    yColor () {
      const baseColor = this.$store.state.plotPage.colorProfile[this.quadrantData.y]
      return ColorFunctions.createGradientString(baseColor, [7, 100]) + baseColor + ' 100%'
    },
    xDir () {
      if (this.quadrantData.number === 'one' || this.quadrantData.numberr === 'three') {
        return 'left, '
      } else {
        return 'right, '
      }
    },
    yDir () {
      if (this.quadrantData.number === 'one' || this.quadrantData.number === 'two') {
        return 'top, '
      } else {
        return 'bottom, '
      }
    }
  },
  methods: {
    collectPlotData (e) {
      const transformed = PlotFunctions.coordinateTransform(e, this.quadrantData.number)
      const payload = {
        happiness: transformed.happinessVal,
        calm: transformed.calmVal,
        mapX: Math.round(PlotFunctions.maplerize(transformed.happinessVal, 'x')),
        mapY: Math.round(PlotFunctions.maplerize(transformed.calmVal, 'y')),
        timerange: PlotFunctions.determineTimeRange()
      }
      // this.$store.commit('userData/addNewClick', payload)
      PlotFunctions.post(payload, 'plot/getplotclick')
    },

    throttleClick: _.throttle(function (e) { this.collectPlotData(e) }, 1000)
  }
}
</script>

<style scoped>

div {
  background: var(--h), var(--v);
  position:absolute;
  width:90%;
  height:90%;
  z-index:10;
  background-blend-mode: multiply;

}
</style>
