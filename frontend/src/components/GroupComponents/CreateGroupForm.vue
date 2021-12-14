<template>
<set-group-name v-if='currentPhase === "name"' />
<set-group-members v-if='currentPhase === "addMembers"' />
<set-group-colors v-if='currentPhase === "setColors"' />
<set-group-weights v-if='currentPhase === "setWeights"' />
<button @click='backButton' v-if='currentPhase !== "name"' > previous </button>
<button v-if='currentPhase === "confirm"' > confirm group settings </button>
</template>

<script>
// import GroupFunctions from '@/services/group.service.js'
import SetGroupName from './SetGroupName.vue'
import SetGroupMembers from './SetGroupMembers.vue'
import SetGroupColors from './SetGroupColors.vue'
import SetGroupWeights from './SetWeights.vue'
export default {
  name: 'CreateGroupForm',
  components: {
    SetGroupName,
    SetGroupMembers,
    SetGroupColors,
    SetGroupWeights
  },
  methods: {
    backButton () {
      this.$store.commit('groupCreator/previousForm')
    }
  },
  computed: {
    testData () {
      return this.$store.state.groupCreator.allFormData
    },
    currentPhase () {
      return this.$store.state.groupCreator.phaseList[this.$store.state.groupCreator.phaseList.length - 1]
    }
  }
}
</script>

<style>
.btn {
  padding: 15px 100px;
  margin:10px 4px;
  color: black;
  font-family: sans-serif;
  font-weight: 800;
  text-transform: uppercase;
  text-align: center;
  position: relative;
  text-decoration: none;
  display:inline-block;
}

.btn::before{
  content: "";
position: absolute;
top: 0;
left: 0;
display: block;
width: 100%;
height: 100%;
z-index: -1;
background-color: #000;
-webkit-transform: scaleY(.3);
transform: scaleY(.3);
opacity: 0;
transition: all .3s
}
.btn:hover{
  color:#6098FF;
}
.btn:hover::before{
  opacity: 1;
  background-color: #fff;
  -webkit-transform: scaleY(1);
  transform: scaleY(1);
  transition: -webkit-transform .6s cubic-bezier(.08, .35, .13, 1.02), opacity .4s;
  transition: transform .6s cubic-bezier(.08, .35, .13, 1.02), opacity
}
</style>
