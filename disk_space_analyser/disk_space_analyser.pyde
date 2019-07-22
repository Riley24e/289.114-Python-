size(600,700)
background('#004477')
stroke('#FFFFFF')
strokeWeight(3)
noFill()

#layer 3
fill('#00FC6F')
arc(width/2,height/2, 650,650, PI+1.85,PI+2.3,PIE)

#layer 2
fill('#FF6FF1')
arc(width/2,height/2, 500,500, PI,PI+0.925,PIE)

fill('#FF6FF1')
arc(width/2,height/2, 500,500,PI+0.925,PI+1.85,PIE)

fill('#00A6FC')
arc(width/2,height/2, 500,500,PI+1.85,PI+2.71,PIE)

fill('#00A6FC')
arc(width/2,height/2, 500,500,PI+2.71,PI*2,PIE)

#layer 1
fill('#8121FF')
arc(width/2,height/2, 350,350, 5,PI*2,PIE) 

fill('#FF21CF')
arc(width/2,height/2, 350,350, PI,5,PIE)  

fill('#ff0000')
arc(width/2,height/2, 350,350, 0/2,PI,PIE)   

fill('#004477')
ellipse(width/2,height/2,200,200)
