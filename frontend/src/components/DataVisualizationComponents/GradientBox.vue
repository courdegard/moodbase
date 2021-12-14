<template>
<svg>
<g>
        <defs>
    <linearGradient id="boxGradient"
        x1=".0" y1="0"
        x2="0" y2="1"
        gradientUnits="objectBoundingBox">
        <stop offset="0" stop-color="pink"/>
        <stop offset="1" stop-color="pink" stop-opacity="0"/>
      </linearGradient>
        </defs>
    <rect y="10%" width="100%" height="100%" fill="url(#boxGradient)" />
  </g>
</svg>
</template>

<script>
export default {
  name: 'GradientBox'
  // props: {
  //   color:String,
}
</script>

<style>

</style>
