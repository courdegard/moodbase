<template>
<body>
<div  class="navbar" v-if="checkLogin">

  <div class="navitem">
    <router-link to="/home">back to base!</router-link>
  </div>
  <div class="navitem">
    <router-link to="/plot">how do you feel?</router-link>
  </div>
  <div class="navitem">
    <router-link to="/allot">what's bothering you?</router-link>
  </div>
  <div class="navitem">
    <router-link to="/groups">how are your groups doing?</router-link>
  </div>
  <div class="navitem">
    <a id="logoutButton" @click="logout">logout</a>
  </div>
</div>

  <br>

  <br>
    <router-view :key="$route.fullPath"></router-view>

</body>
</template>

<script>
// import {mapActions} from 'vuex'
export default {
  data () {
    return {
      hide: false
    }
  },

  computed: {
    checkLogin () {
      return this.$store.state.auth.loggedIn
    }

  },

  methods: {
    toggleHide () {
      this.hide = !this.hide
    },
    logout () {
      // this.$store.commit('userData/wipeDataState')
      // this.$store.commit('butts/wipeButts')
      this.$store.dispatch('auth/logout')
      console.log('s')
      this.$router.push('/')
    }
  }

}
</script>

<style>

.navitem {
  margin-left:2%;
}

body, html {
  padding: 0;
  margin: 0;
  width: 100%;
  min-height: 100vh;
}
/* body {
  background-color: #cc99ff;
} */

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.navbar {
  justify-content:center;
  overflow:hidden;
  display:flex;
  flex-direction:row;
  padding-top:.5%;
  padding-bottom:.5%;
  margin-bottom:5%;
  width:100%;
  font-size:x-large;
  font-weight: bold;
  background-color: #ffb3d9;
}

li {
  list-style-type:none;
  margin-left:5%;
  color:black;
}

a:visited{
  color:black;
}

a {
    text-decoration:none;
    cursor:pointer;
}
ul a:hover{
  color:#42b983
}

div a.router-link-exact-active {
  text-decoration:none;
  color: #42b983;
}

.flexc{
  display:flex;
  margin:0;
  padding:0;
  flex-direction:column;
}

.flexr{
  display:flex;
  margin:0;
  padding:0;
  flex-direction:row;
}

.button2{
  display:inline-block;
  padding:0.5em 3em;
  border:0.16em solid #FFFFFF;
  margin:0 0.3em 0.3em 0;
  box-sizing: border-box;
  text-decoration:none;
  /* text-transform:uppercase; */
  font-family:'Roboto',sans-serif;
  font-weight:400;
  color:black;
  text-align:center;
  transition: all 0.15s;
}
.button2:hover{
  /* color:#DDDDDD; */
  border-color:#DDDDDD;
}
.button2:active{
  color:#BBBBBB;
  border-color:#BBBBBB;
}

label {
  font-size:150%;
}

.field {
  width:30%;
  border: 2px solid black;
  border-radius: 7%;
}

</style>
