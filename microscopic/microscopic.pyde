from amoeba import Amoeba

def setup():
    size(800,800)

amoebas = []

for i in range (50):
    amoebas.append( Amoeba(
        random(900), # x
        random(900), # y
        random(-0.5,0.5), # xspeed
        random(-0.5,0.5), # ySpeed
        random(50,200)
        ))
        

def draw():
    background('#004477')
    
    for amoeba in amoebas:
        
        #mouse interaction
        
        mouse = PVector(mouseX,mouseY-amoeba.diameter/2)
        goto = PVector.sub(mouse,amoeba.location)
        goto.div(10000)
        
        if mousePressed:
            goto.mult(-1)
        
        amoeba.velocity.add(goto)
        
        amoeba.velocity.limit(0.5)
        
        
        
        
        amoeba.update()
        
