import png
import pyqrcode

AccountBallance = '$1825'

qr = pyqrcode.create('$55654655' )
qr.png('code.png', scale=5)

def setup():
    size(1200,600,P3D)
    global num,qr,Name,DOB,Country,Bank
    num = createFont('TurretRoad-Medium.ttf',20)
    qr = loadImage('code.png')
    
    
    
ID= '19026005'
Name= 'Trevor Stewart'
DOB= '24/03/01'
Country= 'NZ'
Bank='One True Bank'

    
    
r = 0

def draw():
    global num,qr,r,ID,Name,DOB,Country,Bank
    background('#004477')
    stroke('#FFFFFF')
    strokeWeight(1)
    noFill()


    #card

    pushMatrix()
    noStroke
    fill('#cccccc')
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
    
