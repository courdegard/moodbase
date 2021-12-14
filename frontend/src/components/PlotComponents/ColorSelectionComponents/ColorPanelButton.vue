<template>
<div :style="classVar">
  <button @click="changeColor">
      <span  :style="{'color':colorHex}"> {{colorName}}</span></button>
</div>

</template>

<script>
export default {
  name: 'ColorPanelButton',
  props: {
    colorName: String,
    colorHex: String
  },
  computed: {
    classVar () {
      return { '--color': this.colorHex }
    },
    variableName () {
      return this.$store.state.plotPage.panelState.variableSelectedForColorChange
    }
  },
  methods: {
    changeColor () {
      this.$store.commit('plotPage/holdColorChange', this.colorHex)
    }
  }

}
</script>
<style scoped>
#colorbutton{
    display:flex;
    justify-content:center;
    height:40px;
    width:40px;
    background-color:var(--color);
}

</style>
