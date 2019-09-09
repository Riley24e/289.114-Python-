def setup():
    size(600,600)
    background('#004477')
    frameRate(20)
    
rainbow = [
     '#FF0000', '#FF9900', '#FFFF00',
     '#00FF00','#0099FF','#6633FF',     
]

sw = 7

def draw():
    global sw
    stroke(rainbow[frameCount % len(rainbow) ])
    strokeWeight(sw)
    
    if mousePressed:
        if mouseButton == LEFT:
            line(mouseX,mouseY,pmouseX,pmouseY)
            
        if mouseButton == RIGHT:
            sw += 1
        
        if mouseButton == CENTER:
            sw = 3
    
    colorMode(HSB , 360,100,100,100)
    h = float(mouseX)/width*360
    s = float(mouseY)/height*100
    b = 100
    a = 15
    fill(h,s,b,a)
    rect(-50,-50,width+100,height+100)
    
    noCursor()
    rectMode(CORNERS)
    fill(rainbow[frameCount % len(rainbow)])
    rect(mouseX,mouseY, pmouseX,pmouseY)
