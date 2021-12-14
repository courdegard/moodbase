import FetchFunctions from './fetch.service'

class ColorFunctions extends FetchFunctions {
  formatColorData () {
    return this.get('plot/popularcolors').then(response => response.json())
  }

  hexToRgbA (hex, opacity) {
    var c
    if (/^#([A-Fa-f0-9]{3}){1,2}$/.test(hex)) {
      c = hex.substring(1).split('')
      if (c.length === 3) {
        c = [c[0], c[0], c[1], c[1], c[2], c[2]]
      }
      c = '0x' + c.join('')

      return 'rgba(' + [(c >> 16) & 255, (c >> 8) & 255, c & 255].join(', ') + ', ' + opacity + ')'
    }
    throw new Error('Bad Hex')
  }

  invertColor (rgbColor, opacity) {
    var invertedString = 'rgba('
    console.log(rgbColor)
    rgbColor.forEach(colorValue => {
      colorValue = 255 - colorValue
      invertedString = invertedString + colorValue + ', '
    })
    invertedString = invertedString + (1 - opacity) + ')'
    return invertedString
  }

  createGradientString (color, interval, inverse) {
    var colorString = ''
    for (var i = interval[0]; i < interval[1]; i += 7) {
      if (inverse) {
        colorString = colorString + color + ' ' + i + '%, '
      } else {
        colorString = colorString + this.hexToRgbA(color, i / 100) + ' ' + i + '%, '
      }
    }
    return colorString
  }

  hexToInverseGradient (hex, index) {
    console.log(this.hexToRgbA(hex, index))
    const rawString = this.createGradientString(
      this.invertColor(this.hexToRgbA(hex, index)
        .slice(6, this.hexToRgbA(hex, index).lastIndexOf(')'))
        .split(',')
        .slice(0, 3),
      index / 100),
      [index, index + 7],
      true)
    const rgbOnly = rawString.slice(0, rawString.lastIndexOf(')') + 1)
    let startOpacity = rgbOnly.slice(rgbOnly.lastIndexOf('.') - 1, rgbOnly.indexOf(')'))
    startOpacity = startOpacity.slice(0, startOpacity.indexOf('.') + 3)
    var stopOpacity = 0
    if (startOpacity < 0.03) {
      stopOpacity = startOpacity + 0.14
    } else {
      stopOpacity = startOpacity - 0.14
    }
    var stopGradient = rgbOnly.slice(0, rgbOnly.lastIndexOf(', '))
    stopGradient = String(stopGradient) + ', ' +
    String(stopOpacity).slice(0, String(stopOpacity).indexOf('.') + 2) + ')'
    return {
      startY: String(index) + '%',
      stopY: String(index + 7) + '%',
      startGradient: rgbOnly,
      stopGradient: stopGradient
    }
  }
}

export default new ColorFunctions()
