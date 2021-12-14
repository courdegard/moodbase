import { gsap } from 'gsap'

class Animator {
  shiftX (passRef, quadrant) {
    if (quadrant === 'two' || quadrant === 'four') {
      gsap.to(passRef, { x: '-200%', duration: 0.5 })
    } else {
      gsap.to(passRef, { x: '-100%', duration: 0.5 })
    }
  }

  shiftY (passRef, quadrant) {
    switch (quadrant) {
      case 'one':
        gsap.to(passRef, { y: '1000%', duration: 0.5 })
        gsap.to(passRef, { x: '10%', duration: 0.5 })
        break
      case 'two':
        gsap.to(passRef, { y: '1000%', duration: 0.5 })
        break
      default:
        gsap.to(passRef, { y: '750%', duration: 0.5 })
    }
  }

  revertX (passRef, quadrant) {
    if (quadrant === 'two' || quadrant === 'four') {
      gsap.to(passRef, { x: '6%', duration: 0.5 })
    } else {
      gsap.to(passRef, { x: '3%', duration: 0.5 })
    }
  }

  revertY (passRef, quadrant) {
    switch (quadrant) {
      case 'one':
        gsap.to(passRef, { y: '-5%', duration: 0.5 })
        gsap.to(passRef, { x: '-10%', duration: 0.5 })
        break
      case 'two':
        gsap.to(passRef, { y: '-3.5%', duration: 0.5 })
        break
      default:
        gsap.to(passRef, { y: '-2%', duration: 0.5 })
    }
  }

  moveGridAside (passRef, toTheRight) {
    if (toTheRight === true) {
      gsap.to(passRef, { x: '20%', duration: 0.5 })
    } else if (toTheRight === false) {
      gsap.to(passRef, { x: '-3%', duration: 0.5 })
    }
  }
}
export default new Animator()
