size(500,380,)
background('#004477')
noFill()
stroke('#FFFFFFF')
strokeWeight(3)

h = 50
translate(100,40)

# 0 dimentional
bands = 6
rect(0,0,40,h*bands)

# 1 dimensional
bands = [
 '#FF0000',
 '#FF9900',
 '#FFFF00',
 '#00FF00',
 '#0099FF',
 '#6633FF'
]

for i in range(len(bands)):
    fill(bands[i])
    rect(0,i*h,40,h)
    

#2 dimentional
bands=[
[100, 0, 0, 'red'],
[100, 60, 0, 'orange'],
[100, 100, 0, 'yellow'],
[0, 100, 0, 'green'],
[0, 60, 100, 'blue'],
[40, 20, 100,'violet']    
]

colorMode(RGB, 100)
for i in range(len(bands)):
    r = bands[i][0]
    g = bands[i][1]
    b = bands[i][2]
    #sum = r + g+ b
    #avg = sum/3
    #fill(avg, avg, avg)
    #rect(0,i*h, sum,h)
    fill('#FF0000')
    rect(0,i*h, r ,h)
    fill('#00FF00')
    rect(0 +r, i*h,g,h)
    fill('#0000FF')
    rect(0 +r+g, i*h,b,h)
    fill('#FFFFFF')
    text(bands[i][3],-60, i*h+30)
    
    
    
