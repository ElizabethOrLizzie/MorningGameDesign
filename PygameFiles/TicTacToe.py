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
import pygame, time,os,random, math, datetime, sys
pygame.init()
TITLE_FONT = pygame.font.SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 20)

os.system('cls')
WIDTH = 600 #like constant
HEIGHT = 600
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51),"turquoise":(102, 139, 139)}
screen=pygame.display.set_mode((WIDTH,HEIGHT))
#make tic tac toe
#need functions:
# draw_grid()
# zero_grid()
# draw_marker()
# check_winner()
# game_end()
U_FONT = pygame.font.SysFont('comicsans', 20)
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
O_score = 0
X_score=0

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
    pygame.display.update()
def agn():
    global Game, X_score, O_score, markers, cnt
    Game = False
    screen.fill(bgcolor)
    strx = str(X_score)
    stro = str(O_score)
    textxscore=U_FONT.render("X's score is "+strx, 1, (linecolor))
    textoscore=U_FONT.render("O's score is "+stro, 1, (linecolor))
    textagn=U_FONT.render('Want to play again?', 1, (linecolor))
    Buttony=pygame.Rect(WIDTH//4, HEIGHT//2, 100, 50)
    Button_n=pygame.Rect(3*WIDTH//4, HEIGHT//2, 100, 50)
    textyes=U_FONT.render('Yes', 1, (linecolor))
    textno=U_FONT.render('No', 1, (linecolor))
    xd = WIDTH//2 - (textagn.get_width()//2)
    screen.blit(textagn, (xd, 50))
    pygame.draw.rect(screen, colors.get('white'), Buttony)
    pygame.draw.rect(screen, colors.get('white'), Button_n)
    screen.blit(textyes, (WIDTH//4, HEIGHT//2))
    screen.blit(textno, (3*WIDTH//4, HEIGHT//2))
    screen.blit(textxscore, (WIDTH//2, 4*HEIGHT//6))
    screen.blit(textoscore, (WIDTH//2, 5*HEIGHT//6))
    pygame.display.update()
    pygame.time.delay(10000)
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            mousePos=pygame.mouse.get_pos()
            mx=mousePos[0]
            my=mousePos[1]
            if Buttony.collidepoint((mx, my)):
                pygame.event.get()
                cnt=0
                screen.fill(bgcolor)
                pygame.display.update()
                markers=[]
                zero_grid()
                Game = True
            if Button_n.collidepoint((mx, my)):
                pygame.event.get()
                screen.fill(bgcolor)
                textbye=U_FONT.render('Bye!', 1, (linecolor))
                screen.blit(textbye, (WIDTH//2, HEIGHT//2))
                pygame.display.update()
                pygame.time.delay(2000)
def vert_0():
    pygame.draw.line(screen, linecolor, (WIDTH//(2*size), 15), (WIDTH//(2*size), HEIGHT-15), lineWidth)
    pygame.display.update()
    pygame.time.delay(1000)
def vert_1():
    pygame.draw.line(screen, linecolor, (WIDTH//2, 15), (WIDTH//2, HEIGHT-15), lineWidth)
    pygame.display.update()
    pygame.time.delay(1000)
def vert_2():
    pygame.draw.line(screen, linecolor, ((2*size-1)*WIDTH//(2*size), 15), ((2*size-1)*WIDTH//(2*size), HEIGHT-15), lineWidth)
    pygame.display.update()
    pygame.time.delay(1000)
def hori_0():
    pygame.draw.line(screen, linecolor, (15, HEIGHT//(2*size)), (WIDTH-15, HEIGHT//(2*size)), lineWidth)
    pygame.display.update()
    pygame.time.delay(1000)
def hori_1():
    pygame.draw.line(screen, linecolor, (15, HEIGHT//2), (WIDTH-15, HEIGHT//2), lineWidth)
    pygame.display.update()
    pygame.time.delay(1000)
def hori_2():
    pygame.draw.line(screen, linecolor, (15, (2*size-1)*HEIGHT//(2*size)), (WIDTH-15, (2*size-1)*HEIGHT//(2*size)), lineWidth)
    pygame.display.update()
    pygame.time.delay(1000)
def diag_1():
    pygame.draw.line(screen, linecolor, (15, 15), (WIDTH-15, HEIGHT-15), lineWidth)
    pygame.display.update()
    pygame.time.delay(1000)
def diag_2():
    pygame.draw.line(screen, linecolor, (WIDTH-15, 15), (15, HEIGHT-15), lineWidth)
    pygame.display.update()
    pygame.time.delay(1000)
def x_win():
    global X_score
    X_score += 1
    screen.fill(xcolor)
    textx=U_FONT.render('X won!', 1, (linecolor))
    screen.blit(textx, (WIDTH//2, HEIGHT//2))
    pygame.display.update()
    pygame.time.delay(3000)
    agn()
def O_win():
    global O_score
    O_score += 1
    screen.fill(circolor)
    texto=U_FONT.render('O won!', 1, (linecolor))
    screen.blit(texto, (WIDTH//2, HEIGHT//2))
    pygame.display.update()
    pygame.time.delay(3000)
    agn()
def check_winner():
    global Game
    if markers[0][0] + markers[0][1] + markers[0][2] == 3:#vertical
        vert_0()
        x_win()
    elif markers[0][0] + markers[0][1] + markers[0][2] == -3:
        vert_0()
        O_win()
    elif markers[1][0] + markers[1][1] + markers[1][2] == 3:#vertical
        vert_1()
        x_win()
    elif markers[1][0] + markers[1][1] + markers[1][2] == -3:
        vert_1()
        O_win()
    elif markers[2][0] + markers[2][1] + markers[2][2] == 3:#vertical
        vert_2()
        x_win()
    elif markers[2][0] + markers[2][1] + markers[2][2] == -3:
        vert_2()
        O_win()
    elif markers[0][0] + markers[1][0] + markers[2][0] == 3:#horizontal
        hori_0()
        x_win()
    elif markers[0][0] + markers[1][0] + markers[2][0] == -3:
        hori_0()
        O_win()
    elif markers[0][1] + markers[1][1] + markers[2][1] == 3:#horizontal
        hori_1()
        x_win()
    elif markers[0][1] + markers[1][1] + markers[2][1] == -3:
        hori_1()
        O_win()
    elif markers[0][2] + markers[1][2] + markers[2][2] == 3:#horizontal
        hori_2()
        x_win()
    elif markers[0][2] + markers[1][2] + markers[2][2] == -3:
        hori_2()
        O_win()
    elif markers[0][0] + markers[1][1] + markers[2][2] == 3:#diagonal
        diag_1()
        x_win()
    elif markers[0][0] + markers[1][1] + markers[2][2] == -3:#diagonal
        diag_1()
        O_win()
    elif markers[2][0] + markers[1][1] + markers[0][2] == 3:#diagonal
        diag_2()
        x_win()
    elif markers[2][0] + markers[1][1] + markers[0][2] == -3:#diagonal
        diag_2()
        O_win()
    else:
        Game = True

zero_grid()
cnt=0
Game = True
while Game and cnt<9:
    screen.fill(bgcolor)
    draw_grid()
    draw_markers()
    pygame.display.update()
    check_winner()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
                #run=False
                #mainMenu()
            print("You quit")
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            cnt+=1
            MxMy=pygame.mouse.get_pos()
            cellx=MxMy[0]//(WIDTH//size)
            celly=MxMy[1]//(HEIGHT//size)
            print(markers)
            if markers[cellx][celly]==0:
                markers[cellx][celly]=player
                player *=-1
if cnt==9:
    screen.fill(linecolor)
    cnttext = U_FONT.render('Nobody won.', 1, (bgcolor))
    screen.blit(cnttext, (10, HEIGHT//2))
    pygame.display.update()
    pygame.time.delay(2000)
    agn()