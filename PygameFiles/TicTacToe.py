#Elizabeth Nassi
#create grid- draw lines
#for loop for lines
#need two things to draw line: x y beginning, xy end
#Width//3- linewidth//2, height//3-linewidth//2
#instructions
#3 lists, 2 dimentional 
#x=1, o=-1
#times negative after each turn so that it goes to the opposite players turn
#[100]
#[010]
#[001]
#if sum column = 3 or negative three, someone wins- horizon
#if sum of all list at  certain index = 3 or -3- vertical
#if sum list 1 index 0, list two index 1, list three index 2, = 3 or -3- diagonal
from tkinter import Widget
import pygame, time,os,random, math, datetime, sys
pygame.init()
TITLE_FONT = pygame.font.SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 20)

os.system('cls')
WIDTH = 600 #like constant
HEIGHT = 600
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51), "turquoise":(102, 139, 139)}
screen=pygame.display.set_mode((WIDTH,HEIGHT))
#make tic tac toe
#need functions:
# draw_grid()
# zero_grid()
# draw_marker()
# check_winner()
# game_end()
size = 3
markers = []
MxMy=(0,0)
lineWidth=10
cellx=0
celly=0
player=1
circolor=colors.get("limeGreen")
xcolor=colors.get("pink")
bgcolor = colors.get("turquoise")
linecolor = colors.get("blue")

def zero_grid():
    for x in range(3):
        row = [0]*size #this will create 3 zeroes
        markers.append(row)
#zero_grid
#print(markers)
#markers[1][1]=1 #fisrt index is row, second is column
#print(markers[1][1])


def draw_grid():
    for x in range(1,3):
        pygame.draw.line(screen, linecolor,(0,HEIGHT//size*x),(WIDTH,HEIGHT//size*x), lineWidth) #0 for horizontal
        pygame.draw.line(screen, linecolor,(WIDTH//size*x, 0),(WIDTH//size*x, HEIGHT), lineWidth)
        pygame.display.update

def draw_markers():
    xvalue=0
    for x in markers: #give me each row of list
        yvalue=0
        for y in x: #give each element
            if y==1:
                # draw x
                pygame.draw.line(screen, xcolor, (xvalue*WIDTH//size+15, yvalue*HEIGHT//size+15), (xvalue*WIDTH//size+WIDTH//size-15, yvalue*HEIGHT//size+HEIGHT//size-15), lineWidth)
                pygame.draw.line(screen, xcolor, (xvalue*WIDTH//size+WIDTH//size-15, yvalue*HEIGHT//size+15), (xvalue*WIDTH//size+15, yvalue*HEIGHT//size+HEIGHT//size-15), lineWidth)
            if y==-1:
                #draw o
                pygame.draw.circle(screen, circolor, (xvalue*WIDTH//size+WIDTH//(2*size)+5, yvalue*HEIGHT//size+HEIGHT//(2*size)+5), WIDTH//(2*size)-lineWidth-10, lineWidth)
            yvalue+=1
        xvalue+=1
def check_winner():
    print(markers[0][0])
zero_grid()
Game = True
while Game:
    screen.fill(bgcolor)
    draw_grid()
    draw_markers()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
                #run=False
                #mainMenu()
            print("You quit")
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            MxMy=pygame.mouse.get_pos()
            cellx=MxMy[0]//(WIDTH//size)
            celly=MxMy[1]//(HEIGHT//size)
            print(markers)
            if markers[cellx][celly]==0:
                markers[cellx][celly]=player
                player *=-1
                #check winner
    pygame.time.delay(50)
    pygame.display.update()