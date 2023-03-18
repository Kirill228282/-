asdf = 940
asdfg = 545
asdfgh = 150
qwerty = 940
qwertyu = 545
qwertyui = 150
zxc = 940
asd = 545
qwe = 150
qaz = 940
wsx = 545
edc = 150
def setup():
    fullScreen()
    background(0)
def draw():
    fill(random(0,255),random(0,255),random(0,255))
    noStroke()
    clear()
    frameRate(200000)
    global zxc,asd,qwe
    zxc = zxc+1
    asd = asd-1
    ellipse(zxc,asd,qwe,qwe)
    fill(random(0,255),random(0,255),random(0,255))
    global qwerty,qwertyu,qwertyui
    qwerty = qwerty+1
    qwertyu = qwertyu+1
    ellipse(qwerty,qwertyu,qwertyui,qwertyui)
    fill(random(0,255),random(0,255),random(0,255))
    global asdf,asdfg,asdfgh
    asdf = asdf-1
    asdfg = asdfg+1
    ellipse(asdf,asdfg,asdfgh,asdfgh)
    fill(random(0,255),random(0,255),random(0,255))
    global qaz,wsx,edc
    qaz = qaz-1
    wsx = wsx-1
    ellipse(qaz,wsx,edc,edc)
