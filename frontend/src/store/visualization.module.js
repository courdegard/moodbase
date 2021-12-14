export const wheelLock = {
  namespaced: true,
  state: { mouseOverMap: false },
  getters: {
    isWheelLocked (state) {
      return state.mouseOverMap
    }
  },
  mutations: {
    lockWheel (state) {
      state.mouseOverMap = true
    },
    unlockWheel (state) {
      state.mouseOverMap = false
    }
  }
}
