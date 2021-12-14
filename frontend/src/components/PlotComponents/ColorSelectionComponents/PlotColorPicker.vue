<template>
<div class="flexcl">
  <span> Your colors </span>
    <color-text-element variable="happiness" />
    <color-text-element variable="sadness" />
    <color-text-element variable="calm" />
    <color-text-element variable="anxiety" />
</div>
</template>

<script>
import ColorTextElement from './ColorTextElement.vue'
export default {
  name: 'PlotColorPicker',
  components: { ColorTextElement }
}
</script>

<style>

.flexcl{
  display:flex;
  transform: translate(15%, 0);
  flex-direction:column;
  width:20vw;
}

</style>
