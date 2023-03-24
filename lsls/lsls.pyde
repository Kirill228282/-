qaz = 20
wsx = 0
edc = 0

def setup():
    fullScreen()
def draw():
    frameRate(100)
    global qaz,wsx,edc
    clear()
    stroke(random(255),random(255),random(255))
    strokeWeight(qaz)
    point(wsx,edc)
    wsx += 1
    edc += 0.5
    qaz += 0.4
    
    













































































    
