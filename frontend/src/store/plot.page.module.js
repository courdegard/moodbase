import ColorFunctions from '@/services/color.functions.js'

const defaultColors = {
  happiness: '#FBF6D9',
  calm: '#CFECEC',
  anxiety: '#C35817',
  sadness: '#2B1B17'
}

const initialPanelState = {
  oldColorToChange: '',
  newColorOfChange: '',
  variableSelectedForColorChange: '',
  inPanelSubset: '',
  colorList: {}
}

const initialGridState = {
  colorProfile: defaultColors,
  showDataCollectionBox: false,
  showTextVariableQuadrant: { quadrant: '', move: false },
  animateTextInQuadrant: '',
  activeQuadrant: 'none',
  panelState: initialPanelState,
  displayOnlyMode: 0,
  incrementDisplayToggle: 1,
  hoverOnlyMode: false
}

export const plotPage = {
  namespaced: true,
  state: initialGridState,
  getters: {
    organizeColorsByQuadrant (state) {
      const quadrantsByVariable = {
        one: ['sadness', 'calm'],
        two: ['happiness', 'calm'],
        three: ['sadness', 'anxiety'],
        four: ['happiness', 'anxiety']
      }

      if (state.activeQuadrant !== 'none') {
        const vars = quadrantsByVariable[state.activeQuadrant]
        return {
          x: vars[0],
          y: vars[1],
          number: state.activeQuadrant
        }
      } else {
        const allQuadrantState = {}
        for (const [number, variables] of Object.entries(quadrantsByVariable)) {
          allQuadrantState[number] = {
            x: variables[0],
            y: variables[1],
            number: number
          }
        }
        return allQuadrantState
      }
    }
  },
  actions: {
    loadListOfColors ({ commit }) {
      ColorFunctions.get('plot/listofcolors')
        .then(res => res.json())
        .then(data => { commit('holdListOfColors', data) })
    },
    retrieveUserColorChoices ({ commit }) {
      return ColorFunctions.post({}, 'plot/usercolorchoice')
        .then(res => res.json())
        .then(data => {
          commit('loadUserColorChoices', data)
        })
    }
  },
  mutations: {
    setDisplayToggleIncrementValue (state, value) {
      if (value === 2) {
        state.displayOnlyMode = 1
      }
      state.incrementDisplayToggle = value
    },
    toggleHoverOnlyMode (state) {
      state.hoverOnlyMode = !state.hoverOnlyMode
    },
    toggleDisplayOnlyMode (state) {
      state.displayOnlyMode = (state.displayOnlyMode + state.incrementDisplayToggle) % 2
      if (state.displayOnlyMode === 0) {
        return false
      } else {
        return true
      }
    },
    activateQuadrant (state, quadrantToActivate) {
      state.activeQuadrant = quadrantToActivate
    },
    animateText (state, quadrantToAnimate) {
      state.animateTextInQuadrant = quadrantToAnimate
    },
    loadUserColorChoices (state, colorChoices) {
      state.colorProfile.happiness = colorChoices.happiness.hex
      state.colorProfile.sadness = colorChoices.sadness.hex
      state.colorProfile.calm = colorChoices.calm.hex
      state.colorProfile.anxiety = colorChoices.anxiety.hex
    },
    setVariableForColorChange (state, value) {
      if (value === '') {
        state.colorProfile[state.panelState.variableSelectedForColorChange] = state.panelState.oldColorToChange
        state.panelState.variableSelectedForColorChange = value
        state.panelState.oldColorToChange = ''
        state.panelState.inPanelSubset = ''
      } else {
        state.panelState.variableSelectedForColorChange = value
        state.panelState.oldColorToChange = state.colorProfile[value]
      }
    },
    holdColorChange (state, value) {
      state.panelState.newColorOfChange = value
      state.colorProfile[state.panelState.variableSelectedForColorChange] = value
    },
    setColorSubset (state, subsetName) {
      state.panelState.inPanelSubset = subsetName
    },
    clearPanelState (state) {
      state.panelState.oldColorToChange = ''
      state.panelState.newColorOfChange = ''
      state.panelState.variableSelectedForColorChange = ''
      state.panelState.inPanelSubset = ''
    },
    holdListOfColors (state, list) {
      state.panelState.colorList = list
    }
  }
}
