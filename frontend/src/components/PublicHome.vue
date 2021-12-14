<template>
  <div class="flexrh">
    <router-link to="/register"> Sign up</router-link>
    <router-link to="/login"> Sign in</router-link>
  </div>

</template>

<script>
export default {
  name: 'PublicHome'
}
</script>

<style scoped>
.flexrh{
  display: flex;
  margin: auto;
  box-sizing: border-box;
  width: max-content;
  padding: 5%;
  flex-direction: column;
  border: 5px solid black;
  font-size: xxx-large;
}

/* body, html {
  padding: 0;
  margin: 0;
  width: 100%;
  min-height: 100vh;
}
body {
  background-color: rgba(184, 235, 201, 0.959);
} */
</style>
