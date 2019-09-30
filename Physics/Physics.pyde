import pypybox2d as b2
from pypybox2d.common import *

def setup():
    size(600,600)
    frameRate(60)
    ernest = createFont ('Ernest.ttf', 3)
    textFont(ernest)
    global world
    world = b2.World(gravity =(0,-9.8) )
    
    #create bodies
    global ground
    ground = world.create_static_body(
        position =(20,20)
    )
    ground.create_polygon_fixture(
        vertices=[(0,0),(20,0),(20,10),(0,10)],
        user_data = ['ground','#ff9900']
        )
    
    global ball
    ball = world.create_dynamic_body(
      position=(20, 55)
    )
    ball.create_circle_fixture(
      1, density=1.0,
      user_data = ['ball', '#FF0000']
    )
    
def draw():
    background('#004477')
    noFill()
    
    world.step(1.0/frameRate,10,10)
    world.clear_forces()
    
    scale(1,-1)
    translate(0,-height)
    scale(10)
    
    # x/z corner marker
    
    stroke('#0099ff'); strokeWeight(3.0/10); fill('#0099ff')
    pushMatrix()
    scale(1,-1); text('x:1,y:1',2,-3); line(1,-1,1,-10); line(1,-1,12,-1)
    
    popMatrix()
    noFill(); noStroke()
    
    
    # render bodies

    pushMatrix()
    translate(ground.position.x, ground.position.y)
    fill(ground.fixtures[0].user_data[1])
    beginShape()
    vertex(ground.fixtures[0].shape._vertices[0].x, ground.fixtures[0].shape._vertices[0].y)
    vertex(ground.fixtures[0].shape._vertices[1].x, ground.fixtures[0].shape._vertices[1].y)
    vertex(ground.fixtures[0].shape._vertices[2].x, ground.fixtures[0].shape._vertices[2].y)
    vertex(ground.fixtures[0].shape._vertices[3].x, ground.fixtures[0].shape._vertices[3].y)
    endShape(CLOSE)
    popMatrix()
    
    pushMatrix()
    fill(ball.fixtures[0].user_data[1])
    translate(ball.position.x, ball.position.y)
    rotate(ball.angle)
    r = ball.fixtures[0].shape.radius;
    ellipse(0, 0, r*2, r*2)
    stroke('#FFFFFF'); strokeWeight(3.0/10); line(0,0,0,0.8); noStroke()
    popMatrix()
    ball.apply_force_to_center(force=(5,0))
    
    
    
