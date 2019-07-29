size(600,600)
noFill()
noStroke()

fill('#FF0000') #red
rect(width/2,0, width/2, height/2)

fill('#004477') #blue
rect(0,0, width/2, height/2)

fill('#6633FF') #violet
rect(0,width/2,width/2,height/2)

fill('#FF9900') #orange
rect(width/2,width/2,width/2,height/2)

x = 400
y = 200
txt = '?'

if  x < width/2 and y < height/2:
    txt = 'B'

if x <= 0:
    txt = 'V'
    
if y > width/2 and y > height/2:
    txt = '0'

if x >= width/2 and y <= height/2:
    txt = 'R'



fill('#FFFFFF')
textSize (40)
textAlign (CENTER, CENTER)
text(txt, x,y)
