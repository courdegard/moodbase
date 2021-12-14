<template>
<br>
<br>
  <div class="test">

    <CreateGroupForm />
    <!-- <ClickMap /> -->
  </div>

</template>

<script>
// import ClickMap from '@/components/DataVisualizationComponents/ClickMap.vue'
import CreateGroupForm from '@/components/GroupComponents/CreateGroupForm.vue'
export default {
  name: 'GroupPage',
  components: { CreateGroupForm }
}
</script>

<style>

.test{
  transform: translate(50%, 0);
  position:fixed;
  margin: auto;
  width: 50vw;
  height: 50vw;

}
/* .
        CreateGroupFormtest {

  position:fixed;
  margin: auto;
  width: 50vw;
  height: 50vw;
  transform: translate(50%, 0);

  /* border: 3px solid gray; */
/* } */
</style>
