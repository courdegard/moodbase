<template>
<transition leave-active-class="animate__animated animate__fadeOut" >
    <div v-transition-grid="variableAndQuadrantData.variable" :watch="animate"
    v-if="showText" :style="tStyle" >{{ variableAndQuadrantData.variable }}</div>
</transition>
</template>

<script>
import Animator from '@/services/animation.service.js'
export default {
  name: 'TextElement',
  data () {
    return {
      watch: true,
      reverse: false
    }
  },
  props: {
    isClassifier: {
      default: false,
      type: Boolean
    },
    variableAndQuadrantData: {
      type: Object,
      required: false,
      default: () => { return {} }
    },
    y: {
      type: String,
      default: '10%'
    }
  },
  computed: {
    test () {
      return this.$store.state.plotPage.animateTextInQuadrant
    },
    animate () {
      const quadrantToAnimate = this.$store.state.plotPage.animateTextInQuadrant
      if (quadrantToAnimate === this.variableAndQuadrantData.quadrant) {
        return true
      }
      return false
    },
    tStyle () {
      return { '--yOffset': this.y }
    },
    activeQuadrant () {
      return this.$store.state.plotPage.activeQuadrant
    },
    showText () {
      if (this.activeQuadrant !== this.variableAndQuadrantData.quadrant && this.activeQuadrant !== 'none') {
        return false
      }
      return true
    }
  },
  directives: {
    transitionGrid: {
      updated: (el, binding) => {
        const quad = binding.instance.$props.variableAndQuadrantData.quadrant
        if (binding.instance.animate) {
          if (binding.value === 'calm' || binding.value === 'anxiety') {
            Animator.shiftX(el, quad)
          } else if (binding.value === 'happiness' || binding.value === 'sadness') {
            Animator.shiftY(el, quad)
          }
        } else {
          if (binding.value === 'calm' || binding.value === 'anxiety') {
            Animator.revertX(el, quad)
          } else if (binding.value === 'happiness' || binding.value === 'sadness') {
            Animator.revertY(el, quad)
          }
        }
      }
    }
  }

}
</script>

<style scoped>
div {
    position:relative;
    top: var(--yOffset);
    font-size:xx-large;
    cursor:pointer;
}
</style>
