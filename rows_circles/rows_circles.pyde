size(500,500)
background('#004477')
noFill()
strokeWeight(3)
stroke('#FFFFFF')



i=1
col=100
row=100
while i < 17:
    ellipse(col,row,80,80)
    col += 100
    
    if col > 400:
        row +=100
        col = 100
    i +=1
        
    

    
