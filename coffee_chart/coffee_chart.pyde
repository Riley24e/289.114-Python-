size(800,800)
background('#004477')

mug = 110
col = 1
row = 1
tex= 0

coffees = [
  { 'name':'cafe con leche','espresso':50, 'hotwater':0, 'steamedmilk':30,'foamedmilk':0  },
  { 'name':'espresso',      'espresso':60, 'hotwater':0, 'steamedmilk':0, 'foamedmilk':0  },
  { 'name':'demi-creme',    'espresso':40, 'hotwater':0, 'steamedmilk':40,'foamedmilk':0  },
  { 'name':'americano',     'espresso':60, 'hotwater':30,'steamedmilk':0, 'foamedmilk':0  },
  { 'name':'capucchino',    'espresso':40, 'hotwater':0, 'steamedmilk':30,'foamedmilk':30 },
  { 'name':'latte',         'espresso':35, 'hotwater':0, 'steamedmilk':10,'foamedmilk':30 },
  { 'name':'ristretto',     'espresso':30, 'hotwater':0, 'steamedmilk':0, 'foamedmilk':0  },
  { 'name':'macchiato',     'espresso':40, 'hotwater':0, 'steamedmilk':0, 'foamedmilk':60 },
  { 'name':'flat white',    'espresso':40, 'hotwater':0, 'steamedmilk':60,'foamedmilk':0  },
]


for coffee in coffees:
    
    x = width/4*col
    y= height/4*row
    
   #text
   

    
    #espresso
    fill('#5A4040')
    strokeWeight(0)
    rect(x-mug/2,y-mug/2+mug,mug,-coffee['espresso'])
    
    #hotwater
    fill('#4BAFFF')
    strokeWeight(0)
    rect(x-mug/2,y-mug/2+mug-coffee['espresso'],mug,-coffee['hotwater'])
    
    #steamedmilk
    fill('#FFFFFF')
    strokeWeight(0)
    rect(x-mug/2,y-mug/2+mug-coffee['espresso']-coffee['hotwater'],mug,-coffee['steamedmilk'])
    
    #foamedmilk
    fill('#EAEAEA')
    strokeWeight(0)
    rect(x-mug/2,y-mug/2+mug-coffee['espresso']-coffee['hotwater']-coffee['steamedmilk'],mug,-coffee['foamedmilk'])
    
    
     #mug
    stroke('#FFFFFF')
    strokeWeight(3)
    noFill()
    arc(x+55,y,40,40,-HALF_PI, HALF_PI)
    arc(x+55,y,65,65,-HALF_PI, HALF_PI)
    rect(x-mug/2,y-mug/2,mug,mug)
    
    if col%3 == 0:
        row += 1
        col = 1
        tex += 1
    else:
        col += 1
        tex += 1
        
