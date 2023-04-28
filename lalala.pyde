q = 0
img = 0
def setup():
    global img
    img = loadImage("aaa.jpg")
    fullScreen()
    background(0)
    strokeWeight(100)
    textSize(100)
def draw():
    global q, img
    clear()
    image(img, -170,0,2260,1100)
    fill(255,255,255)
    text("0rel and Reshka", 550,100)
    fill(0)
    if keyPressed:
        q = random(1,2)
    if q < 1.5:
        text("0rel!",800,600)    
    if q > 1.5:
        text("Reshka!",720,600)
