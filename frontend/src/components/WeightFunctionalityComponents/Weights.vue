<template>
<svg height='40%' width='40%' viewBox='-100 -100 225 225 ' ref='weightCanvas'>
  <circle cx='0' cy='0' r="1%"/>

<!-- <path :d='reactivePath1'
  style="stroke: #ff0000;
          stroke-width: 3;
          fill: none;
          "
/> -->
<WeightDot v-for='i in propsToPass.numPoints' :key='i'
 :iter='i' :buttName='propsToPass.buttNames[i - 1]' />
</svg>
</template>

<script>
import { mapGetters } from 'vuex'
import WeightDot from './WeightDot.vue'
export default {
  name: 'Weights',
  components: {
    WeightDot
  },
  data () {
    return {
      interval: null
    }
  },
  computed: {
    ...mapGetters({
      propsToPass: 'butts/dataForDotRendering'
    })
  }
}
</script>

<style>

</style>
