<template>
<div>
    <h1>Sign up below with an email address, username and password. Password must be at least 6 characters.</h1>
    <Form :validation-schema="schema" id="RegistrationForm" @submit="handleRegistration">
        <br>

        <label for="username">username </label>
        <Field  name="username" type="text" /><br><br>
        <label for="password">password </label>
        <Field  name="password" type="password" /><br><br>
        <label for="email">email </label>
          <Field class="field" name="email" type="text" /><br><br>
        <button  class="button2"  type="submit">Log me in!</button>

    </Form>

</div>
</template>

<script>

import AuthService from '@/services/auth.service'
import { Form, Field } from 'vee-validate'
import * as yup from 'yup'

export default {
  name: 'Register',
  components: {
    Form,
    Field
  },
  data () {
    const schema = yup.object().shape({
      username: yup
        .string()
        .required('Username is required!')
        .min(3, 'Must be at least 3 characters!')
        .max(20, 'Must be maximum 20 characters!'),
      email: yup
        .string()
        .required('Email is required!')
        .email('Email is invalid!')
        .max(50, 'Must be maximum 50 characters!'),
      password: yup
        .string()
        .required('Password is required!')
        .min(6, 'Must be at least 6 characters!')
        .max(40, 'Must be maximum 40 characters!')
    })
    return {
      successful: false,
      loading: false,
      message: '',
      schema
    }
  },
  computed: {
    loggedIn () {
      return this.$store.state.auth.loggedIn
    }
  },
  mounted () {
    if (this.loggedIn) {
      this.$router.push('/home')
    }
  },
  methods: {

    handleRegistration (registrationForm) {
      console.log('133W')
      this.message = ''
      this.successful = false
      this.loading = true
      return AuthService.register(registrationForm).then(
        response => {
          console.log(response)
          if (response.status === 200) {
            alert("Success! You'll be getting an activation link in your email soon.")
          } else if (response.status !== 200) {
            alert('User with that username or email already exists')
          }
        })
    }
  }
}

</script>

<style>
.flexcr{
  display:flex;
  margin-left:30%;
  padding:0;
  flex-direction:column;
}

.flexrr{
  display:flex;
  margin:0;
  column-gap: 10%;
  justify-content:right;
  padding:0;
  flex-direction:row;
}
</style>
