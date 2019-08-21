size(300, 300)
translate (150,150)
noStroke()


R=[
'#FF0303',
'#E00000',
'#C10202',
'#FC4A4A',
'#A72E2E',
'#EA2F2F'
]

B=[
'#030CFF',
'#555CFF',
'#070C86',
'#0A69C6',
'#4292E0',
'#1CAEFA'
]

G=[
'#05FF03',
'#82FF81',
'#09AA07',
'#0B710A',
'#8BFF2E',
'#43ED63'    
]



background(R[1])
x=1
num = 1
while num < 120:
    #select the second shape should have same colour as back ground
    fill(R[x])
    
    rd = int(random(0,2))
    
    if rd == 0:
        ellipse(random(-175,175), random(-175,175), random(100,150), random(100,150)),
    elif rd == 1:
        quad(random(-100,0),random(-100,0), random(0,100),random(-100,0), random(0,100),random(0,100), random(-100,0),random(0,100))
        
    num+=1
    x+=1
    
    if x==6 :
        x=1


#select first shape
fill('#ffffff')
sh = int(random(0,3))
    
if sh == 0:
    rect(-100, -100, 200,200)
elif sh == 1:
    ellipse(0, 0, 200, 200)
elif sh == 2:
    triangle( -100,100, 0,-100, 100,100)


saveFrame()
