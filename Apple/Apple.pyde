size(800,800)

grid = loadImage('grid.png')
image(grid, 0,0)
apple = loadImage('apple copy.png')
image(apple, 0,0)

noFill()
strokeWeight(0)


#color
fill('#00bc38')
rect(0,190,800,100)
fill('#ffb900')
rect(0,290,800,100)
fill('#ff8301')
rect(0,390,800,100)
fill('#ff373c')
rect(0,490,800,100)
fill('#ad3b9b')
rect(0,590,800,100)
fill('#009edf')
rect(0,690,800,100)




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
fill('#00bc38')
beginShape()
vertex(370,200)
bezierVertex(
             360,95,
             390,20,
             500,20
             )
bezierVertex(
             510,130,
             480,190,
             370,200
             )

endShape()

#circle
fill('#FFFFFF')
ellipse(720,420,320,320)

strokeWeight(5)
fill('#FFFFFF')
ellipse(750,750,75,75)
fill('#000000')
textSize(50)
text('R', 735,770)
