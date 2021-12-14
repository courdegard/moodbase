<template>
  <circle @mousedown='beginUpdate' :id='iter' :cx='x' :cy='y' r="1%"/>
</template>

<script>
import { useStore } from 'vuex'
export default {
  name: 'WeightDot',
  props: {
    iter: Number,
    buttName: String
  },
  setup (props) {
    var interval = null
    const store = useStore()
    const nGon = store.getters['butts/dataForDotRendering'].numPoints
    const sign = {
      x: 1,
      y: 1
    }
    const theta = ((props.iter) * ((Math.PI * 2) / (nGon)))
    if (theta < Math.PI / 2 && theta > Math.PI * 3 / 2) {
      sign.x = -1
    }
    if (theta < Math.PI && theta > 2 * Math.PI) {
      sign.y = -1
    }
    const x = 100 * sign.x * Math.cos((props.iter * ((Math.PI * 2) / nGon)))
    const y = 100 * sign.x * Math.sin((props.iter * ((Math.PI * 2) / nGon)))
    function beginUpdate () {
      interval = window.setInterval(() => {
        store.commit('butts/drawPath', props.nGon)
      })
    }
    return { x, y, beginUpdate, interval }
  }
}
</script>

<style>

</style>
