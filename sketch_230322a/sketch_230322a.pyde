zxc = 930
zxcv = 530
qwe = 2300
asd = 2300
def setup():
    fullScreen()
def draw():
    global zxc,zxcv,qwe,asd
    fill(random(0,255),random(0,255),random(0,255))
    frameRate(1000)
    clear()
    ellipseMode(CENTER)
    ellipse(zxc,zxcv,qwe,asd)
    qwe -= 5
    asd -= 5
    
    
