<template>
  <h1> Welcome to the moodbase! </h1>

          <VisualizationDashboard v-if="checkedLoggedIn===true" />
          <div v-else> Looks like you haven't collected any data yet </div>
</template>

<script>
import VisualizationDashboard from '@/components/DataVisualizationComponents/VisualizationDashboard.vue'
export default {
  components: { VisualizationDashboard },
  name: 'UserHome',

  computed: {
    checkedLoggedIn () {
      if (this.$store.state.auth.loggedIn === true) { return true }
      return false
    }
  }
}

</script>

<style scoped>
h1 {
  color:black;
}
</style>
