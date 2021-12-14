<template>
        <Form :validation-schema="schema" id="ResetPassword" @submit="resetPassword">
        <br>
        <label for="password">Your new password </label>
        <Field class="field" name="password" type="text" /><br><br>
        </Form>

</template>

<script>
import AuthService from '@/services/auth.service.js'
import { Form, Field } from 'vee-validate'
import * as yup from 'yup'
export default {
  name: 'ResetPasswordForm',
  components: {
    Form,
    Field
  },
  props: {
    token: String
  },

  data () {
    const schema = yup.object().shape({
      password: yup.string().required('Password is required!').min(6, 'must be at least 6 characters')
    })
    return { schema }
  },

  methods: {
    resetPassword (newPassword) {
      const checkToken = this.$route.params.token
      const passwordPayload =
        {
          newPassword: newPassword.password,
          token: checkToken
        }
      console.log(passwordPayload)
      return AuthService.reset(passwordPayload)
    }
  }
}
</script>

<style>

</style>
