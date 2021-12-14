<template>
      <Form :validation-schema="schema" id="ForgotPasswordEmail" @submit="submitResetRequest">
        <br>
        <label for="email">Your email address </label>
        <Field class="field" name="email" type="text" /><br><br>
    </Form>
</template>

<script>
import AuthService from '@/services/auth.service.js'
import { Form, Field } from 'vee-validate'
import * as yup from 'yup'
export default {
  name: 'ForgotPasswordEmail',
  components: {
    Form,
    Field
  },
  data () {
    const schema = yup.object().shape({
      email: yup
        .string()
        .required('Email is required!')
        .email('Email is invalid!')
    })
    return { schema }
  },
  methods: {
    submitResetRequest (e) {
      const resetModelObject = {
        email: e.email,
        token: '',
        newPassword: ''
      }
      return AuthService.forgot(resetModelObject).then(response => response.json()).then(data => { alert(data.message) })
    }
  }
}
</script>

<style>

</style>
