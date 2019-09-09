def setup():
    size(600,600)
    background('#004477')
    wendy = createFont('wendy.ttf', 20)
    textFont(wendy)
    noStroke()
    noLoop()
    
rainbow = [
     '#FF0000', '#FF9900', '#FFFF00',
     '#00FF00','#0099FF','#6633FF', '#004477',   
]

brushcolor = rainbow[0]
brushshape = ROUND
brushsize = 3
painting = False
paintmode = 'free'

def mousePressed():
    if mouseButton == LEFT:
        loop()
        
    global brushcolor,brushshape,brushsize
    
    if mouseX < 30:
        if mouseY < 30:
            brushcolor = rainbow[0]
        elif mouseY < 60:
            brushcolor = rainbow[1]
        elif mouseY < 90:
            brushcolor = rainbow[2]
    elif mouseX < 60:
        if mouseY < 30:
            brushcolor = rainbow[3]
        elif mouseY < 60:
            brushcolor = rainbow[4]
        elif mouseY < 90:
            brushcolor = rainbow[5]
            
    global clearall
    
    if mouseY > height - 30 and mouseX < 60:
        clearall = True
        redraw()
    if mouseY > height - 60 and mouseX < 60:
        brushcolor = rainbow [6]
       
    
def mouseReleased():
    noLoop() 
    global painting
    painting = False
    
def mouseWheel(e):
    print(e)
    global brushsize, paintmode
    
    paintmode = 'select'
    brushsize = e.count
    
    if brushsize < 3 :
        brushsize = 3
    if brushsize > 45:
        brushsize = 45
    
    redraw()
    
clearall = False

def draw():
    global painting, paintmode
    print(frameCount)
    
    if mouseX < 60:
        paintmode = "select"
        
    
    if paintmode == 'free':
        if not painting and frameCount > 1:
            line(mouseX,mouseY,pmouseX,pmouseY)
            painting = True
        elif painting:
            stroke(brushcolor)
            strokeCap(brushshape)
            strokeWeight(brushsize)
            line(mouseX,mouseY,pmouseX,pmouseY)
    #black panle
    noStroke()
    fill('#000000')
    rect(0,0,60,height)
    
    #color palette
    fill(rainbow[0]); rect(0,0,30,30)
    fill(rainbow[1]); rect(0,30,30,30)
    fill(rainbow[2]); rect(0,60,30,30)
    fill(rainbow[3]); rect(30,0,30,30)
    fill(rainbow[4]); rect(30,30,30,30)
    fill(rainbow[5]); rect(30,60,30,30)
    
    #brush preview
    fill(brushcolor)
    if brushshape == ROUND:
        ellipse(30,123, brushsize,brushsize)
        
    paintmode = 'free'
    
    #clear button
    global clearall
    fill('#FFFFFF')
    text('clear',10,height-12)
    
    if clearall:
        fill('#004477')
        rect(60,0,width,height)
        clearall = False
        
    #erase
    fill('#FFFFFF')
    text('Erase',10,height-32)
    
            
    
    
