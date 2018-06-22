#snake Game

import pygame
import sys
import random
import time

errors=pygame.init()
if errors[1]>0:
    print("(!)It has some error in game......")
    sys.exit(-1)
else:
    print("It has successfully game......")

#play board
game_board=pygame.display.set_mode((800,500))
#time.sleep(3)
pygame.display.set_caption("Snake Game!!")
#time.sleep(3)

#colours in game
red=pygame.Color(255,0,0)#gameover
green=pygame.Color(0,255,0)#snake
black=pygame.Color(0,0,0)#score
white=pygame.Color(255,255,255)#background
brown=pygame.Color(0,0,255)#food

#frames per second(FPS) controller
fpsController=pygame.time.Clock()

#important varibles
snakepos=[100,50]
snakebody=[[100,50],[90,50],[80,50]]

foodPlace=[random.randrange(1,80)*10,random.randrange(1,50)*10]
foodSpawn=True

direction="RIGHT"
change_dir=direction
score=0

#Game over function

def gameover():
    mymsgfont=pygame.font.SysFont("monaco",72)
    Gover_surface=mymsgfont.render('Game over!',True,red)
    Gamerect=Gover_surface.get_rect()
    Gamerect.midtop=(400,250)
    game_board.blit(Gover_surface,Gamerect)
    Showscore(2)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()#pygame quit
    sys.exit()#console exit

#score function
def Showscore(option=1):
    scorefont=pygame.font.SysFont('monaco',30)
    scoresurface=scorefont.render("Score:{0}".format(score),True,black)
    scorerect=scoresurface.get_rect()
    if option==1:
        scorerect.midtop=(50,10)
    else:
        scorerect.midtop=(410,300)
        
    game_board.blit(scoresurface,scorerect)
    #pygame.display.flip()
    #time.sleep(5)
   


    
#main logic for the game
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key== pygame.K_RIGHT or event.key ==ord('d'):
                change_dir='RIGHT'
            if event.key== pygame.K_LEFT or event.key ==ord('a'):
                change_dir='LEFT'
            if event.key== pygame.K_UP or event.key ==ord('w'):
                change_dir='UP'
            if event.key== pygame.K_DOWN or event.key ==ord('s'):
                change_dir='DOWN'
            if event.key== pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
                
    #validation for direction

    if change_dir=='RIGHT' and not direction=='LEFT':
        direction='RIGHT'
    if change_dir=='LEFT' and not direction=='RIGHT':
        direction='LEFT'
    if change_dir=='UP' and not direction=='DOWN':
        direction='UP'
    if change_dir=='DOWN' and not direction=='UP':
        direction='DOWN'

#SNAKE POSITION [X,Y]
    if direction=='RIGHT':
        snakepos[0] +=10
    if direction=='LEFT':
        snakepos[0] -=10
    if direction=='UP':
        snakepos[1] -=10
    if direction=='DOWN':
        snakepos[1] +=10

#SNAKE BODY BUILDING
    snakebody.insert(0,list(snakepos))
    if snakepos[0]==foodPlace[0] and snakepos[1]==foodPlace[1]:
        score +=1
        foodSpawn=False
    else:
        snakebody.pop()
    if foodSpawn == False:
        foodPlace=[random.randrange(1,80)*10,random.randrange(1,50)*10]
    foodSpawn=True

    game_board.fill(white)
    for pos in snakebody:
        pygame.draw.rect(game_board,green,pygame.Rect(pos[0],pos[1],10,10))
    pygame.draw.rect(game_board,brown,pygame.Rect(foodPlace[0],foodPlace[1],10,10))
    if snakepos[0]>790 or snakepos[0]<0:
        gameover()
    if snakepos[1]>490 or snakepos[1]<0:
        gameover()
    for block in snakebody[1:]:
        if snakepos[0]==block[0] and snakepos[1]==block[1]:
            gameover()
    
    Showscore()
    pygame.display.flip()
    fpsController.tick(25)
    




        



    
    
    



