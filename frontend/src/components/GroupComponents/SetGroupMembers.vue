<template>
<div >
    <Form :validation-schema="memberSchema" id="MembershipField" @submit="addMemberToList">
        <label  for="memberEmail">Who's in your group? </label>
        <Field  name="memberEmail" type="email" /><br><br>
        <button type="submit">Add this person to my group!</button>
    </Form>
      <ul  v-for="(activeAccount, email) in currentList" :key="email">
        <li :v-if='activeAccount' > {{ email }} <button @click='removeMemberFromList(email)' > remove </button></li>
      </ul>
      <button @click='moveToNextForm' v-if='Object.keys(currentList).length > 0'> Yes, add these people to my group! </button>
</div>
</template>

<script>
import { reactive } from 'vue'
import { useStore } from 'vuex'
import { Form, Field } from 'vee-validate'
import * as yup from 'yup'
export default {
  name: 'SetGroupMembers',
  components: {
    Form,
    Field
  },
  setup () {
    const store = useStore()
    function moveToNextForm () {
      store.commit('groupCreator/nextForm', { nextFormName: 'setColors', formValues: Object.keys(currentList) })
    }
    function addMemberToList (MembershipField) {
      currentList[MembershipField.memberEmail] = true
    }
    function removeMemberFromList (emailToRemove) {
      delete currentList[emailToRemove]
    }
    const currentList = reactive({})
    const memberSchema = yup.object().shape({
      memberEmail: yup
        .string()
        .required('Email is required!')
        .email('Email is invalid!')
        .max(30, 'Must be maximum 30 characters!')
    })
    return { memberSchema, currentList, moveToNextForm, addMemberToList, removeMemberFromList }
  }
}
</script>

<style>
.field{
  border: 2px solid black;
  border-radius: 4px;
}
</style>
