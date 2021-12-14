<template>
<div id="panel">

    <ul  v-for="(colorCategory,colorName) in listOptions" :key="colorName" >
        <div :style="{'color':colorName}" @click="enterSubsetLayer(colorName)"
        v-if="currentSubset===''">  {{ colorName }} </div>
        <ColorPanelSubset v-if="currentSubset===colorName" :subset="colorCategory" />
    </ul>
 </div>
</template>

<script>
import ColorFunctions from '@/services/color.functions.js'
import ColorPanelSubset from './ColorPanelSubset.vue'
export default {
  name: 'ListOfColors',
  data () {
    return {
      listOptions: {}
    }
  },
  created () {
    this.loadList()
  },
  components: { ColorPanelSubset },
  computed: {
    currentSubset () {
      return this.$store.state.plotPage.panelState.inPanelSubset
    }
  },
  methods: {
    loadList () {
      ColorFunctions.get('plot/listofcolors')
        .then(res => res.json())
        .then(data => { this.listOptions = data })
    },
    enterSubsetLayer (layerToEnter) {
      this.$store.commit('plotPage/setColorSubset', layerToEnter)
    }
  }

}
</script>

<style>
#panel {
  height: 40%;
  width:100%;
  overflow-y: scroll;
  scrollbar-width:none;

}
::-webkit-scrollbar {
    display: none;
}
</style>
