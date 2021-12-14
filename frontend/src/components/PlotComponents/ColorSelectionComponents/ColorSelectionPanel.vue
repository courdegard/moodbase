<template>
<transition enter-active-class="animate__animated animate__fadeIn">
  <div >
  which color best describes {{currentVariable}}?
  <ListOfColors />
</div>
</transition>

</template>

<script>
// import PlotFunctions from '@/services/plot.functions.js'
import ListOfColors from './ListOfColors.vue'
export default {
  name: 'ColorSelectionPanel',
  components: { ListOfColors },
  computed: {
    currentVariable () {
      return this.$store.state.plotPage.panelState.variableSelectedForColorChange
    }
  },
  methods: {
  }
}
</script>

<style scoped>

div {
  width:100%;
  height:80%;
}

</style>
