size(600,700)
background('#004477')
stroke('#FFFFFF')
strokeWeight(3)
noFill()

#layer 2
fill('#ff0000')
arc(width/2,height/2, 500,500, PI,PI+1,PIE)

#layer 1
fill('#ff0000')
arc(width/2,height/2, 350,350, 5,PI*2,PIE) 

fill('#ff0000')
arc(width/2,height/2, 350,350, PI,5,PIE)  

fill('#ff0000')
arc(width/2,height/2, 350,350, 0/2,PI,PIE)   

fill('#004477')
ellipse(width/2,height/2,200,200)
