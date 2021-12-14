<template>
<div >
    <Form :validation-schema="weightSchema" id="WeightButtonField" @submit="addWeightToList">
        <label  for="weightName"> Which factors influencing mood will your group be tracking? </label>
        <Field  name="weightName" type="text" /><br><br>
        <button type="submit">I'd like to track this variable</button>
    </Form>
      <ul  v-for="(showWeight, weightName) in selectedWeights" :key="weightName">
        <li :v-if='showWeight' > {{ weightName }} <button @click='removeWeightFromList(weightName)' > remove </button></li>
      </ul>
      <button @click='moveToNextForm' v-if='Object.keys(selectedWeights).length > 0'> Let's track these for now </button>

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
      store.commit('groupCreator/nextForm', { nextFormName: 'confirm', formValues: Object.keys(selectedWeights) })
    }
    function addWeightToList (WeightButtonField) {
      selectedWeights[WeightButtonField.weightName] = true
    }
    function removeWeightFromList (weightToRemove) {
      delete selectedWeights[weightToRemove]
    }
    const selectedWeights = reactive({
      family: true,
      health: true,
      work_and_school: true,
      relationships: true,
      spirituality_and_faith: true
    })
    const weightSchema = yup.object().shape({
      weightName: yup
        .string()
        .required('Weight needs a name')
        .max(30, 'Must be maximum 30 characters')
    })
    return { weightSchema, selectedWeights, moveToNextForm, addWeightToList, removeWeightFromList }
  }
}
</script>

<style>
.field{
  border: 2px solid black;
  border-radius: 4px;
}
</style>
