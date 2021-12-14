<template>
    <div class="py-4" >
        <h1 > The most popular colors for peoples' emotions right now... </h1>
        <ul  v-for="(dataPair,emotion) in popularColorData" :key="emotion" >
            <div @click="showDetails(emotion)">
                <div >{{emotion}}</div>
                <div :style="{'background-color':dataPair.mostPopularFamily}"> </div>
                <div >{{dataPair.popularityCount}}</div>
            </div>
        </ul>
        <h1 > Hover over a color for more detail </h1>
    </div>
</template>

<script>
import ColorFunctions from '@/services/color.functions.js'
export default {
  name: 'PopularColors',
  data () {
    return {
      popularColorData: {},
      popularityDetails: {}
    }
  },
  computed: {
    currentVariable () {
      return this.$store.state.currentMoodColors.variableSelection
    }
  },
  methods: {
    showDetails (emotion) {
      if (this.currentVariable !== emotion) {
        this.$store.dispatch('currentMoodColors/getPopularityData', emotion)
      }
      this.$store.commit('currentMoodColors/toggleDetailPanel', emotion)
    }
  },
  async beforeCreate () {
    this.popularColorData = await ColorFunctions.get('plot/popularcolors').then(response => response.json())
  }
}
</script>

<style>

</style>
