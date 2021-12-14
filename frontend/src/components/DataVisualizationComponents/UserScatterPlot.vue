<template>
  <svg viewBox='-5 0 95 200' ref='svgRef'>
  <defs>
    <linearGradient v-for='i in count' :key = 'i' :id='"gradient"+String(i)'
    gradientTransform="rotate(90)">
      <stop offset="0%"  :stop-color='backgroundGradient((i - 1) * 7).startGradient' />
      <stop offset="100%" :stop-color='backgroundGradient(i * 7).stopGradient' />
    </linearGradient>
  </defs>
  <rect v-for='i in count' :key= 'i'
  border='none'
  x=0 :y='backgroundGradient((i - 1) * 7).startY' width=100%
  height='8%'
  :fill='"url(#gradient"+String(i)+")"' />
  <!-- using my linear gradient -->
  <!-- <g>

  <rect x=0 y=0 width=100% height=100% fill="url('#myGradient')" />
  </g> -->
    <g class='x-axis' />
    <g class='y-axis'/>
  </svg>

</template>

<script>
import ColorFunctions from '@/services/color.functions.js'
import { useStore } from 'vuex'
import { onMounted, ref } from 'vue'
import {
  select,

  // line,
  scaleLinear,
  // min,
  // max,
  // curveBasis,
  axisBottom,
  axisLeft

} from 'd3'

export default {
  name: 'UserScatterPlot',
  props: {
    count: {
      type: Number
    },
    data: {
      required: true,
      type: Object
    },
    chosenVariables: {
      type: Array
    }
  },
  setup (props) {
    const svgRef = ref()
    useStore().dispatch('plotPage/retrieveUserColorChoices')
    const colors = useStore().state.plotPage.colorProfile

    function backgroundGradient (index) {
      if (index > 42) {
        if (props.chosenVariables[0] === 'calm') {
          return ColorFunctions.hexToInverseGradient(colors.anxiety, index)
        } else {
          return ColorFunctions.hexToInverseGradient(colors.sadness, index)
        }
      } else {
        return ColorFunctions.hexToInverseGradient(colors[props.chosenVariables[0]], index)
      }
    }
    onMounted(() => {
      const svg = select(svgRef.value)
      const t = svg.attr('viewBox').split(' ')
      var width = t[2]
      var height = t[3]

      const xScale = scaleLinear()
        .domain([0, props.data.count - 1])
        .range([0, width])

      const yScale = scaleLinear()
        .domain([-7, 7])
        .range([height, 0])

      function dotColor (dotData, variable) {
        if (dotData < 0) {
          if (variable === 'happiness') {
            return colors.sadness
          } else {
            return colors.anxiety
          }
        } else {
          if (variable === 'happiness') {
            return colors.happiness
          } else {
            return colors.calm
          }
        }
      }

      function drawCircle (dotData, v) {
        svg
          .selectAll('.circle')
          .data(dotData)
          .enter()
          .append('circle')
          .attr('fill', (d) => { return dotColor(d, v) })
          .attr('stroke', 'none')
          .attr('cx', (_, i) => { return xScale(i) })
          .attr('cy', (d) => { return yScale((d)) })
          .attr('r', 1)
      }
      const xAxis = axisBottom(xScale).tickValues([])

      for (const v of props.chosenVariables) {
        drawCircle(props.data[v], v)
      }

      svg
        .select('.x-axis')
        .style('transform', 'translateY(50%)')
        .call(xAxis)

      const yAxis = axisLeft(yScale)

      svg
        .select('.y-axis')
        .style('font-size', '4px')
      // .style('transform',`translateX(100px)`)
        .call(yAxis)
    })

    // return refs to make them available in template
    return { svgRef, backgroundGradient }
  }
}

</script>

<style scoped>

</style>
