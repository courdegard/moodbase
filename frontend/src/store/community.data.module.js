import PlotFunctions from '@/services/plot.functions.js'

const initialState = {
  dayList: [],
  clickMap: [],
  averageLineChartHappiness: [],
  averageLineChartCalm: [],
  totalHappinessByDay: [],
  totalCalmByDay: [],
  clickCount: 0

}

export const communityData = {
  namespaced: true,
  state: initialState,
  getters: {
  },
  actions: {

    async communityClickData ({ commit }) {
      const dataToCommit = await PlotFunctions.get('plot/communityclickdata').then(response => response.json())
      commit('createClickArray', dataToCommit)
    }
  },
  mutations: {
    createClickArray (state, arrayData) {
      Object.keys(arrayData).forEach(key => {
        state[key] = arrayData[key]
      })
    },

    addNewClick (state, clickData) {
      state.lineChartArrays.happinessVals.push(clickData.lineChart.happinessVal)
      state.lineChartArrays.calmVals.push(clickData.lineChart.calmVal)
      state.clickMapArray.push(clickData.clickMap)
    },

    wipeDataState (state) {
      Object.keys(initialState).forEach(key => {
        state[key] = initialState[key]
      })
    }

  }
}
