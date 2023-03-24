z = 5
def setup():
    size(700,700)
    background(255,255,255)

def draw():
    stroke(random(255))
    frameRate(60)
    global z
    strokeWeight(z)
    ellipse(350,350,695,695)
    line(525,648,350,0)
    line(173,648,350,0)
    line(525,648,13,270)
    line(15,270,686,270)
    line(173,648,686,270)

    z += 0.2
























































































































    
