<template>
<div>
<br>
<br>
<div class="flexrp">
  <transition enter-active-class="animate__animated animate__slideInUp fast">

  <div class="flexc">
    <PlotColorPicker  v-if="quadrantSelected==='none'" />

    <color-selection-panel v-if="currentVariable!=''"  />

  </div>
  </transition>

  <div class="center">
      <PlotGrid4 />
    </div>
</div>
</div>
</template>

<script>
import ColorSelectionPanel from '@/components/PlotComponents/ColorSelectionComponents/ColorSelectionPanel.vue'
import PlotGrid4 from '@/components/PlotComponents/GridComponents/PlotGrid4.vue'
import PlotColorPicker from '@/components/PlotComponents/ColorSelectionComponents/PlotColorPicker.vue'

export default {
  name: 'PlotPage',
  beforeCreate () {
    this.$store.commit('plotPage/setDisplayToggleIncrementValue', 1)
  },
  components: {
    ColorSelectionPanel,
    PlotGrid4,
    PlotColorPicker
  },
  computed: {
    quadrantSelected () {
      return this.$store.state.plotPage.activeQuadrant
    },
    currentVariable () {
      return this.$store.state.plotPage.panelState.variableSelectedForColorChange
    }
  }
}
</script>

<style>

.flexrp{
  position:fixed;
  transform: translate(30%, 0);
  display:flex;
  margin:0;
  padding:0;
  flex-direction:row;
  overflow:visible;
}

.center {
  transform: translate(50%, 0);
  position:fixed;
  margin: auto;
  width: 50vw;
  height: 50vw;
  /* border: 3px solid gray; */
}

/* .flexc{
  display:flex;
  margin:0;
  padding:0;
  flex-direction:column;
} */
</style>
