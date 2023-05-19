z = 0
bg=0
def setup():
    size(750,750)
    z = loadImage("kkk.jpg")
def draw():
    global z,bg
    rect(300,300,150,150)
    background(bg)
def mouseClicked():
    global z,bg
    if mouseX < 300 and mouseX > 450 and mouseY < 300 and mouseY > 450:
        bg = image(z, 300,300,150,150)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
