# Elizabeth Nassi
# #6/14/22
# #We are learning pygame basic functins, 
# # creating screens, clrs, shape ,move 
# # move  the square
# # K_UP                  up arrow
# # K_DOWN                down arrow
# # K_RIGHT               right arrow
# # K_LEFT                left arrow
# #picture = pygame. image. load(filename)
# #picture = pygame. transform. scale(picture, (1280, 720))
# #bg=pygame.image.load('ClassStuff\CircleEatsSquare\Images\\bgSmaller.jpg')

import sys
import pygame, time,os,random, math, datetime
date=datetime.datetime.now()
pygame.init()#initialize the pygame package

# print(pygame.font.get_fonts())
# pygame.time.delay(10000)
TITLE_FONT = pygame.font.SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 20)

os.system('cls')
clock = pygame.time.Clock
WIDTH=700 #like constant
w = WIDTH
HEIGHT=700
h = HEIGHT
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51)}
clr=colors.get("limeGreen")
message=['Instructions', 'Settings', 'Game 1', 'Game 2', 'Scoreboard', 'Exit']
#create dispay wind with any name y like
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("My First Game")  #change the title of my window
Bx=WIDTH//3
#boxes for menu
Button_menu=pygame.Rect(Bx, 125, WIDTH//4, 40)
Button_instruct=pygame.Rect(Bx, 150, WIDTH//4, 40)
Button_settings=pygame.Rect(Bx, 200, WIDTH//4, 40)
Button_Game1=pygame.Rect(Bx, 250, WIDTH//4, 40)
Button_Game2=pygame.Rect(Bx, 300, WIDTH//4, 40)
Button_score=pygame.Rect(Bx, 350, WIDTH//4, 40)
Button_exit=pygame.Rect(Bx, 400, WIDTH//4, 40)
#images
bg=pygame.image.load('MorningGameDesign\PygameFiles\Images\Backgroundimagepurplerock.jpg')
char = pygame.image.load('MorningGameDesign\PygameFiles\Images\PixelArtTutorialCharacter.png')
char = pygame.transform.scale(char, (50, 50))
# screen.blit(bg, (0,0))
# pygame.display.update()
# pygame.time.delay(5000)


#square Var
hb=50
wb=50
xb=100
rad=25
yb=300

charx = xb
chary = yb
txtcolor="blue"
bgcolor="white"
cx=350
cy=350
speed=2
ibox = rad*math.sqrt(2)
xig = cx-(ibox/2)
yig = cy-(ibox/2)

#mouse varuables
mx = 0
my = 0

score = 0
name = "Maria" #in settings add option change name

square=pygame.Rect(xb,yb,wb,hb)# create the object to draw
insSquare=pygame.Rect(xig,yig,ibox,ibox)
squareClr=colors.get("pink")
#keep running create a lp
mountainSquare=pygame.Rect(250,320,180,250)
circleClr=colors.get("blue")
backgrnd=colors.get("limeGreen")
run = True
Game = False

def mainMenu():
    pygame.draw.rect(screen, colors.get('limeGreen'), Button_settings)
    Title = TITLE_FONT.render("Circle eats Square Menu", 1, colors.get(txtcolor))
    screen.fill(colors.get(bgcolor))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))
    yMenu=150
    
    for item in message:
        Button_menu=pygame.Rect(274, yMenu, 125, 40)
        text=MENU_FONT.render(item, 1, colors.get(txtcolor))
        pygame.draw.rect(screen, colors.get('limeGreen'), Button_menu)
        screen.blit(text, (280, yMenu))
        pygame.display.update()
        pygame.time.delay(50)
        yMenu += 50
    MENU=True
    while MENU:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                mainMenu()
                print("You quit")
                MENU=False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_instruct.collidepoint((mx, my)):
                    Instructions()
                if Button_settings.collidepoint((mx, my)):
                    settings()
                if Button_Game1.collidepoint((mx, my)):
                    GameOne()
                if Button_score.collidepoint((mx, my)):
                    scoreboard()
                if Button_exit.collidepoint((mx, my)):
                    exit()
                if Button_Game2.collidepoint((mx, my)):
                    GameTwo()
    
def Instructions():
    global txtcolor, bgcolor
    #rendering text objects
    Title = TITLE_FONT.render("Instructions", 1, colors.get(txtcolor))

    #fills screen with white
    screen.fill(colors.get(bgcolor))

    #creating button options

    #Instructions
    myFile = open("MorningGameDesign\PygameFiles\instructions.txt", "r")
    content = myFile.readlines()

    #var to controll change of line
    yinstructions = 150
    for line in content:
        Instruc = MENU_FONT.render(line[0:-1], 1, colors.get(txtcolor))
        screen.blit(Instruc, (40, yinstructions))
        pygame.display.update()
        pygame.time.delay(50)
        yinstructions += 40

    myFile.close()

    #renderig fonts to the screen
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))

    pygame.display.update()
    Instructions = True
    while Instructions:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Instructions=False
                mainMenu()
                print("You quit")


def settings():
    global txtcolor, bgcolor, w, h, screen
    title=TITLE_FONT.render('Settings', 1, colors.get(txtcolor))
    text=MENU_FONT.render('Clr 1', 1, colors.get("white"))
    text2=MENU_FONT.render('press x to see the new settings', 1, colors.get(txtcolor))
    text3=MENU_FONT.render('Clr 2', 1, colors.get("pink"))
    text4=MENU_FONT.render('Clr 3', 1, colors.get("blue"))
    text5=MENU_FONT.render('Size 1', 1, colors.get(txtcolor))
    text6=MENU_FONT.render('Size 2', 1, colors.get(txtcolor))
    text7=MENU_FONT.render('Sound on', 1, colors.get(txtcolor))
    text8=MENU_FONT.render('Sound off', 1, colors.get(txtcolor))

    screen.fill(colors.get(bgcolor))

    Button_3 = pygame.Rect(w//6, h//2, w//14, h//14)
    Button_4 = pygame.Rect(2*w//6, h//2, w//14, h//14)
    Button_5 = pygame.Rect((3*w)//6, h//2, w//14, h//14)
    Button_6 = pygame.Rect((4*w)//6, h//2, w//12, h//14)
    Button_7 = pygame.Rect((5*w)//6, h//2, w//12, h//14)
    Button_8 = pygame.Rect(w//3, 3*h//4, w//7, h//14)
    Button_9 = pygame.Rect(2*w//3, 3*h//4, w//7, h//14)

    pygame.draw.rect(screen, colors.get("limeGreen"), Button_3)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_4)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_5)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_6)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_7)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_8)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_9)
    screen.blit(title, (w//3,50))
    screen.blit(text2, (w//2, 100))
    screen.blit(text, (w//6, h//2))
    screen.blit(text3, (w*2//6, h//2))
    screen.blit(text4, (w*3//6, h//2))
    screen.blit(text5, (w*4//6, h//2))
    screen.blit(text6, (w*5//6, h//2))
    screen.blit(text7, (w//3, 3*h//4))
    screen.blit(text8, (2*w//3, 3*h//4))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                mainMenu()
                print("You quit")
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]
                if Button_3.collidepoint((mx, my)):
                    txtcolor = "white"
                    bgcolor = "blue"
                    pygame.display.update()
                if Button_4.collidepoint((mx, my)):
                    txtcolor = "pink"
                    bgcolor = "white"
                    pygame.display.update()
                if Button_5.collidepoint((mx, my)):
                    txtcolor = "blue"
                    bgcolor = "white"
                    pygame.display.update()
                if Button_6.collidepoint((mx, my)):
                    WIDTH=1000
                    HEIGHT=1000
                    w=WIDTH
                    h=HEIGHT
                    screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
                    pygame.display.update()
                if Button_7.collidepoint((mx, my)):
                    WIDTH=700
                    HEIGHT=700
                    w=WIDTH
                    h=HEIGHT
                    screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
                    pygame.display.update()


def exit():
    title=TITLE_FONT.render('Bye-Bye', 1, colors.get(txtcolor))
    screen.fill(colors.get(bgcolor))
    screen.blit(title, (275, 100))
    pygame.display.update()
    pygame.time.delay(1000)
    pygame.quit()
    sys.exit()

def GameOne():
    global score, hb, wb, xb, rad, yb, charx, chary, cx, cy, speed, ibox, xig, yig, char, bg, mx, my, insSquare, txtcolor, bgcolor
    title=TITLE_FONT.render('Game Level 1', 1, colors.get(txtcolor))
    screen.fill(colors.get(bgcolor))
    rad=25
    screen.blit(title, (275,50))
    pygame.time.delay(1000)
    pygame.display.update()
    score=0
    Game=True
    while Game:
        pygame.draw.rect(screen, colors.get("white"), mountainSquare)
        screen.blit(bg, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                mainMenu()
                print("you quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                # print(mousePos)
        keys = pygame.key.get_pressed() #allow us to see what key was pressed

        #square movement
        if keys[pygame.K_d] and square.x < WIDTH-wb:
            square.x += speed
            charx += speed
        if keys[pygame.K_a] and square.x > 0:
            square.x -= speed
            charx -= speed
        if keys[pygame.K_s] and square.y < HEIGHT-hb:
            square.y += speed
            chary += speed
        if keys[pygame.K_w] and square.y > 0:
            square.y -= speed
            chary -= speed

        #circle and inscribed square movement
        #circle square collide
        if square.colliderect(insSquare): 
            print("BOOM")
            score += 5
            cx = random.randint(rad, WIDTH-rad)
            cy = random.randint(rad, HEIGHT-rad)
            if rad < WIDTH//2:
                rad += 5
            else:
                endtext = TITLE_FONT.render("Game Over", 1, colors.get(txtcolor))
                screen.fill(colors.get(bgcolor))
                screen.blit(endtext, (275, 100))
                leavegametext = MENU_FONT.render("Press x to return to the main menu", 1, colors.get(txtcolor))
                screen.blit(leavegametext, (275, 300))
                pygame.display.update()
                Game = False
            ibox = rad*math.sqrt(2)
            xig = cx-(ibox/2)
            yig = cy-(ibox/2)
            insSquare=pygame.Rect(xig,yig,ibox,ibox)
        
        #mountain collide square
        if square.colliderect(mountainSquare):
            square.x = 10
            square.y = 10
            charx = 10
            chary = 10
        
        #mountain collide circle
        if insSquare.colliderect(mountainSquare):
            cx = rad + 10
            cy = rad + 10
            ibox = rad*math.sqrt(2)
            xig = cx-(ibox/2)
            yig = cy-(ibox/2)
            insSquare=pygame.Rect(xig,yig,ibox,ibox)

        #rect(surface, color, object)
        pygame.draw.rect(screen, colors.get("blue"), square)
        pygame.draw.rect(screen, colors.get("blue"), insSquare)
        screen.blit(char, (charx, chary))

        #circle(surface, color, center, radius)
        pygame.draw.circle(screen, colors.get("pink"), (cx, cy), rad)
        
        pygame.display.update()
        pygame.time.delay(5)
#game one done
def GameTwo():
    global score, hb, wb, xb, rad, yb, charx, chary, cx, cy, speed, ibox, xig, yig, char, bg, mx, my, insSquare, txtcolor, bgcolor
    title=TITLE_FONT.render('Game Level 2', 1, colors.get(txtcolor))
    screen.fill(colors.get(bgcolor))
    rad = 25
    screen.blit(title, (275,50))
    pygame.time.delay(1000)
    pygame.display.update()
    score=0
    Game=True
    while Game:
        pygame.draw.rect(screen, colors.get("white"), mountainSquare)
        screen.blit(bg, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                mainMenu()
                print("you quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                # print(mousePos)
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_RIGHT] and cx < WIDTH-rad:
            cx += speed
            insSquare.x += speed
        if keys[pygame.K_LEFT] and cx > 0+rad:
            cx -= speed
            insSquare.x -= speed
        if keys[pygame.K_DOWN] and cy < HEIGHT-rad:
            cy += speed
            insSquare.y += speed
        if keys[pygame.K_UP] and cy > 0+rad:
            cy -= speed
            insSquare.y -= speed

        if square.colliderect(insSquare): 
            print("BOOM")
            score += 5
            cx = random.randint(rad, WIDTH-rad)
            cy = random.randint(rad, HEIGHT-rad)
            if rad < WIDTH//2:
                rad += 5
            else:
                endtext = TITLE_FONT.render("Game Over", 1, colors.get(txtcolor))
                screen.fill(colors.get(bgcolor))
                screen.blit(endtext, (275, 100))
                leavegametext = MENU_FONT.render("Press x to return to the main menu", 1, colors.get(txtcolor))
                screen.blit(leavegametext, (275, 300))
                pygame.display.update()
                Game = False
            ibox = rad*math.sqrt(2)
            xig = cx-(ibox/2)
            yig = cy-(ibox/2)
            insSquare=pygame.Rect(xig,yig,ibox,ibox)
        
        #mountain collide square
        if square.colliderect(mountainSquare):
            square.x = 10
            square.y = 10
            charx = 10
            chary = 10
        
        #mountain collide circle
        if insSquare.colliderect(mountainSquare):
            cx = rad + 10
            cy = rad + 10
            ibox = rad*math.sqrt(2)
            xig = cx-(ibox/2)
            yig = cy-(ibox/2)
            insSquare=pygame.Rect(xig,yig,ibox,ibox)

        #rect(surface, color, object)
        pygame.draw.rect(screen, colors.get("blue"), square)
        pygame.draw.rect(screen, colors.get("blue"), insSquare)
        screen.blit(char, (charx, chary))

        #circle(surface, color, center, radius)
        pygame.draw.circle(screen, colors.get("pink"), (cx, cy), rad)
        
        pygame.display.update()
        pygame.time.delay(5)
def scoreboard():
    global score, name, txtcolor, bgcolor
    high=0
    two=0
    three=0
    four=0
    five=0
    title=TITLE_FONT.render('Scoreboard', 1, colors.get(txtcolor))
    screen.fill(colors.get(bgcolor))
    screen.blit(title, (250,50))
    print(score)
    high = 0
    if score>high:
        high = score
    two = 0
    if score>two and score<high:
        two = score
    three = 0
    if score>three and score<two:
        three = score
    four = 0
    if score>four and score<three:
        four = score
    five = 0
    if score>five and score<four:
        five = score
    date=datetime.datetime.now()
    scrLine=str(high)+"    "+name + "   "+date.strftime("%m-%d-%Y")+ "\n"
    scrLine2=str(two)+"    "+name + "   "+date.strftime("%m-%d-%Y")+ "\n"
    scrLine3=str(three)+"    "+name + "   "+date.strftime("%m-%d-%Y")+ "\n"       
    scrLine4=str(four)+"    "+name + "   "+date.strftime("%m-%d-%Y")+ "\n"
    scrLine5=str(five)+"    "+name + "   "+date.strftime("%m-%d-%Y")+ "\n"
    myFile = open("MorningGameDesign\PygameFiles\scoreboardd.txt", 'a')
    myFile.write(scrLine+scrLine2+scrLine3+scrLine4+scrLine5)
    myFile.close()
    File = open("MorningGameDesign\PygameFiles\scoreboardd.txt", "r")
    yscores=150
    content = File.readlines()
    for line in content:
        scr = MENU_FONT.render(line[0:-1], 1, colors.get(txtcolor))
        screen.blit(scr, (40, yscores))
        pygame.display.update()
        pygame.time.delay(50)
        yscores += 40
    File.close()
    scoreboard=True
    while scoreboard:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                mainMenu()
                print("You quit")
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]


mainMenu()
        

            