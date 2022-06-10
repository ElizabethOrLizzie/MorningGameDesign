#Maria Suarez
#6/9/2022
#We are learning pygame basic functins, 
# creating screens, clrs, shape ,move 
# move  the square
# K_UP                  up arrow
# K_DOWN                down arrow
# K_RIGHT               right arrow
# K_LEFT                left arrow
#picture = pygame. image. load(filename)
#picture = pygame. transform. scale(picture, (1280, 720))
#bg=pygame.image.load('ClassStuff\CircleEatsSquare\Images\\bgSmaller.jpg')
from cv2 import insertChannel, sqrt
import random
import math
import pygame, time,os
pygame.init()#initialize the pygame package
os.system('cls')
WIDTH=700 #like constant
HEIGHT=700
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51)}
clr=colors.get("limeGreen")
#create dispay wind with any name y like
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("My First Game")  #change the title of my window
bg=pygame.image.load('MorningGameDesign\PygameFiles\Images\Backgroundimagepurplerock.jpg')
screen.blit(bg)
dude=pygame.image('MorningGameDesign\PygameFiles\Images\PixelArtTutorialCharacter.png')
dude = pygame. transform. scale(dude, (1280, 720))


#square Var
hb=50
wb=50
xb=100
yb=300
cx=350
cy=350
rad=25
ibox=rad*math.sqrt(2)
xig= cx-(ibox/2)
yig= cy-(ibox/2)
inscribSq=pygame.Rect(xig,yig,ibox,ibox)
square=pygame.Rect(xb,yb,wb,hb)# create the object to draw
squareClr=colors.get("pink")
#keep running create a lp
circleClr=colors.get("blue")
backgrnd=colors.get("limeGreen")
run = True
#create var mve
speed=2
cx=350
cy=350
rad=25
while run:
    screen.blit(bg)
    screen.fill(backgrnd)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            print("Y quit")
    keys= pygame.key.get_pressed() #this is a list
    if keys[pygame.K_RIGHT] and square.x < WIDTH -(wb):
        square.x += speed
    if keys[pygame.K_LEFT] and  square.x > speed:
        square.x -= speed
    if keys[pygame.K_UP] and square.y >speed:   #means clser t 0
        square.y -= speed
    if keys[pygame.K_DOWN] and square.y <HEIGHT -hb:  #means clser t max value HEIGHT
        square.y += speed
        #move circle
    if keys[pygame.K_d] and cx < WIDTH -(rad):
        cx += speed
        inscribSq.x += speed
    if keys[pygame.K_a] and  cx > speed+rad:
        cx -= speed
        inscribSq.x -= speed
    if keys[pygame.K_w] and cy >speed+rad:   #means clser t 0
        cy -= speed
    if keys[pygame.K_s] and cy <HEIGHT -(rad):  #means clser t max value HEIGHT
        cy += speed
        inscribSq.y += speed
    if square.collidepoint(cx,cy):
        cx=random.randint(rad,WIDTH-rad)
        cy=random.randint(rad,HEIGHT-rad)
        print("BOOM")
        ibox=rad*math.sqrt(2)
        xig= cx-(ibox/2)
        yig= cy-(ibox/2)
        inscribSq=pygame.Rect(xig,yig,ibox,ibox)
    #rect(surface, color, rect) -> Rect
    pygame.draw.rect(screen, squareClr,square)
    screen.blit/dude
    #circle(surface, color, center, radius)
    pygame.draw.circle(screen, circleClr, (cx,cy), rad)
    pygame.draw.rectangle(screen, squareClr, inscribSq)
    pygame.display.update()

