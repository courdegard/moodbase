<template>
<div>
  <button class="weightButton" @mousedown="startTime" @mouseup="endTime">
     {{buttonName}} : {{buttonValue}}
  </button>
</div>
</template>

<script>
export default {
  name: 'Weight',
  props: {
    buttonName: String,
    buttonValue: Number,
    userId: Number
  }

}
</script>

<style>
.weightButton {
  background-color: #04AA6D;
  border: none;
  color: white;
  padding: 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  border-radius: 25%;
}
</style>
