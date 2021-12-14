import FetchFunctions from './fetch.service'

class PlotFunctions extends FetchFunctions {
  coordinateTransform (e, quadrant) {
    var xValue = 0
    var yValue = 0
    const xCoordinate = (e.clientX - e.target.getBoundingClientRect().x)
    const yCoordinate = e.clientY - e.target.getBoundingClientRect().y
    switch (quadrant) {
      case 'one':
        xValue = -1 * (7 - xCoordinate * (7 / (e.target.getBoundingClientRect().right - e.target.getBoundingClientRect().x)))
        yValue = (7 - yCoordinate * (7 / (e.target.getBoundingClientRect().bottom - e.target.getBoundingClientRect().y)))
        break
      case 'two':
        xValue = xCoordinate * (7 / (e.target.getBoundingClientRect().right - e.target.getBoundingClientRect().x))
        yValue = 7 - yCoordinate * (7 / (e.target.getBoundingClientRect().bottom - e.target.getBoundingClientRect().y))
        break
      case 'three':
        xValue = -1 * (7 - xCoordinate * (7 / (e.target.getBoundingClientRect().right - e.target.getBoundingClientRect().x)))
        yValue = -1 * (yCoordinate * (7 / (e.target.getBoundingClientRect().bottom - e.target.getBoundingClientRect().y)))
        break
      case 'four':
        xValue = (xCoordinate * (7 / (e.target.getBoundingClientRect().right - e.target.getBoundingClientRect().x)))
        yValue = -1 * (yCoordinate * (7 / (e.target.getBoundingClientRect().bottom - e.target.getBoundingClientRect().y)))
        break
    }
    return {
      happinessVal: Number(String(xValue).slice(0, String(xValue).lastIndexOf('.') + 2)),
      calmVal: Number(String(yValue).slice(0, String(yValue).lastIndexOf('.') + 2))
    }
  }

  maplerize (val, axis) {
    if (axis === 'x') {
      return (((val + 7) * 100) / 14)
    } else {
      return 100 - (((val + 7) * 100) / 14)
    }
  }

  classifyMoodValues (coordinates) {
    return this.bucketMood({
      x: { magnitude: Math.round(Math.abs(coordinates.happinessVal)), sign: Math.sign(coordinates.happinessVal) },
      y: { magnitude: Math.round(Math.abs(coordinates.calmVal)), sign: Math.sign(coordinates.calmVal) }
    })
  }

  bucketMood (coordinatePair) {
    const bucketMagnitude = {
      0: 'barely',
      1: 'slightly',
      2: 'somewhat',
      3: 'noticeably',
      4: 'quite',
      5: 'very',
      6: 'extremely',
      7: 'incredibly'
    }
    const bucketHappiness = {
      '-1': 'sad',
      1: 'happy',
      0: 'any happiness or sadness'
    }
    const bucketCalm = {
      '-1': 'anxious',
      1: 'calm',
      0: 'any calm or anxiety'
    }
    const classificationInformation = {
      happiness: {
        severity: bucketMagnitude[coordinatePair.x.magnitude],
        mood: bucketHappiness[coordinatePair.x.sign]
      },
      calm: {
        severity: bucketMagnitude[coordinatePair.y.magnitude],
        mood: bucketCalm[coordinatePair.y.sign]
      }
    }
    return classificationInformation
  }

  returnGradient (request) {
    if (request.axis === 'h') {
      return { x1: 1, x2: 0, y1: 0.5, y2: 0.5 }
    } else if (request.axis === 'v') {
      return { x1: 0.5, x2: 0.5, y1: 0, y2: 1 }
    }
  }
}

export default new PlotFunctions()
