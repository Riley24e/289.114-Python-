size(500,500)

grid = loadImage('grid.png')
image(grid, 0,0)

noFill()
strokeWeight(3)
#catmull
stroke('#0099FF')

#line(100,100,400,400)
curve(0,0,100,100,400,400,500,500)

curveTightness(0)

stroke('#FFFF00')
curve(0,250,100,100,400,400,500,250)

stroke('#ff9900')
#control point one
curve(0,250,0,250,100,100,400,400)

#control point two
curve(100,100,400,400,500,250,500,250)





#bezier

stroke('#ff99ff')

cp1x = 500
cp1y = 150 
cp2x = 320
cp2y = 350


bezier(
    400,100, #vertex 1
    cp1x,cp1y, #control point 1
    cp2x,cp2y, #control point 2
    100,400 #vertex 2
)


stroke('#ff0000')
line(400,100,cp1x,cp1y)
line(100,400,cp2x,cp2y)
