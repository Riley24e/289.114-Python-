size(800,800)
background('#004466')
noStroke()
csv = loadStrings('list_of_best-selling_video_games.csv')

tetrisentry = csv[1].split('\t')

print(int(tetrisentry[1]) + 1)
i = 1

fill('#FF0303')
stroke('#FFFFFF')
strokeWeight(1)

for game in csv:
    rect(0,1*i,p,16)
    i += 16
