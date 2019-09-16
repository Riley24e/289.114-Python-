def setup():
    size(800,800)
    background('#004477')
    strokeWeight(3)
    
def parabola(x):
    return x*x

def circle(t):
    x = cos(t)
    y = sin(t)
    return [x,y]

def lissajous(t,a,b,kx,ky):
    x = a*cos(kx*t)
    y = b*sin(ky*t)
    return [x,y]
    
    
x = -300.0
y = 0.0
t = 0.0
h = 1

def draw():
    global x,y,t,h
    colorMode(HSB,360,100,100,100)
    fill(0,0,0,15)
    
    rect(-10,-10,width+20,height+20)
    translate(width/2,height/2)
    '''
    stroke('#0099ff')
    line(width/2*-1,0,width/2,0)
    line(0,width/2*-1,0,width/2,)

    stroke('#ffffff')

    y = parabola(x)
    point(x,y)
    x += 1

    xy = circle(t)
    x = xy[0] * 100
    y = xy[1] * 100
    point(x,y)
    t += 0.01

    
    xy = lissajous(t,100,100,3,2)
    point(xy[0],xy[1])
    
    t += 0.01
    
    stroke('#ff0000')
    
    xy = lissajous(t,300,150,154,693)
    point(xy[0],xy[1])
    
    t += 0.01
    '''

    xy1 = lissajous(t,2,1,3,1)
    x1 = xy1[0]*100
    y1 = xy1[1]*100
    
    xy2 = lissajous(t,5,6,1,3)
    x2 = xy2[0]*100
    y2 = xy2[1]*100
    
    xy3 = lissajous(t,7,2,4,4)
    x3 = xy3[0]*100
    y3 = xy3[1]*100
    
    stroke(h,100,100,100)
    line(x1,y1,x2,y2)
    line(x2,y2,x3,y3)
    line(x3,y3,x1,y1)
    
    
    xy4 = lissajous(t,7,3,2,1)
    x4 = xy4[0]*100
    y4 = xy4[1]*100
    
    xy5 = lissajous(t,6,3,4,1)
    x5 = xy5[0]*100
    y5 = xy5[1]*100
    
    xy6 = lissajous(t,5,4,3,3)
    x6 = xy6[0]*100
    y6 = xy6[1]*100
    
    stroke(h+180,100,100,100)
    line(x4,y4,x5,y5)
    line(x5,y5,x6,y6)
    line(x6,y6,x4,y4)
    
    
    t += 0.01
    h += 1
    
    if h >360:
        h=1
    
    
