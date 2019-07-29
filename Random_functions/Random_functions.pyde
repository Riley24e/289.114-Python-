size(600,600)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)

randomSeed(12)

for i in range(100):
    point(random(width), random(height))
