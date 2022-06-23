#Elizabeth Nassi
# June 2022
# K_UP                  up arrow
# K_DOWN                down arrow
# K_RIGHT               right arrow
# K_LEFT                left arrow
import pygame, time, os,random, math, datetime, sys

pygame.init()#initialize the pygame package
os.system('cls')
clock = pygame.time.Clock() #try to use clock instead of delays to make it better

WIDTH=800#need to find width and height for new background
HEIGHT=600
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(0,100,50),"yellow":(255,255,0),"purple":(229,204,255),"grass":(152,220,111),"randt":(random.randint(0,255), random.randint(0,255), random.randint(0,255)),"randb":(random.randint(0,255), random.randint(0,255), random.randint(0,255))}
message=['Instructions', 'Settings', '1: Tulip', '2: Sunflower', '3: Rose', 'Scoreboard', 'Exit']
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("Garden Guardian")  #change the title of my window
#boxes for menu
#images for game
tree=pygame.image.load('MorningGameDesign\PygameFiles\Tree.png')
char = pygame.image.load('MorningGameDesign\PygameFiles\ShovelCropped.png')
char = pygame.transform.scale(char, (WIDTH//25, HEIGHT//14)) #scale images so won't be too big or small compared to rest of screen
tulip = pygame.image.load('MorningGameDesign\PygameFiles\Lavendar.png')
tulip = pygame.transform.scale(tulip, (WIDTH//30, HEIGHT//12))
sunflower = pygame.image.load('MorningGameDesign\PygameFiles\Sunflower.png')
sunflower = pygame.transform.scale(sunflower, (WIDTH//14, HEIGHT//16))
rose = pygame.image.load('MorningGameDesign\PygameFiles\Rose.png')
rose = pygame.transform.scale(rose, (WIDTH//40, HEIGHT//12))
weed = pygame.image.load('MorningGameDesign\PygameFiles\GardenWeed.png')
weed = pygame.transform.scale(weed, (WIDTH//35, HEIGHT//12))
# screen.blit(bg, (0,0))
# pygame.display.update()
# pygame.time.delay(5000)

#SCOREBOARD VARIABLES
date=datetime.datetime.now()
high = 0
two = 0
three = 0
four = 0
five = 0
scrLine="1. 0    nobody   "+date.strftime("%m-%d-%Y")+ "\n"
scrLine2="2. 0    nobody    "+date.strftime("%m-%d-%Y")+ "\n"
scrLine3="3. 0    nobody    "+date.strftime("%m-%d-%Y")+ "\n"       
scrLine4="4. 0    nobody    "+date.strftime("%m-%d-%Y")+ "\n"
scrLine5="5. 0    nobody    "+date.strftime("%m-%d-%Y")+ "\n"

#scoreboard and game variable
score = 0
speed =5
#GAME VARIABLES
circleClr=colors.get("blue")
backgrnd=colors.get("limeGreen")

#SETTINGS VARIABLES
txtcolor="yellow"
bgcolor="limeGreen"
name = ''#settings/score variable?

#mouse variables(used a lot, mainly for buttons in menu and settings and exiting)
mx = 0
my = 0

run = True
Game = False
def mainMenu():
    TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//18)
    MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//35)
    Bx2=WIDTH//6
    Bx=WIDTH//2-Bx2//2
    Button_menu=pygame.Rect(Bx, 125, Bx2, WIDTH//18)
    Button_instruct=pygame.Rect(Bx, HEIGHT//8, Bx2, WIDTH//18)
    Button_settings=pygame.Rect(Bx, 2*HEIGHT//8, Bx2, WIDTH//18)
    Button_Game1=pygame.Rect(Bx, 3*HEIGHT//8, Bx2, WIDTH//18)
    Button_Game2=pygame.Rect(Bx, 4*HEIGHT//8, Bx2, WIDTH//18)
    Button_Game3=pygame.Rect(Bx, 5*HEIGHT//8, Bx2, WIDTH//18)
    Button_score=pygame.Rect(Bx, 6*HEIGHT//8, Bx2, WIDTH//18)
    Button_exit=pygame.Rect(Bx, 7*HEIGHT//8, Bx2, WIDTH//18)
    #pygame.draw.rect(screen, colors.get('purple'), Button_settings)
    Title = TITLE_FONT.render("Garden Guardian", 1, colors.get(txtcolor))
    screen.fill(colors.get(bgcolor))
    screen.blit(Title, (WIDTH//2 - (Title.get_width()//2), HEIGHT//100))
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
                #run=False
                mainMenu()
                print("You quit")

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
    
def Instructions():#has been changed
    #rendering text objects
    TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//18)
    MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//35)
    Title = TITLE_FONT.render("Instructions", 1, colors.get(txtcolor))
    Luck = MENU_FONT.render("Good luck, ", 1, colors.get(txtcolor))
    FloDepend = MENU_FONT.render("the safety of your neighbors’ flowers rests in your hands.", 1, colors.get(txtcolor))

    #fills screen with background
    screen.fill(colors.get(bgcolor))

    #creating button options

    #Instructions
    myFile = open("MorningGameDesign\PygameFiles\GGInstructions.txt", "r")
    content = myFile.readlines()

    #var to controll change of line
    yinstructions = HEIGHT//4.7
    for line in content:
        Instruc = MENU_FONT.render(line[0:-1], 1, colors.get(txtcolor))
        screen.blit(Instruc, (WIDTH//2 - (Instruc.get_width()//2), yinstructions))
        pygame.display.update()
        #time delay
        yinstructions += HEIGHT//18
    myFile.close()

    #renderig fonts to the screen
    screen.blit(Title, (WIDTH//2 - (Title.get_width()//2), HEIGHT//60))
    screen.blit(Luck, (WIDTH//2 - (Luck.get_width()//2), yinstructions))
    yinstructions+=HEIGHT//18
    screen.blit(FloDepend, (WIDTH//2 - (FloDepend.get_width()//2), yinstructions))

    pygame.display.update()
    Instructions = True
    while Instructions:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Instructions=False
                mainMenu()
                print("You quit")


def settings():
    global txtcolor, bgcolor, screen, WIDTH, HEIGHT, colors, name
    TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//18)
    MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//35)
    colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(0,100,50),"yellow":(255,255,50),"purple":(229,204,255),"grass":(152,220,111),"randt":(random.randint(0,255), random.randint(0,255), random.randint(0,255)),"randb":(random.randint(0,255), random.randint(0,255), random.randint(0,255))}
    title=TITLE_FONT.render('Settings', 1, colors.get(txtcolor))
    text=MENU_FONT.render('Clr 1', 1, colors.get("yellow"))
    text3=MENU_FONT.render('Clr 2', 1, colors.get("pink"))
    text4=MENU_FONT.render('Random Clr', 1, colors.get("randt"))
    text5=MENU_FONT.render('Smaller Screen', 1, colors.get(txtcolor))
    text6=MENU_FONT.render('Bigger Screen', 1, colors.get(txtcolor))
    text7=MENU_FONT.render('Enter Name: ', 1, colors.get(txtcolor))
    text8=MENU_FONT.render(name, 1, colors.get(txtcolor))

    screen.fill(colors.get(bgcolor))

    Button_3 = pygame.Rect(WIDTH//4-WIDTH//12, HEIGHT//4, WIDTH//6, HEIGHT//14)
    Button_4 = pygame.Rect(2*WIDTH//4-WIDTH//12, HEIGHT//4, WIDTH//6, HEIGHT//14)
    Button_5 = pygame.Rect(3*WIDTH//4-WIDTH//12, HEIGHT//4, WIDTH//6, HEIGHT//14)
    Button_6 = pygame.Rect(WIDTH//3-WIDTH//8, 2*HEIGHT//4, WIDTH//4, HEIGHT//14)
    Button_7 = pygame.Rect(2*WIDTH//3-WIDTH//8, 2*HEIGHT//4, WIDTH//4, HEIGHT//14)
    Button_8 = pygame.Rect(WIDTH//4-WIDTH//12, 3*HEIGHT//4, 3*WIDTH//4-WIDTH//12, HEIGHT//14)
    Button_9 = pygame.Rect(WIDTH//4+WIDTH//12, 3*HEIGHT//4, 3*WIDTH//4-3*WIDTH//12, HEIGHT//14)

    pygame.draw.rect(screen, colors.get("limeGreen"), Button_3)
    pygame.draw.rect(screen, colors.get("white"), Button_4)
    pygame.draw.rect(screen, colors.get("randb"), Button_5)
    pygame.draw.rect(screen, colors.get("purple"), Button_6)
    pygame.draw.rect(screen, colors.get("purple"), Button_7)
    pygame.draw.rect(screen, colors.get("purple"), Button_8)
    screen.blit(title, (WIDTH//2-8*WIDTH//18, HEIGHT//12))
    screen.blit(text, (WIDTH//4-WIDTH//12, HEIGHT//4))
    screen.blit(text3, (2*WIDTH//4-WIDTH//12, HEIGHT//4))
    screen.blit(text4, (3*WIDTH//4-WIDTH//12, HEIGHT//4))
    screen.blit(text5, (WIDTH//3-WIDTH//8, 2*HEIGHT//4))
    screen.blit(text6, (2*WIDTH//3-WIDTH//8, 2*HEIGHT//4))
    screen.blit(text7, (WIDTH//4-WIDTH//12, 3*HEIGHT//4))
    screen.blit(text8, (Button_9.x+5, Button_9.y+5))

    pygame.display.update()
    setting = True
    while setting:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                setting = False
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
                    mainMenu()
                if Button_4.collidepoint((mx, my)):
                    txtcolor = "pink"
                    bgcolor = "white"
                    pygame.display.update()
                    mainMenu()
                if Button_5.collidepoint((mx, my)):
                    txtcolor = "randt"
                    bgcolor = "randb"
                    pygame.display.update()
                    mainMenu()
                if Button_6.collidepoint((mx, my)):
                    if WIDTH!=300:
                        WIDTH-=100
                        HEIGHT-=100
                        screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
                        pygame.display.update()
                        mainMenu()
                if Button_7.collidepoint((mx, my)):
                    WIDTH+=100
                    HEIGHT+=100
                    screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
                    pygame.display.update()
                    mainMenu()
                if Button_9.collidepoint((mx,my)): #does not work, need to fix
                    pygame.draw.rect(screen, colors.get("blue"), Button_9)
                    pygame.display.update()
                    run = True
                    while run:
                        for event in pygame.event.get():
                            if event.type==pygame.QUIT:
                                mainMenu()
                                #Menu(mainTitle,messageMenu)
                                # pygame.quit()
                                # sys.exit()
                                print("You quit")
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RETURN:
                                    print(name)
                                    #run main menu - if in main program
                                    pygame.draw.rect(screen, colors.get("purple"), Button_9)
                                    textSurface=MENU_FONT.render(name, True, colors.get(txtcolor))
                                    #use rect x and y to  allign the text 
                                    screen.blit(textSurface, (Button_9.x+5, Button_9.y+5))
                                    run = False
                                    mainMenu()
                                    # pygame.quit()
                                    # sys.exit()
                                if event.key ==pygame.K_BACKSPACE:
                                    name=name[:-1]
                                    print('back')
                                else:
                                    name += event.unicode
                                    # textname=MENU_FONT.render(name, True, colors.get(txtcolor))
                                    # screen.blit(textname, (Button_9.x+5, Button_9.y+5))
                                    # pygame.display.update()
                            pygame.draw.rect(screen, colors.get("blue"), Button_9)
                            textSurface=MENU_FONT.render(name, True, colors.get(txtcolor))
                            #use rect x and y to  allign the text 
                    #use rect x and y to  allign the text 
                            #use rect x and y to  allign the text 
                    #use rect x and y to  allign the text 
                            #use rect x and y to  allign the text 
                            screen.blit(textSurface, (Button_9.x+5, Button_9.y+5))
                            pygame.display.flip()
                    #clock.tick(60)


def exit():
    TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//18)
    title=TITLE_FONT.render('Bye', 1, colors.get(txtcolor))
    screen.fill(colors.get(bgcolor))
    screen.blit(title, (WIDTH//2 - (title.get_width()//2), HEIGHT//2- (title.get_height()//2)))
    #screen.blit(title, (WIDTH//2, HEIGHT//2))
    pygame.display.update()
    pygame.time.delay(1000)
    pygame.quit()
    sys.exit()
def GameTwo():
    global score
    score = 0
    MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//35)
    grass = colors.get("grass")
    line = colors.get("white")
    charbox = char.get_rect()
    charbox.x=0
    charbox.y=0
    sunflowers = [sunflower,sunflower,sunflower,sunflower,sunflower,sunflower,sunflower,sunflower]
    trees = [tree, tree, tree, tree, tree]
    weeds = [weed, weed, weed, weed, weed, weed, weed, weed, weed, weed, weed, weed]
    screen.fill(grass)
    images = []
    treeboxes  =[]
    def imagelocation(images):
        global old_time
        imgInf = []
        counter = 0
        for item in images:
            imgRect = item.get_rect()
            imgRect.x = random.randint(0, WIDTH-item.get_width())
            imgRect.y = random.randint(0, HEIGHT-item.get_height())
            tile = (item, imgRect)
            imgInf.append(tile)
            pygame.draw.rect(screen, grass, imgRect)
            screen.blit(imgInf[counter][0], imgInf[counter][1])
        
            counter+=1
            
        old_time = pygame.time.get_ticks()

        return imgInf

    def draw_grid():
        lineClr=colors.get("white")
        for x in range(1,11):
            pygame.draw.line(screen,lineClr,(0,HEIGHT//10*x),(WIDTH,HEIGHT//10*x),2)  #Hztal line
            pygame.draw.line(screen,lineClr,(WIDTH//10*x, 0),(WIDTH//10*x,HEIGHT),2)  #Vert line
        pygame.time.delay(100)
    def draw_image(images):
        counter = 0
        for item in images:
            screen.blit(images[counter][0], images[counter][1])
            counter+=1
    def collidecheck():
        global score
        nonlocal charbox
        counter = 0
        for item in treeslist:
            if charbox.colliderect(treeslist[counter][1]):
                charbox.x=0
                charbox.y=0
            counter+=1
        counter = 0
        for item in weedslist:
            if charbox.colliderect(weedslist[counter][1]):
                print("hit")
                score += 5
                del weedslist[counter]
            counter+=1
        counter=0
        for item in sunflowerslist:
            if charbox.colliderect(sunflowerslist[counter][1]):
                print("hit")
                score -= 5
                del sunflowerslist[counter]
            counter+=1
    draw_grid()
    treeslist=[]
    images = []
    treeslist=imagelocation(trees)

    sunflowerslist = []
    sunflowerslist = imagelocation(sunflowers)
    weedlist = []
    weedslist = imagelocation(weeds)
    game = True
    while game:
        clock.tick(60)
        screen.fill(grass)
        text= MENU_FONT.render("Score = "+str(score), 1, colors.get("blue"))
        screen.blit(text, (WIDTH-text.get_width(), 0))
        current_time = pygame.time.get_ticks()
        if current_time-old_time > 5000:
            sunflowerslist = imagelocation(sunflowers)
            weedslist = imagelocation(weeds)
        draw_image(treeslist)
        draw_image(sunflowerslist)
        draw_image(weedslist)
        screen.blit(char, charbox)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainMenu()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and charbox.x < WIDTH-char.get_width():
            charbox.x += speed
        if keys[pygame.K_LEFT] and charbox.x > 0:
            charbox.x -= speed
        if keys[pygame.K_DOWN] and charbox.y < HEIGHT-char.get_height():
            charbox.y += speed
        if keys[pygame.K_UP] and charbox.y > 0:
            charbox.y -= speed
        collidecheck()
def GameOne():
    global score
    score = 0
    MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//35)
    grass = colors.get("grass")
    line = colors.get("white")
    charbox = char.get_rect()
    charbox.x=0
    charbox.y=0
    tulips = [tulip, tulip, tulip, tulip, tulip, tulip]
    trees = [tree, tree, tree]
    weeds = [weed, weed, weed, weed, weed, weed, weed, weed, weed, weed, weed, weed, weed, weed, weed]
    screen.fill(grass)
    images = []
    treeboxes  =[]
    def imagelocation(images):
        global old_time
        imgInf = []
        counter = 0
        for item in images:
            imgRect = item.get_rect()
            imgRect.x = random.randint(0, WIDTH-item.get_width())
            imgRect.y = random.randint(0, HEIGHT-item.get_height())
            tile = (item, imgRect)
            imgInf.append(tile)
            pygame.draw.rect(screen, grass, imgRect)
            screen.blit(imgInf[counter][0], imgInf[counter][1])
        
            counter+=1
            
        old_time = pygame.time.get_ticks()

        return imgInf

    def draw_grid():
        lineClr=colors.get("white")
        for x in range(1,11):
            pygame.draw.line(screen,lineClr,(0,HEIGHT//10*x),(WIDTH,HEIGHT//10*x),2)  #Hztal line
            pygame.draw.line(screen,lineClr,(WIDTH//10*x, 0),(WIDTH//10*x,HEIGHT),2)  #Vert line
        pygame.time.delay(100)
    def draw_image(images):
        counter = 0
        for item in images:
            screen.blit(images[counter][0], images[counter][1])
            counter+=1
    def collidecheck():
        global score
        nonlocal charbox
        counter = 0
        for item in treeslist:
            if charbox.colliderect(treeslist[counter][1]):
                charbox.x=0
                charbox.y=0
            counter+=1
        counter = 0
        for item in weedslist:
            if charbox.colliderect(weedslist[counter][1]):
                print("hit")
                score += 5
                del weedslist[counter]
            counter+=1
        counter=0
        for item in tulipslist:
            if charbox.colliderect(tulipslist[counter][1]):
                print("hit")
                score -= 5
                del tulipslist[counter]
            counter+=1
    draw_grid()
    treeslist=[]
    images = []
    treeslist=imagelocation(trees)

    tulipslist = []
    tulipslist = imagelocation(tulips)
    weedlist = []
    weedslist = imagelocation(weeds)
    game = True
    while game:
        clock.tick(60)
        screen.fill(grass)
        text= MENU_FONT.render("Score = "+str(score), 1, colors.get("blue"))
        screen.blit(text, (WIDTH-text.get_width(), 0))
        current_time = pygame.time.get_ticks()
        if current_time-old_time > 6000:
            tulipslist = imagelocation(tulips)
            weedslist = imagelocation(weeds)
        draw_image(treeslist)
        draw_image(tulipslist)
        draw_image(weedslist)
        screen.blit(char, charbox)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainMenu()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and charbox.x < WIDTH-char.get_width():
            charbox.x += speed
        if keys[pygame.K_LEFT] and charbox.x > 0:
            charbox.x -= speed
        if keys[pygame.K_DOWN] and charbox.y < HEIGHT-char.get_height():
            charbox.y += speed
        if keys[pygame.K_UP] and charbox.y > 0:
            charbox.y -= speed
        collidecheck()
def GameThree():
    global score
    score = 0
    MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//35)
    grass = colors.get("grass")
    line = colors.get("white")
    charbox = char.get_rect()
    charbox.x=0
    charbox.y=0
    roses = [rose,rose,rose,rose,rose,rose,rose,rose, rose, rose, rose,rose, rose]
    trees = [tree, tree, tree, tree, tree, tree, tree]
    weeds = [weed, weed, weed, weed, weed, weed, weed, weed, weed]
    screen.fill(grass)
    images = []
    treeboxes  =[]
    def imagelocation(images):
        global old_time
        imgInf = []
        counter = 0
        for item in images:
            imgRect = item.get_rect()
            imgRect.x = random.randint(0, WIDTH-item.get_width())
            imgRect.y = random.randint(0, HEIGHT-item.get_height())
            tile = (item, imgRect)
            imgInf.append(tile)
            pygame.draw.rect(screen, grass, imgRect)
            screen.blit(imgInf[counter][0], imgInf[counter][1])
        
            counter+=1
            
        old_time = pygame.time.get_ticks()

        return imgInf

    def draw_grid():
        lineClr=colors.get("white")
        for x in range(1,11):
            pygame.draw.line(screen,lineClr,(0,HEIGHT//10*x),(WIDTH,HEIGHT//10*x),2)  #Hztal line
            pygame.draw.line(screen,lineClr,(WIDTH//10*x, 0),(WIDTH//10*x,HEIGHT),2)  #Vert line
        pygame.time.delay(100)
    def draw_image(images):
        counter = 0
        for item in images:
            screen.blit(images[counter][0], images[counter][1])
            counter+=1
    def collidecheck():
        global score
        nonlocal charbox
        counter = 0
        for item in treeslist:
            if charbox.colliderect(treeslist[counter][1]):
                charbox.x=0
                charbox.y=0
            counter+=1
        counter = 0
        for item in weedslist:
            if charbox.colliderect(weedslist[counter][1]):
                print("hit")
                score += 5
                del weedslist[counter]
            counter+=1
        counter=0
        for item in roseslist:
            if charbox.colliderect(roseslist[counter][1]):
                print("hit")
                score -= 5
                del roseslist[counter]
            counter+=1
    draw_grid()
    treeslist=[]
    images = []
    treeslist=imagelocation(trees)

    roseslist = []
    roseslist = imagelocation(roses)
    weedlist = []
    weedslist = imagelocation(weeds)
    game = True
    while game:
        clock.tick(60)
        screen.fill(grass)
        text= MENU_FONT.render("Score = "+str(score), 1, colors.get("blue"))
        screen.blit(text, (WIDTH-text.get_width(), 0))
        current_time = pygame.time.get_ticks()
        if current_time-old_time > 3000:
            roseslist = imagelocation(roses)
            weedslist = imagelocation(weeds)
        draw_image(treeslist)
        draw_image(roseslist)
        draw_image(weedslist)
        screen.blit(char, charbox)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainMenu()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and charbox.x < WIDTH-char.get_width():
            charbox.x += speed
        if keys[pygame.K_LEFT] and charbox.x > 0:
            charbox.x -= speed
        if keys[pygame.K_DOWN] and charbox.y < HEIGHT-char.get_height():
            charbox.y += speed
        if keys[pygame.K_UP] and charbox.y > 0:
            charbox.y -= speed
        collidecheck()
def scoreboard():
    global score, name, txtcolor, bgcolor, high, two, three, four, five, scrLine, scrLine2, scrLine3, scrLine4, scrLine5
    TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//18)
    MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//35)
    title=TITLE_FONT.render('Leaderboard', 1, colors.get(txtcolor))
    date=datetime.datetime.now()
    screen.fill(colors.get(bgcolor))
    screen.blit(title, (WIDTH//3,50))
    print(score)
    if score>high:
        five = four
        four = three
        three = two
        two = high
        high = score
        scrLine="1. "+str(high)+"    "+name + "   "+date.strftime("%m-%d-%Y")+ "\n"
    if score>two and score<high:
        five = four
        four = three
        three = two
        two = score
        scrLine2="2. "+str(two)+"    "+name + "   "+date.strftime("%m-%d-%Y")+ "\n"
    if score>three and score<two:
        five = four
        four = three
        three = score
        scrLine3="3. "+str(three)+"    "+name + "   "+date.strftime("%m-%d-%Y")+ "\n"
    if score>four and score<three:
        five = four
        four = score
        scrLine4="4. "+str(four)+"    "+name + "   "+date.strftime("%m-%d-%Y")+ "\n"
    if score>five and score<four:
        five = score
        scrLine5="5. "+str(five)+"    "+name + "   "+date.strftime("%m-%d-%Y")+ "\n"
    date=datetime.datetime.now()
    myFile = open("MorningGameDesign\PygameFiles\scoreboardd.txt", 'a')
    myFile.write(scrLine+scrLine2+scrLine3+scrLine4+scrLine5)
    myFile.close()
    File = open("MorningGameDesign\PygameFiles\scoreboardd.txt", "r")
    yscores=150
    content = File.readlines()
    for line in content[-5:]:
        scr = MENU_FONT.render(line[0:-1], 1, colors.get(txtcolor))
        screen.blit(scr, (WIDTH//18, yscores))
        pygame.display.update()
        yscores += HEIGHT//18
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
