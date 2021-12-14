import { select } from 'd3'
class VisualizationFunctions {
  drawGradients (svgRef) {
    const svg = select(svgRef)
    for (let i = 0; i < 14; i++) {
      svg.append('rect')
        .attr('y', String(i * 7))
        .attr('width', '100%')
        .attr('height', '7%')
        .attr('fill', 'pink')
    }
  }
}
export default new VisualizationFunctions()
