logo = None
x = 0
xspeed = 2
y = 0
yspeed = 2

def setup():
    global logo
    size(800,600)
    logo = loadImage('dvd-logo.png')
    
def draw():
    global x
    global y
    global xspeed
    global yspeed
    background('#000000')
    image(logo,x,y)
    x += xspeed
    y += yspeed
    
    if y+45 > height or y < 0:
        yspeed *= -1
        
    elif x+100 > width or x < 0:
        xspeed *= -1


        
    
