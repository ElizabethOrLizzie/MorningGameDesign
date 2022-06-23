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
grass = colors.get("grass")
line = colors.get("white")
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("Garden Guardian")  #change the title of my window
MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//35)
#images for game
tree=pygame.image.load('MorningGameDesign\PygameFiles\Tree.png')
tree = pygame.transform.scale(tree, (WIDTH//10, HEIGHT//7))
trees = [tree, tree, tree, tree, tree, tree, tree]
numbtrees = len(trees)
char = pygame.image.load('MorningGameDesign\PygameFiles\ShovelCropped.png')
char = pygame.transform.scale(char, (WIDTH//30, HEIGHT//14)) #scale images so won't be too big or small compared to rest of screen
charbox = char.get_rect()
charbox.x=0
charbox.y=0
tulip = pygame.image.load('MorningGameDesign\PygameFiles\Lavendar.png')
tulip = pygame.transform.scale(tulip, (WIDTH//30, HEIGHT//12))
tulips = [tulip, tulip, tulip, tulip, tulip, tulip]
sunflower = pygame.image.load('MorningGameDesign\PygameFiles\Sunflower.png')
sunflower = pygame.transform.scale(sunflower, (WIDTH//14, HEIGHT//16))
sunflowers = [sunflower, sunflower,sunflower,sunflower,sunflower,sunflower,sunflower,sunflower]
rose = pygame.image.load('MorningGameDesign\PygameFiles\Rose.png')
rose = pygame.transform.scale(rose, (WIDTH//30, HEIGHT//12))
roses = [rose, rose, rose, rose, rose, rose, rose, rose, rose, rose, rose, rose]
weed = pygame.image.load('MorningGameDesign\PygameFiles\GardenWeed.png')
weed = pygame.transform.scale(weed, (WIDTH//35, HEIGHT//12))
weeds = [weed, weed, weed, weed, weed, weed, weed, weed, weed, weed]
#character location
score = 0
#char speed
speed = 5
clock = pygame.time.Clock()
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
    global charbox, score
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
    text=MENU_FONT.render("Score = "+str(score), 1, colors.get("blue"))
    screen.blit(text, (WIDTH-text.get_width(), 0))
    current_time = pygame.time.get_ticks()
    if current_time-old_time > 5000:
        tulipslist = imagelocation(tulips)
        weedslist = imagelocation(weeds)
    draw_image(treeslist)
    draw_image(tulipslist)
    draw_image(weedslist)
    screen.blit(char, charbox)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
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
# counter = 0
# for boxes in treeboxes:
#     print(tree)
#     pygame.draw.rect(screen, line, boxes)

#     # rect = tree[counter][1]
#     # pygame.draw.rect(screen, grass, rect, 1)
#     counter+=1