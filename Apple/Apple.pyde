size(800,800)

grid = loadImage('grid.png')
image(grid, 0,0)
apple = loadImage('apple copy.png')
image(apple, 0,0)

noFill()
strokeWeight(3)
fill('#ffffff')
beginShape()
vertex(0,0)
vertex(0,800)
vertex(800,800)
vertex(800,0)
vertex (0,0)
beginContour()
vertex(400,750)
bezierVertex(
             320,750,
             280,820,
             180,740
             )
bezierVertex(
             120,680,
             70,560,
             60,480
             )
bezierVertex(
             40,260,
             160,190,
             260,190
             )
bezierVertex(
             320,190,
             330,220,
             400,220
             )
bezierVertex(
             480,220,
             490,190,
             540,190
             )
bezierVertex(
             640,190,
             760,260,
             740,480
             )
bezierVertex(
             740,560,
             690,680,
             620,740
             )
bezierVertex(
             520,820,
             480,750,
             400,750
             )
endContour()
endShape()

beginShape()
vertex(370,200)
bezierVertex(
             520,820,
             480,750,
             400,750
             )
endContour()

endShape()
