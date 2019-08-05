def setup():
    frameRate(25)
    size(500,500)
    
    noFill()
    stroke('#FFFFFF')
    strokeWeight(3)
    
def draw():
    background('#004477')
    if frameCount%2 == 0:
        ellipse(250,140,47,47)
    else:
        ellipse(250,height-140,47,47)
    
