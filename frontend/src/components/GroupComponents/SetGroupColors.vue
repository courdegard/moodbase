<template>
<div class="flexc">
  <div class="flexr">
      <button @click="confirmChanges"> Use my colors </button>
      <button @click="changeColors"> Make changes </button>
      <button v-if='showConfirmationButton' @click="confirmChanges"> Use these colors </button>

  </div>
  <div class="flexr">
    <plot-grid-4 />
    <plot-color-picker v-if='newColors'/>
    <color-selection-panel v-if="currentVariable!=''"  />
  </div>
</div>
</template>

<script>
import ColorSelectionPanel from '../PlotComponents/ColorSelectionComponents/ColorSelectionPanel.vue'
import PlotColorPicker from '../PlotComponents/ColorSelectionComponents/PlotColorPicker.vue'
import PlotGrid4 from '../PlotComponents/GridComponents/PlotGrid4.vue'
export default {
  name: 'SetGroupColors',
  components: {
    PlotGrid4,
    PlotColorPicker,
    ColorSelectionPanel
  },
  data () {
    return {
      newColors: false
    }
  },
  methods: {
    changeColors () {
      this.newColors = !this.newColors
    },
    confirmChanges () {
      this.$store.commit('groupCreator/nextForm', { nextFormName: 'setWeights', formValues: this.colorData })
    }
  },
  beforeMount () {
    this.$store.commit('plotPage/setDisplayToggleIncrementValue', 2)
  },
  computed: {
    colorData () {
      return this.$store.state.plotPage.colorProfile
    },
    showConfirmationButton () {
      return this.$store.state.groupCreator.confirmColorChange
    },
    currentVariable () {
      return this.$store.state.plotPage.panelState.variableSelectedForColorChange
    }
  }
}
</script>

<style>

</style>
