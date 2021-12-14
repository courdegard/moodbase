<template>
  <h1> Thanks for activating your account! We'll redirect you to the home page soon </h1>
</template>

<script>
import AuthService from '@/services/auth.service.js'
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'
export default {
  name: 'Activate',
  props: { token: String },
  async setup (props) {
    const store = useStore()
    const router = useRouter()
    await AuthService.activate(props.token)
      .then(res => res.json())
      .then(async data => {
        store.dispatch('auth/activate', data)
        store.dispatch('userData/retrieveClickData')
        store.dispatch('currentMoodColors/createInitialState')
        router.push('/home')
      })
  }
}
</script>

<style>

</style>
