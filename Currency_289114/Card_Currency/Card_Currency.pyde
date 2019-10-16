import png
import pyqrcode

AccountBallance = '$1829'

qr = pyqrcode.create(AccountBallance)
qr.png('code.png', scale=5)



def setup():
    size(1200,600,P3D)
    global num,qr,Name,DOB,Country,Bank,colors
    num = createFont('TurretRoad-Medium.ttf',20)
    qr = loadImage('code.png')
    
    
    
ID= '19026005'
Name= 'Trevor Stewart'
DOB= '24/03/01'
Country= 'NZ'
Bank='One True Bank'
Expiry ='29/12/22'
b= random(-20,20)
c= random(-20,20)
d= random(-20,20)
e= random(-20,20)
f= random(-20,20)
g= random(-20,20)
h= random(-20,20)
i= random(-20,20)
j= random(-20,20)
k= random(-20,20)
colors = ['#FF4D4D','#AB4DFF','#4DC2FF','#4DFF75','#F0FF4D','#AAAAAA']
ran= int(random(0,5))

    
    
r = 0

def draw():
    global num,qr,r,ID,Name,DOB,Country,Bank,b,c,d,e,f,g,h,i,j,k,colors,ran,Expiry
    background('#004477')
    stroke('#FFFFFF')
    strokeWeight(1)
    noFill()


    #card

    pushMatrix()
    noStroke()
    fill(colors[ran])
    rect(200,100,800,400,10)
    
    fill('#ffffff')

    beginShape()
    vertex(650,100)
    vertex(1000,100)
    vertex(1000,500)
    vertex(550,500)
    endShape()

    
    popMatrix()
    
    #holo infomation
    
    pushMatrix()
    fill('#ffffff')
    rect(270,170,400,250,10)
    popMatrix()
    
    #qr code
    image(qr,690,170,width*0.22,height*0.42)
    

    textFont(num)
    fill('#111111')
    

    #id
    text('ID:',295,220)
    text(ID,320,220)
    #name
    text('Name:',295,250)
    text(Name,355,250)
    #Date of birth
    text('D.O.B:',295,280)
    text(DOB,350,280)
    #county of origin
    text('Country:',295,310)
    text(Country,380,310)
    #bank
    text('Bank:',295,340)
    text(Bank,350,340)
    #expiry
    text('Expiry Date:',295,370)
    text(Expiry,410,370)
    
    #3d rotating icon (anti theft)
    stroke('#111111')
    pushMatrix()
    noFill()
    translate(600,300,0)
    rotateY(r)
    sphere(50)
    r += 0.01
    popMatrix()
    
    #black slip on bottom overlay rectanges to create barcode
    fill('#111111')
    rect(200,450,20,50,1,1,1,10)
    rect(230 + b ,450,20,50)
    rect(260+ c,450,20,50)
    rect(290+ d,450,20,50)
    rect(320+ e,450,20,50)
    rect(350+ f,450,20,50)
    rect(380+ g,450,20,50)
    rect(410+ h,450,20,50)
    rect(440+ i,450,20,50)
    rect(470+ j,450,20,50)
    rect(500+ k,450,20,50)
    
