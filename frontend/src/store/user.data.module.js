import PlotFunctions from '@/services/plot.functions.js'
// import { timeParse, extent} from 'd3'

const initialState = {
  happiness: [],
  calm: [],
  mapX: [],
  mapY: [],
  timestamp: []
}

export const userData = {
  namespaced: true,
  state: initialState,
  getters: {
    // refactoring possible here
    returnMostRecent (state) {
      const i = state.happiness.length - 1
      const toBucket = {
        x: {
          magnitude: Math.round(Math.abs(state.happiness[i])),
          sign: Math.sign(state.happiness[i])
        },
        y: {
          magnitude: Math.round(Math.abs(state.calm[i])),
          sign: Math.sign(state.calm[i])
        }
      }
      return PlotFunctions.bucketMood(toBucket)
    },
    packageChartData (state) {
      return {
        happiness: state.happiness,
        calm: state.calm,
        count: state.calm.length
      }
    }
  },
  actions: {

    async retrieveClickData ({ commit }) {
      const dataToCommit = await PlotFunctions.get('plot/userclickdata').then(response => response.json())
      commit('createClickArray', dataToCommit)
    }
  },
  mutations: {
    createClickArray (state, arrayData) {
      state.happiness = arrayData.happiness
      state.calm = arrayData.calm
      state.mapX = arrayData.mapX
      state.mapY = arrayData.mapY
      state.timestamp = arrayData.timestamp
    },

    addNewClick (state, clickData) {
      state.happiness.push(clickData.lineChart.happinessVal)
      state.calm.push(clickData.lineChart.calmVal)
      state.mapX.push(clickData.clickMap.happinessVal)
      state.mapY.push(clickData.clickMap.calmVal)
    },

    wipeDataState (state) {
      Object.keys(initialState).forEach(key => { state[key] = initialState[key] })
    }

  }
}
