add_library('controlP5')

def setup():
    size(720,485)
    global cp5
    cp5 = ControlP5(this)
    
    (cp5.addTextfield('alias')
        .setPosition(500,20)
        .setSize(200,25)
     )
    
    (cp5.addSlider('eye distance')
        .setPosition(500,80)
        .setSize(200,20)
        .setRange(30,120)
        .setValue(80)
     )
    (cp5.getController('eye distance')
     .getCaptionLable()
     .align(ControlP5.LEFT, ControlP5.BOTTOM_OUTSIDE)
     .setPaddingX(0)
     )
    
def draw():
    background('#004477')
    stroke('#FFFFFF')
    strokeWeight(3)
    axis = 250
    
    #face
    noFill()
    ellipse(axis,220,370,370)
    
    #alis
    fill('#ffffff')
    textSize(20)
    textAlign(CENTER)
    alias = cp5.getController('alias').getText()
    text(alias, axis,450)
    noFill()
    
    
    
