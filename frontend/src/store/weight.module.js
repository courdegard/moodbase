import WeightFunctions from '@/services/weight.functions.js'

const initialState = {
  vertexButtCoordinates: {},
  currentButtCoordinates: {
    x: 0,
    y: 0
  },
  buttConfig: {},
  interval: null,
  sumX: 0,
  sumY: 0
}

export const butts = {
  namespaced: true,
  state: initialState,
  getters: {
    dataForDotRendering (state) {
      return {
        numPoints: Object.keys(state.todaysButts).length,
        buttNames: Object.keys(state.todaysButts)
      }
    }
  },
  actions: {
    createButts ({ commit }) {
      WeightFunctions.get('allot/retrieveweightdata')
        .then(res => res.json())
        .then(data => {
          commit('loadInitialButts', data)
        })
    },
    newButt ({ commit }, butt) {
      WeightFunctions.post({}, 'allot/createnewbutton/' + butt)
      commit('brandNewButt', butt)
    },
    deleteButt ({ commit }, butt) {
      WeightFunctions.post({}, 'allot/deletebutt/' + butt)
      commit('deleteButt', butt)
    }
  },
  mutations: {
    vertexCoordinates (state, variable, coords) {
      state.vertexButtCoordinates[variable].x = coords.x
      state.vertexButtCoordinates[variable].y = coords.y
    },
    drawPath (state, variable) {
      var wiggleRoom = 0
      for (const v of Object.values(state.currentButtCoordinates)) {
        for (const sv of v) {
          wiggleRoom += sv ** 2
        }
      }
      var x = state.currentButtCoordinates[variable].x
      var y = state.currentButtCoordinates[variable].y
      while (x ** 2 + y ** 2 <= wiggleRoom) {
        const incrementOrDecrement = WeightFunctions.wackyLogic(x, y)
        state.currentButtCoordinates[variable].x += incrementOrDecrement.x
        state.currentButtCoordinates[variable].y += incrementOrDecrement.y
        x += incrementOrDecrement.x
        y += incrementOrDecrement.y
      }
    }
  }
}
