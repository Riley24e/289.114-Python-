
size(300, 300)
translate (150,150)
noStroke()
# background will be desided by the hour so will the seconday shape color
colors = [
 '#FF171F',
 '#FF8817',
 '#FFF417',
 '#1720FF',
 '#17A8FF',
 '#A117FF',
 '#63E80C',
 '#030303',
 '#FFFFFF',
 '#FA00C0',
 '#00FAE7',
 '#837D7D',
 '#AF00F0',
 '#6984E3',
 '#0D226C',
 '#3E6C0D',
 '#FCC97A',
 '#FFA51C',
 '#FC908C',
 '#8CFCA0',
 '#3CA8CE',
 '#29C153',
 '#B129C1',
 '#F38BFF',
]
h = hour()
background(colors[h])

#rotate sketch
rotate(PI/random(2,9))

num = 1


#select first shape
fill('#ffffff')
sh = int(random(0,3))
    
if sh == 0:
    rect(-100, -100, 200,200)
elif sh == 1:
    ellipse(0, 0, 200, 200)
elif sh == 2:
    triangle( -100,100, 0,-100, 100,100)
    
    
while num < 12:
    #select the second shape should have same colour as back ground
    fill(colors[int(random(1,24))])
    
    rd = int(random(0,3))
    
    if rd == 0:
        triangle( random(-150,100),random(50,150),random(-50,50),random(-150,100),random(50,150),random(50,150))
    elif sh == 1:
        ellipse(random(-75,75), random(-75,75), random(175,275), random(175,275)),
    elif sh == 2:
        quad(random(-100,0),random(-100,0), random(0,100),random(-100,0), random(0,100),random(0,100), random(-100,0),random(0,100))
        
    num+=1
    
#select first shape
fill('#ffffff')
sh = int(random(0,3))
    
if sh == 0:
    rect(-100, -100, 200,200)
elif sh == 1:
    ellipse(0, 0, 200, 200)
elif sh == 2:
    triangle( -100,100, 0,-100, 100,100)
    
    
    
    
    







#select the second shape should have same colour as back ground
fill(colors[h])
