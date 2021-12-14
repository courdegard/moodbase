import AuthService from '../services/auth.service'

const initialState = {
  loggedIn: false
}

export const auth = {
  namespaced: true,
  state: initialState,
  actions: {
    login ({ commit }, user) {
      return AuthService.login(user)
        .then(
          response => response.json())
        .then(
          data => {
            if ('detail' in data) {
              return 'Failed'
            }
            commit('loginSuccess', data)
            return data
          }
        )
        .catch(
          (error) => {
            commit('loginFailure')
            return error
          }
        )
    },
    logout ({ commit }) {
      localStorage.clear()
      commit('logoutSuccess')
    },
    activate ({ commit }, token) {
      commit('loginSuccess', token)
    },
    refresh ({ commit }) {
      commit('loginSuccess')
    }
  },
  mutations: {
    loginSuccess (state, tokenData) {
      state.loggedIn = true
      window.localStorage.setItem('accessToken', tokenData.access_token)
      window.localStorage.setItem('refreshToken', tokenData.refresh_token)
    },
    loginFailure (state) {
      state.loggedIn = false
      state.user = null
    },
    logoutSuccess (state) {
      state.loggedIn = false
      return AuthService.logout()
    },
    refreshToken (state, newToken) {
      window.localStorage.setItem('accessToken', newToken)
    }
  }

}
