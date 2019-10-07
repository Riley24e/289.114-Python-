import png
import pyqrcode 

qr = pyqrcode.create('4545436')
qr.png('myqr.png', scale=5)

def setup():
    size(1200,600,P3D)
    global num,qr
    num = createFont('TurretRoad-Medium.ttf',20)
    qr = loadImage('myqr.png')
    
    
    

    
    
r = 0

def draw():
    global num,qr,r
    background('#FFFFFF')
    stroke('#FFFFFF')
    strokeWeight(1)
    noFill()


    #card

    pushMatrix()
    noStroke
    fill('#cccccc')
    rect(200,100,800,400,10)
    fill('#aaaaaa')
    rect(200,100,805,405,10)
    
    popMatrix()
    
    #holo infomation
    
    pushMatrix()
    fill('#eeeeee')
    rect(250,150,390,250,10)
    popMatrix()
    
    #qr code
    image(qr,690,150,width*0.22,height*0.42)
    

    textFont(num)
    fill('#111111')
    

    #id
    text('ID:',270,200)
    text('19026005',295,200)
    #name
    text('Name:',270,230)
    text("trevor Stewart",330,230)
    #Date of birth
    text('D.O.B:',270,260)
    text("24/03/01",325,260)
    #county of origin
    text('Country:',270,290)
    text("NZ",355,290)
    #bank
    text('Bank:',270,320)
    text("One True Bank",325,320)
    
    #3d rotating icon (anti theft)
    pushMatrix()
    noFill()
    translate(550,265,0)
    rotateY(r)
    sphere(50)
    r += 0.01
    popMatrix()
    
    #black slip on bottom overlay rectanges to create barcode
    
