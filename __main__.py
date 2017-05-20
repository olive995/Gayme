import pygame
import sys

pygame.init()


display_width = 1280
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Gayme')

black = (0,0,0)
white = (255,255,255)
cat_width = 73
cat_height = 73
clock = pygame.time.Clock()
catImg = pygame.image.load('cat.png')
catScene = pygame.image.load('catscene.jpg')
catPickle = pygame.image.load('pickle.png')

def cat(x,y):

    gameDisplay.blit(catImg, (x,y))

def projectile(xp,yp):
    gameDisplay.blit(catPickle, (xp,yp))

def game_loop():

    x = display_width/2
    y = display_height/2
    xp = x
    yp = y
    x_change = 0
    y_change = 0
    xp_change = 0
    yp_change = 0
    gameExit = False
    catPickle = pygame.image.load('pickle.png')




    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                elif event.key == pygame.K_SPACE:
                    xp_change = 5
                    if xp_change > 50:
                        x = 0



            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0


        xp += xp_change
        yp += yp_change
        x += x_change
        y += y_change

        gameDisplay.fill(white)
        cat(x,y)


        if x > display_width - cat_width or x < 0:
            x_change = 0
        if y > display_height - cat_height or y < 0:
            y_change = 0

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
