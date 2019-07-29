size(600,600)
background('#004477')
noFill()
strokeWeight(3)
stroke('#FFFFFF')

fill('#FFFFFF')

i=1
x1=50
y1=50
x2=95
y2=50
x3=95
y3=95
x4=50
y4=95
a=-1
b=2


while i < 65:
   quad((x1+(random(a,b))),(y1+(random(a,b))),(x2+(random(a,b))),(y2+(random(a,b))),(x3+(random(a,b))),(y3+(random(a,b))),(x4+(random(a,b))),(y4+(random(a,b))))
   x1+=65
   x2+=65
   x3+=65
   x4+=65
   
   if x1 >= 550:
       y1+=65
       y2+=65
       y3+=65
       y4+=65
       x1=50
       x2=95
       x3=95
       x4=50
       a-=5
       b+=5
   i+=1
   

    
