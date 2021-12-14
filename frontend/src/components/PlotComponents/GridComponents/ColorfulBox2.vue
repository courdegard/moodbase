<template>

<transition leave-active-class="animate__animated animate__fadeOut" >

    <div @click="triggerMove" @mouseenter="handleBoxVisibility(false)"
    @mouseleave="handleBoxVisibility(false)" :style="setBoxFill">
        <slot  > </slot>
    </div>

</transition>

</template>

<script>
import ColorFunctions from '@/services/color.functions.js'
export default {
  name: 'ColorfulBox2',
  components: {},
  props: {
    quadrantData: {
      type: Object,
      required: true
    },
    x: {
      type: String,
      default: '0%'
    },
    y: {
      type: String,
      default: '0%'
    }
  },
  data () {
    return {
      showGradientFill: false,
      showBorder: '1px solid black'
    }
  },
  computed: {
    hideGradientFill () {
      return this.$store.state.plotPage.hoverOnlyMode
    },
    lockGradientFill () {
      return this.$store.state.plotPage.displayOnlyMode
    },
    // get some state data to get started
    currentlyActiveQuadrant () {
      return this.$store.state.plotPage.activeQuadrant
    },
    // lock box fill by disabling hover functionality once you've clicked on a box
    blockHoverEffects () {
      if (this.hideGradientFill === true) {
        return true
      } else {
        return false
      }
    },
    // dynamic css styling for the border and background (gradient) of each box
    setBoxFill () {
      if ((this.showGradientFill && !this.hideGradientFill) || this.lockGradientFill) {
        return {
          '--h': 'linear-gradient(to ' + this.xDir + this.xColor + ')',
          '--v': 'linear-gradient(to ' + this.yDir + this.yColor + ')',
          '--border': this.showBorder,
          '--offsetX': this.x,
          '--offsetY': this.y
        }
      } else {
        return {
          '--h': 'linear-gradient(to right, white, transparent)',
          '--v': 'linear-gradient(to right, white, transparent)',
          '--border': this.showBorder,
          '--offsetX': this.x,
          '--offsetY': this.y
        }
      }
    },
    xColor () {
      const baseColor = this.$store.state.plotPage.colorProfile[this.quadrantData.x]
      return ColorFunctions.createGradientString(baseColor, [7, 100]) + baseColor + ' 100%'
    },
    yColor () {
      const baseColor = this.$store.state.plotPage.colorProfile[this.quadrantData.y]
      return ColorFunctions.createGradientString(baseColor, [7, 100]) + baseColor + ' 100%'
    },
    xDir () {
      if (this.quadrantData.number === 'one' || this.quadrantData.number === 'three') {
        return 'left, '
      } else {
        return 'right, '
      }
    },
    yDir () {
      if (this.quadrantData.number === 'one' || this.quadrantData.number === 'two') {
        return 'top, '
      } else {
        return 'bottom, '
      }
    }

  },
  watch:
    {
      currentlyActiveQuadrant (newVal) {
        if (newVal === this.quadrantData.number) {
          this.$store.commit('plotPage/animateText', this.quadrantData.number)
          setTimeout(() => {
            this.handleBoxVisibility(true)
          },
          1000)
        } else {
          this.handleBoxVisibility(true)
        }
      }
    },
  methods: {
    handleBoxVisibility (blockHover) {
      if (blockHover === true) {
        this.showGradientFill = false
        this.showBorder = false
      } else if (!this.hideGradientFill) {
        this.showGradientFill = !this.showGradientFill
      }
    },
    triggerMove (e) {
      this.$store.commit('plotPage/activateQuadrant', this.quadrantData.number)
      console.log(this.lockGradientFill)
      this.showGradientFill = false
    }
  }
}
</script>

<style scoped>

div {
    position:relative;
    width:20vw;
    height:20vw;
    background: var(--h), var(--v);
    background-blend-mode: multiply;
    border:var(--border);
    right:var(--offsetX);
    top:var(--ofsetY);
    cursor:pointer;
}

</style>
