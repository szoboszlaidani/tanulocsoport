import pygame,random,math,time
pygame.init()
dpsize=500
window=pygame.display.set_mode((dpsize,dpsize))

class colors():
    food=(0,255,0)
    bg=(255,255,255)
    snake=(255,0,0)
size,grid=[15,[]]
snake=[[3,3]]
direction=[1,0]
food = [[5,5]]
for _ in range(size): grid.append([colors.bg for _ in range(size)])
snakemoves=[]
running=True
if __name__=="__main__":
    while running:
        time.sleep(.1)
        for i in range(len(snakemoves)):
            snake[i+1][0]+=snakemoves[i][0]
            snake[i+1][1]+=snakemoves[i][1]
        snakemoves=[]
        snake[0][0]+=direction[0]
        snake[0][1]+=direction[1]
        if snake[0][0]>size or snake[0][0]<0 or snake[0][1]>size or snake[0][1]<0:running=False
        for f in range(len(snake)-1):
            x=snake[f][0]-snake[f+1][0]
            y=snake[f][1]-snake[f+1][1]
            snakemoves.append([x,y])

        for event in pygame.event.get():
            if event.type==pygame.QUIT:running=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_s and direction[1]==0:direction=[0,1]
                if event.key==pygame.K_w and direction[1]==0:direction=[0,-1]
                if event.key==pygame.K_d and direction[0]==0:direction=[1,0]
                if event.key==pygame.K_a and direction[0]==0:direction=[-1,0]

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                try:
                    for f in food:
                        if f[0]==x and f[1]==y:
                            grid[f[0]][f[1]]=colors.food
                        else:
                            grid[f[0]][f[1]]=colors.bg
                    for s in snake:
                        if s[0]==x and s[1]==y:
                            if grid[s[0]][s[1]]==colors.snake:running=False
                            if grid[s[0]][s[1]]==colors.food:
                                snake.append([-1,-1])
                                food[0]=[random.randint(0,size),random.randint(0,size)]
                            grid[s[0]][s[1]]=colors.snake
                        else:
                            grid[s[0]][s[1]]=colors.bg
                    pygame.draw.rect(window,grid[x][y],(math.floor(x*(dpsize/size)),math.floor(y*(dpsize/size)),math.ceil(dpsize/size),math.ceil(dpsize/size)))
                except:
                    running=False
        pygame.display.update()