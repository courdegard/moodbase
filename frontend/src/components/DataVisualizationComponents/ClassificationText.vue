<template>
     <div>
          <span> {{emotionSeverity}} {{emotionStatus}} </span>
    </div>
    <svg width=250 height=50>
        <rect :fill="emotionColor.color" width=250 height=50 />
    </svg>

</template>

<script>
import { useStore } from 'vuex'
import { onUpdated, reactive } from 'vue'
export default {
  name: 'ClassificationText',
  props:
    {
      emotionStatus: String,
      emotionSeverity: String,
      readable: Boolean
    },
  setup (props) {
    const store = useStore()
    var emotionColor = reactive({ color: '' })
    var backgroundColor = reactive({ bg: '' })
    const severityMapping = {
      barely: 0.07,
      slightly: 0.14,
      somewhat: 0.28,
      noticeably: 0.42,
      quite: 0.56,
      very: 0.70,
      extremely: 0.84,
      incredibly: 0.98
    }
    // todo: make sense of
    function hexToRgbA (hex, opacity) {
      if (props.readable === true) { opacity = 1 }
      var c
      if (/^#([A-Fa-f0-9]{3}){1,2}$/.test(hex)) {
        c = hex.substring(1).split('')
        if (c.length == 3) {
          c = [c[0], c[0], c[1], c[1], c[2], c[2]]
        }
        c = '0x' + c.join('')

        return 'rgba(' + [(c >> 16) & 255, (c >> 8) & 255, c & 255].join(',') + ',' + opacity + ')'
      }
      throw new Error('Bad Hex')
    }
    function invertColor (rgbColor) {
      var invertedString = 'rgba('
      rgbColor.forEach(colorValue => {
        colorValue = 255 - colorValue
        invertedString = invertedString + colorValue + ','
      })
      invertedString = invertedString.slice(0, -1)
      invertedString = invertedString + ')'
      return invertedString
    }

    const emotionColorHex = store.state.currentMoodColors.colorProfile[props.emotionStatus]
    const opacityLevel = severityMapping[props.emotionSeverity]
    emotionColor.color = hexToRgbA(emotionColorHex, opacityLevel)
    backgroundColor.bg = invertColor(emotionColor.color.split(/[(|,|)]/g).slice(1, 4))

    onUpdated(() => {
      const emotionColorHex = store.state.currentMoodColors.colorProfile[props.emotionStatus]
      const opacityLevel = severityMapping[props.emotionSeverity]
      emotionColor.color = hexToRgbA(emotionColorHex, opacityLevel)
      backgroundColor.bg = invertColor(emotionColor.color.split(/[(|,|)]/g).slice(1, 4))
    })
    return { backgroundColor, emotionColor }
  }

}
</script>

<style>

</style>
