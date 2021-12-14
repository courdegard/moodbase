<template>
    <div class="py-4" >
        Color popularity rankings - what does it look like when people feel {{currentVariable}}?
        <ul  v-for="(variable,i) in popularityData" :key="i" >
            <div class="border-black border-4 border-solid">{{i}}</div>
            <div class="border-black border-4 border-solid flex flex-col w-128  justify-between ">
                <ul v-for="(subVariable,j) in variable" :key="j">
                    <div :style="{'color':subVariable.value}" class="border-black border-4 border-solid">
                        <div class="flex flex-row justify-between">
                            <div>{{subVariable.value}}</div>
                            <div>{{subVariable.count}}</div>
                        </div>
                    </div>
                </ul>
            </div>
        </ul>
    </div>
</template>

<script>

export default {
  name: 'ColorPopularityDetails',
  props: {
    popularityData: Object
  },
  computed: {
    currentVariable () {
      return this.$store.state.currentMoodColors.variableSelection
    }
  }
}
</script>

<style>

</style>
