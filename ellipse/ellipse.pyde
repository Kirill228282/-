zxc = 0
w = 170
zxcv = 0
def setup():
    fullScreen()
    background(0)
    
def draw():
    clear()
    frameRate(57777)
    global zxc
    global w
    global zxcv
    zxcv = zxcv+2
    zxc = zxc+1
    fill (random(1,255),random(1,255),random(1,255))
    ellipse(zxcv,zxc,w,w)
