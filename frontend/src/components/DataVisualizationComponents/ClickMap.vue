<template>

      <svg width="80%" height="80%">
        <g>
        <rect width="100%" height="100%" stroke="gray" stroke-width="5" fill="none"/>

          <circle v-for="(xCoord,index) in xVals" :key="index" :cx="String(xCoord)+'%'" :cy="String(yVals[index])+'%'" r="2%"/>

        </g>
      </svg>
</template>

<script>
export default {
  name: 'ClickMap',
  emits: ['lock-wheel', 'unlock-wheel'],
  props: {
    isCommunityData: Boolean
  },
  methods: {
    buildCoordinate (coord) {
      return String(coord) + '%'
    },
    lockWheel () {
      this.isWheelLocked = true
      this.$emit('lock-wheel', this.isWheelLocked)
    },
    unlockWheel () {
      this.isWheelLocked = false
      this.$emit('unlock-wheel', this.isWheelLocked)
    },
    scrollPoints (e) {
      // scroll up to load more points
      if (e.deltaY < 0 && this.hiddenCoordinates.length > 0) {
        this.coordinateArray.push(this.hiddenCoordinates.shift())
        this.lastIndex += 1
      }
      // scroll down to load fewer points
      else if (e.deltaY > 0 && this.coordinateArray.length > 0) {
        this.hiddenCoordinates.unshift(this.coordinateArray.pop())
        this.lastIndex -= 1
      }
    }
  },
  data () {
    return {
      hiddenCoordinates: [],
      displayDate: '',
      mostRecentValue: {},
      isWheelLocked: false,
      wheelEvent: {}
    }
  },
  computed: {
    xVals () {
      var coordinateArrayX = []
      if (this.isCommunityData === false) { coordinateArrayX = this.$store.state.userData.mapX } else { coordinateArrayX = this.$store.state.communityData.clickMap }
      return coordinateArrayX
    },
    yVals () {
      var coordinateArrayY = []
      if (this.isCommunityData === false) { coordinateArrayY = this.$store.state.userData.mapY } else { coordinateArrayY = this.$store.state.communityData.clickMap }
      return coordinateArrayY
    }
  }
}

</script>

<style>

</style>
