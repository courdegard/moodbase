<template>
<h1>
Last I heard, you were feeling {{ currentMood.happiness.severity }} {{ currentMood.happiness.mood}}
    and {{ currentMood.calm.severity }} {{ currentMood.calm.mood }}.
</h1>
</template>

<script>
export default {
  name: 'UserDataOverview',
  components: {},
  computed: {
    currentMood () {
      return this.$store.getters['userData/returnMostRecent']
    }
  }
}
</script>

<style>

</style>
