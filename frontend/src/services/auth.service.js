// const API_URL = 'http://localhost:8000/api/auth/';
import FetchFunctions from './fetch.service.js'

class AuthService extends FetchFunctions {
  login (loginForm) {
    console.log('Login in progress')
    return this.post({ username: loginForm.username, password: loginForm.password }, 'auth/login')
  }

  logout () {
    console.log('Logout in progress')
    return this.post({}, 'auth/logout')
  }

  register (user) {
    console.log('User registration in progress')
    return this.post({ username: user.username, email: user.email, password: user.password }, 'auth/register')
  }

  activate (token) {
    console.log('User activation in progress')
    return this.post({ token: token }, 'auth/activate')
  }

  forgot (emailObj) {
    console.log('Sending reset email')
    return this.post(emailObj, 'auth/forgot')
  }

  reset (newPasswordAndToken) {
    console.log('Resetting password')
    return this.post(newPasswordAndToken, 'auth/reset')
  }
}

export default new AuthService()
