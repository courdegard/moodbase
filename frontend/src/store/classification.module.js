const initialState={
    happiness: {
        severity:"",
        mood:"",
      },
      calm:{
        severity:"",
        mood:""
      }
}

export const moodClassification = {
    namespaced:true,
    state:initialState,
    // actions:{
    //     classifyCoordinates(state){
    //         console.log(state)
    //     },
    // },
    getters: {
        getClassification( state ){
            return state.happiness.severity;
        }
    },
    mutations:{
        setNewClassification(state,classificationState){
            state=classificationState;
        }
    }
}