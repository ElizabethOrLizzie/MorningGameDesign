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

import pygame, time,os,random, math, datetime, sys
date=datetime.datetime.now()
pygame.init()#initialize the pygame package
os.system('cls')
clock = pygame.time.Clock
# print(pygame.font.get_fonts())
# pygame.time.delay(10000)


WIDTH=700 #like constant
w = WIDTH
HEIGHT=700
h = HEIGHT
TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//18)
MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//35)
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(0,100,50),"yellow":(255,255,50),"purple":(229,204,255),"randt":(random.randint(0,255), random.randint(0,255), random.randint(0,255)),"randb":(random.randint(0,255), random.randint(0,255), random.randint(0,255))}
message=['Instructions', 'Settings', 'Game 1', 'Game 2', 'Game 3', 'Scoreboard', 'Exit']
#create dispay wind with any name y like
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("Menu")  #change the title of my window
Bx2=WIDTH//6
Bx=WIDTH//2-Bx2//2
#boxes for menu
Button_menu=pygame.Rect(Bx, 125, Bx2, WIDTH//18)
Button_instruct=pygame.Rect(Bx, HEIGHT//8, Bx2, WIDTH//18)
Button_settings=pygame.Rect(Bx, 2*HEIGHT//8, Bx2, WIDTH//18)
Button_Game1=pygame.Rect(Bx, 3*HEIGHT//8, Bx2, WIDTH//18)
Button_Game2=pygame.Rect(Bx, 4*HEIGHT//8, Bx2, WIDTH//18)
Button_Game3=pygame.Rect(Bx, 5*HEIGHT//8, Bx2, WIDTH//18)
Button_score=pygame.Rect(Bx, 6*HEIGHT//8, Bx2, WIDTH//18)
Button_exit=pygame.Rect(Bx, 7*HEIGHT//8, Bx2, WIDTH//18)
#images
bg=pygame.image.load('MorningGameDesign\PygameFiles\Images\Backgroundimagepurplerock.jpg')
char = pygame.image.load('MorningGameDesign\PygameFiles\Images\PixelArtTutorialCharacter.png')
char = pygame.transform.scale(char, (WIDTH//14, HEIGHT//14))
# screen.blit(bg, (0,0))
# pygame.display.update()
# pygame.time.delay(5000)


#square Var
hb=HEIGHT//14
wb=WIDTH//14
xb=WIDTH//7
rad=25
yb=HEIGHT//2

charx = xb
chary = yb
txtcolor="yellow"
bgcolor="limeGreen"
cx=WIDTH//2
cy=HEIGHT//2
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
    pygame.draw.rect(screen, colors.get('purple'), Button_settings)
    Title = TITLE_FONT.render("Circle eats Square Menu", 1, colors.get(txtcolor))
    screen.fill(colors.get(bgcolor))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 10))
    yMenu = HEIGHT//8
    
    for item in message:
        Button_menu=pygame.Rect(Bx, yMenu, Bx2, WIDTH//18)
        text=MENU_FONT.render(item, 1, colors.get(txtcolor))
        pygame.draw.rect(screen, colors.get('purple'), Button_menu)
        screen.blit(text, (Bx, yMenu))
        pygame.display.update()
        #pygame.time.delay(50)
        yMenu += HEIGHT//8
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
                if Button_Game3.collidepoint((mx, my)):
                    GameThree()
    
def Instructions():
    #rendering text objects
    Title = TITLE_FONT.render("Instructions", 1, colors.get(txtcolor))

    #fills screen with white
    screen.fill(colors.get(bgcolor))

    #creating button options

    #Instructions
    myFile = open("MorningGameDesign\PygameFiles\instructions.txt", "r")
    content = myFile.readlines()

    #var to controll change of line
    yinstructions = HEIGHT//4.7
    for line in content:
        Instruc = MENU_FONT.render(line[0:-1], 1, colors.get(txtcolor))
        screen.blit(Instruc, (WIDTH//14, yinstructions))
        pygame.display.update()
        #time delay
        yinstructions += HEIGHT//18

    myFile.close()

    #renderig fonts to the screen
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 10))

    pygame.display.update()
    Instructions = True
    while Instructions:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Instructions=False
                mainMenu()
                print("You quit")


def settings():
    global txtcolor, bgcolor, w, h, screen, WIDTH, HEIGHT
    title=TITLE_FONT.render('Settings', 1, colors.get(txtcolor))
    text=MENU_FONT.render('Clr 1', 1, colors.get("yellow"))
    text2=MENU_FONT.render('press x to see the new settings', 1, colors.get(txtcolor))
    text3=MENU_FONT.render('Clr 2', 1, colors.get("pink"))
    text4=MENU_FONT.render('Random Clr', 1, colors.get("randt"))
    text5=MENU_FONT.render('Smaller Screen', 1, colors.get(txtcolor))
    text6=MENU_FONT.render('Bigger Screen', 1, colors.get(txtcolor))

    screen.fill(colors.get(bgcolor))

    Button_3 = pygame.Rect(w//4-w//12, h//4, w//6, h//14)
    Button_4 = pygame.Rect(2*w//4-w//12, h//4, w//6, h//14)
    Button_5 = pygame.Rect(3*w//4-w//12, h//4, w//6, h//14)
    Button_6 = pygame.Rect(w//3-w//8, 2*h//4, w//4, h//14)
    Button_7 = pygame.Rect(2*w//3-w//8, 2*h//4, w//4, h//14)

    pygame.draw.rect(screen, colors.get("limeGreen"), Button_3)
    pygame.draw.rect(screen, colors.get("white"), Button_4)
    pygame.draw.rect(screen, colors.get("randb"), Button_5)
    pygame.draw.rect(screen, colors.get("purple"), Button_6)
    pygame.draw.rect(screen, colors.get("purple"), Button_7)
    screen.blit(title, (w//2-8*WIDTH//18,50))
    screen.blit(text2, (w//2, 100))
    screen.blit(text, (w//4-w//12, h//4))
    screen.blit(text3, (2*w//4-w//12, h//4))
    screen.blit(text4, (3*w//4-w//12, h//4))
    screen.blit(text5, (w//3-w//8, 2*h//4))
    screen.blit(text6, (2*w//3-w//8, 2*h//4))

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
                    txtcolor = "yellow"
                    bgcolor = "limeGreen"
                    pygame.display.update()
                if Button_4.collidepoint((mx, my)):
                    txtcolor = "pink"
                    bgcolor = "white"
                    pygame.display.update()
                if Button_5.collidepoint((mx, my)):
                    txtcolor = "randt"
                    bgcolor = "randb"
                    pygame.display.update()
                if Button_6.collidepoint((mx, my)):
                    WIDTH-=100
                    HEIGHT-=100
                    w=WIDTH
                    h=HEIGHT
                    screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
                    pygame.display.update()
                if Button_7.collidepoint((mx, my)):
                    WIDTH+=100
                    HEIGHT+=100
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
def GameThree():
    print("Gamethree")
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
        screen.blit(scr, (WIDTH//18, yscores))
        pygame.display.update()
        pygame.time.delay(50)
        yscores += WIDTH//18
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
        

            