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
current_time = 0
WIDTH=800#need to find width and height for new background
HEIGHT=600
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(0,100,50),"yellow":(255,255,0),"purple":(229,204,255),"grass":(152,220,111),"randt":(random.randint(0,255), random.randint(0,255), random.randint(0,255)),"randb":(random.randint(0,255), random.randint(0,255), random.randint(0,255))}
grass = colors.get("grass")
line = colors.get("white")
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("Garden Guardian")  #change the title of my window

#images for game
tree=pygame.image.load('MorningGameDesign\PygameFiles\Tree.png')
tree = pygame.transform.scale(tree, (WIDTH//10, HEIGHT//7))
trees = [tree, tree, tree, tree, tree, tree, tree]
numbtrees = len(trees)
char = pygame.image.load('MorningGameDesign\PygameFiles\ShovelCropped.png')
char = pygame.transform.scale(char, (WIDTH//30, HEIGHT//14)) #scale images so won't be too big or small compared to rest of screen
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
screen.fill(grass)
images = []
treeboxes  =[]
def imagelocation(images):
    imgInf = []
    treeboxes = []
    counter = 0
    for item in images:
        imgRect=item.get_rect()
        for i in range(1,4):
            imgRect.x = i*WIDTH//4
            imgRect.y = i*HEIGHT//6
            tile = (item, imgRect)
            treeboxes.append(imgRect)
            imgInf.append(tile)
            screen.blit(imgInf[counter][0], imgInf[counter][1])
            pygame.draw.rect(screen, line, imgRect)
            print(imgRect)
            counter+=1
        for i in range(0,3):
            imgRect.x = i*WIDTH//4
            imgRect.y = i*HEIGHT//3
            tile = (item, imgRect)
            imgInf.append(tile)
            screen.blit(imgInf[counter][0], imgInf[counter][1])
            counter+=1

    return imgInf

def draw_grid():
    lineClr=colors.get("white")
    for x in range(1,11):
        pygame.draw.line(screen,lineClr,(0,HEIGHT//10*x),(WIDTH,HEIGHT//10*x),2)  #Hztal line
        pygame.draw.line(screen,lineClr,(WIDTH//10*x, 0),(WIDTH//10*x,HEIGHT),2)  #Vert line
    pygame.time.delay(100)
draw_grid()
trees=imagelocation(trees)
counter = 0
for boxes in treeboxes:
    print(tree)
    pygame.draw.rect(screen, line, boxes)

#     # rect = tree[counter][1]
#     # pygame.draw.rect(screen, grass, rect, 1)
#     counter+=1

pygame.display.update()
Game=True
while Game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()