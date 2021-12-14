export const groupCreator = {
  namespaced: true,
  state: {
    allFormData: {},
    phaseList: ['name'],
    currentPhase: 'name',
    confirmColorChange: false
  },
  mutations: {
    nextForm (state, formData) {
      state.allFormData[state.currentPhase] = formData.formValues
      state.phaseList.push(formData.nextFormName)
      state.currentPhase = formData.nextFormName
    },
    previousForm (state) {
      if (state.currentPhase in state.allFormData) {
        delete state.allFormData[state.currentPhase]
      }
      state.phaseList.pop()
      state.currentPhase = state.phaseList[state.phaseList.length - 1]
    },
    readyToConfirmColorChange (state) {
      state.confirmColorChange = true
    }
  }
}
