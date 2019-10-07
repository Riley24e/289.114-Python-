def setup():
    size(600,600,P3D)
    global img
    img = loadImage('pine.jpg')
    
    
r = 0

def draw():
    global r
    background('#004477')
    stroke('#FFFFFF')
    strokeWeight(1)
    fill('#FF0000')
    translate(width/2, height/2)
    

    
    rotateY(r)
    translate(0,0,0)
    #sphere(200)
    
    r+=0.01
    
    beginShape()
    texture(img)
    textureWrap(CLAMP)
    vertex(-100,-100,-100)
    vertex(100,-100,-100)
    vertex(0,0,100)
    
    vertex(100,-100,-100)
    vertex(100,100,-100)
    vertex(0,0,100)
    
    vertex(100,100,-100)
    vertex(-100,100,-100)
    vertex(0,0,100)
    
    vertex(-100,100,-100)
    vertex(-100,-100,-100)
    vertex(0,0,100)
    
    endShape()
    
    box(40)
