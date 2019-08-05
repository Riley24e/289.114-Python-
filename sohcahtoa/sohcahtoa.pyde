theta = 0
radius = 1
s = 200 # scale variable

def setup():
    size(600,600)
    noFill()
    stroke('#FFFFFF')
    strokeWeight(3)

def draw():
    global theta
    background('#004477')
    translate(width/2,height/2)
    diameter = radius*s*2
    ellipse(0,0,diameter,diameter)
    x = cos(theta)
    y = sin(theta)
    line(0,0,x*s,y*s)
    
    ellipse(-width/2+40, y*s,10,10)
    ellipse(x*s, -height/2 + 40,10,10)
    
    line(x*s,y*s,-width/2+40, y*s)

    theta +=0.1
