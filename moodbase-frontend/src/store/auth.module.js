import AuthService from '../services/auth.service';

const user = JSON.parse(localStorage.getItem('user'));
const initialState = user
  ? { status: { loggedIn: true }, user }
  : { status: { loggedIn: false }, user: null };

export const auth = {
  namespaced: true,
  state: initialState,
  actions: {
    async login({ commit }, user) {
      await AuthService.login(user).then(data => {
          commit('loginSuccess', data);
          return data
          }).catch((error) => {
          commit('loginFailure');
          return Promise.reject(error);
        })
      },
    logout({ commit }, user) {
      AuthService.logout(user);
      commit('logout');
    },
    register({ commit }, user) {
      return AuthService.register(user).then(
          response => {
            commit('registerSuccess');
            return response        
        },
        error => {
          commit('registerFailure');
          return Promise.reject(error);
        }
      )},
    },
  mutations: {
    loginSuccess(state, user) {
      state.status.loggedIn = true;
      state.user = user;
    },
    loginFailure(state) {
      state.status.loggedIn = false;
      state.user = null;
    },
    logout(state) {
      state.status.loggedIn = false;
      state.user = null;
    },
    registerSuccess(state) {
      state.status.loggedIn = false;
    },
    registerFailure(state) {
      state.status.loggedIn = false;
    }
  },

};
