<template>
  <div class="flexct">
    <br>
    <keep-alive>
    <Weights />
    </keep-alive>
  </div>
</template>
<script>
import { defineAsyncComponent } from 'vue'
export default {
  name: 'WeightPage',
  components: {
    Weights: defineAsyncComponent(() => import('../components/WeightFunctionalityComponents/Weights.vue')
    )
  }
}
</script>
<style>
.circle {
  height: 100px;
  width: 200px;
  overflow: hidden;
  position: relative;
}
.circle:before {
  height: inherit;
  width: inherit;
  position: absolute;
  content: "";
  border-radius: 100px 100px 0 0;
  background-color: crimson;
  -webkit-transform-origin: 50% 100%;
  -moz-transform-origin: 50% 100%;
  -ms-transform-origin: 50% 100%;
  transform-origin: 50% 100%;
  -webkit-transform: rotate(140deg);
  -moz-transform: rotate(140deg);
  -ms-transform: rotate(140deg);
  transform: rotate(140deg);
}

.circle
{
  width: 100px;
  height: 100px;
  border-radius: 50%;
  border: 1px solid;
  background-color: #ff0000;
  opacity: 0.3;
}
</style>
