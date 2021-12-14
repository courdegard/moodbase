import FetchFunctions from './fetch.service'

class WeightFunctions extends FetchFunctions {
  wackyLogic (x, y) {
    const excrement = {
      x: 0,
      y: 0
    }
    if (x > 0) {
      if (y > 0) {
        excrement.y++
      } else {
        excrement.y--
      }
    }
    if (y > 0) {
      if (x > 0) {
        excrement.x++
      }
    } else {
      excrement.x--
    }
  }
}

export default new WeightFunctions()
