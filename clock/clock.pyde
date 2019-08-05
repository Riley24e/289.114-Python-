def setup():
    size(600,600)
    noFill()
    stroke('#FFFFFF')
    
def draw():
    background('#004477')
    translate(width/2,height/2)
    strokeWeight(3)
    ellipse(0,0,350,350)
    
    rotate(-PI/2)
    #hourhand
    pushMatrix()
    print(hour())
    h = TAU/12 * hour()
    rotate(h)
    strokeWeight(10)
    line(0,0,100,0)
    popMatrix()
    
    #minutehand
    pushMatrix()
    m=TAU/60 * minute()
    rotate(m)
    strokeWeight(5)
    line(0,0,130,0)
    popMatrix()
    
    #secondhand
    pushMatrix()
    s=TAU/60 * second()
    rotate(s)
    strokeWeight(3)
    line(0,0,130,0)
    popMatrix()
    
