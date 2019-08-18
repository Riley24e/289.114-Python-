size(300, 300)

bg = {
 'red': '#FF171F',
 'orange': '#FF8817',
 'yellow': '#FFF417',
 'blue': '#1720FF',
 'light blue': '#17A8FF',
 'violet': '#A117FF',
 'green': '#63E80C',
 'black': '#030303',
 'white': '#FFFFFF',
 'pink': '#FA00C0',
 'cyan': '#00FAE7',
 'light green': '#00FA9C',
 }

sh={
 'square': rect(100, 100, 100, 100),
 'circle': ellipse(100, 100, 100, 100),
}

# background will be desided by the hour
h = hour()
background(bg[h])
