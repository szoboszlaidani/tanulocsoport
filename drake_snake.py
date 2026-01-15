import pygame,random,math,time
pygame.init()
screensize=500
gridsize=20
screen=pygame.display.set_mode((screensize,screensize))

class colors():
    bg=(200,200,200)
    snake=(186,85,43)
    food=(0,255,0)

class snake():
    grid=[]
    prev_snake=[]
    snake=[[10,10,[1,0]],[9,10,[1,0]]]

def gen_grid():
    for y in range(gridsize): snake.grid.append([colors.bg for _ in range(gridsize)])



def main(running):
    gen_grid()
    while running:
        time.sleep(.1)
        for loopsnake in range(len(snake.snake)):
            s=snake.snake[loopsnake]
            s[0]+=s[2][0]
            s[1]+=s[2][1]
            if loopsnake>0 and len(snake.prev_snake)>0:
                s[2][0]=snake.prev_snake[loopsnake-1][2][0]
                s[2][1]=snake.prev_snake[loopsnake-1][2][1]
            
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_s:snake.snake[0][2]=[0,1]
                if event.key==pygame.K_w:snake.snake[0][2]=[0,-1]
                if event.key==pygame.K_a:snake.snake[0][2]=[-1,0]
                if event.key==pygame.K_d:snake.snake[0][2]=[1,0]
        for x in range(len(snake.grid)):
            for y in range(len(snake.grid[x])):
                for s in snake.snake:
                    if s[0]==x and s[1]==y: 
                        snake.grid[s[0]][s[1]]=colors.snake
                    elif snake.grid[s[0]][s[1]]==colors.snake:
                        snake.grid[s[0]][s[1]]=colors.bg
                snake.grid[x][y]
                size=screensize/gridsize
                pygame.draw.rect(screen,snake.grid[x][y],(x*size+1,y*size+1,size-2,size-2))
        pygame.display.update()
        snake.prev_snake=snake.snake
if __name__=="__main__":
    main(True)