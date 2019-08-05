y = 1

def setup():
    size(500,500)
    noFill()
    stroke('#FFFFFF')
    strokeWeight(3)

    
def draw():
    global y
    background('#004477')
    y += 1
    ellipse(height/2,y,47,47)
    
    if frameCount % 100 == 0:
        saveFrame()
    
