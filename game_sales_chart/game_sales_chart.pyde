size(800,800)
background('#004466')
noStroke()
csv = loadStrings('list_of_best-selling_video_games.csv')

tetrisentry = csv[1].split('\t')

print(int(tetrisentry[1]) + 1)
