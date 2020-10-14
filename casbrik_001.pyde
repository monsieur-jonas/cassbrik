ballX = 0
ballY = 0
ballSpeedX = 4
ballSpeedY = 4
ballRadius = 7
racketWidht = 50
racketX = 0
racketY = 0


def setup():
    global ballX, ballY, racketX, racketY, racketWidht
    print("game start")
    size(800, 600)
    clear()
    fill(0)
    frameRate(60)
    ballX = width/2
    ballY = height/2
    
    racketX = mouseX - (racketWidht/2)
    racketY = height - 20


def draw():
    clear()
    drawRacket()
    drawBall()

def drawRacket():
    global racketWidht, racketHeight, racketX, racketY, ballSpeedY, ballY
    fill(255, 201, 14)
    racketX = mouseX - (racketWidht/2)
    rect(racketX, racketY , racketWidht, 10, 0, 0, 7, 7)

    
        
                
    if(ballY+ballRadius > racketY and ballSpeedY > 0):
        if (racketX < ballX < racketX + racketWidht):
            ballSpeedY *= -1
            ballY = racketY - ballRadius
    
            
    if(racketY < ballY-ballRadius < racketY + racketX and ballSpeedY > 0):
        ballSpeedY *= -1
        ballY = racketY - ballRadius
    
def drawBall():
    global ballX, ballY, ballSpeedX, ballSpeedY, ballRadius, racketHeight
    fill(255)
    
    ballX += ballSpeedX
    ballY += ballSpeedY
    
    #bas
    if(ballY+ballRadius > height):
        ballSpeedY *= -1
        ballY = height-ballRadius
        print("game over")
    
    #haut    
    elif(ballY-ballRadius < 0):
        ballSpeedY *= -1
        ballY = ballRadius
    
    #gauche   
    if(ballX-ballRadius < 0):
        ballSpeedX *= -1
        ballX = ballRadius
        
         #droite
    elif(ballX+ballRadius > width):
        ballSpeedX *= -1
        ballX = width-ballRadius
        
    
        
    fill(0, 128, 255)    
    circle(ballX, ballY, 2*ballRadius)
        
