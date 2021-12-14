<template>

<div>
    <ul v-for="(color,i) in subset" :key="i">
        <ColorPanelButton :colorName=color :colorHex=i />
    </ul>
 </div>
</template>

<script>
import ColorPanelButton from './ColorPanelButton.vue'
export default {
  name: 'ColorPanelSubset',
  components: { ColorPanelButton },
  props: {
    subset: Object
  },
  methods: {
  }
}
</script>

<style scoped>

</style>
