<template>
<div class="name-style">
    <Form :validation-schema="groupNameSchema" id="GroupNameForm" @submit="validateGroupName">
        <label  for="groupName">What's your group called? </label> <br>
        <Field  name="groupName" type="text" />
        <button  class="btn"  type="submit">Make my group!</button>
        <div >
        <error-message name="groupName" />
        </div>
    </Form>

</div>
</template>

<script>
import { useStore } from 'vuex'
import { Form, Field, ErrorMessage } from 'vee-validate'
import * as yup from 'yup'
export default {
  name: 'SetGroupName',
  components: {
    Form,
    Field,
    ErrorMessage
  },
  setup () {
    const store = useStore()
    function validateGroupName (GroupNameForm) {
      store.commit('groupCreator/nextForm', { nextFormName: 'addMembers', formValues: GroupNameForm.groupName })
    }
    const groupNameSchema = yup.object().shape({
      groupName: yup
        .string()
        .required('Please give your group a name')
        .min(3, 'Group name must be at least 3 characters')
        .max(20, 'Group name must have maximum 20 characters')
        .matches(/^[a-zA-Z0-9_.-]*$/, 'bad input')
    })
    return { groupNameSchema, validateGroupName }
  }
}
</script>

<style>
input {
  font-size:xx-large;
  width:50%;
  border:3px solid black;
}
input:valid {
  border-color: green;
}

input:invalid {
  border-color: red;
  background-color: red;
}
.name-style{
  display: flex;
  margin: auto;
  box-sizing: border-box;
  width: max-content;
  padding: 5%;
  flex-direction: column;
  border: 5px solid black;
  font-size: xxx-large;
}
.field{
  border: 10px solid black;
  border-radius: 4px;
}
</style>
