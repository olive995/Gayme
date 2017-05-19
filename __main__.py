import pygame
import sys

pygame.init()


display_width = 800
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

def cat(x,y):

    gameDisplay.blit(catScene, ((x/(display_width)), (y/(display_height))))
    gameDisplay.blit(catImg, (x,y))

def game_loop():

    x =  (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    y_change = 0
    gameExit = False




    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pygame.transform.flip(gameDisplay, 180, 0)
                    x_change = -5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key -- pygame.K_ESCAPE:
                    pygame.quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        x += x_change
        y += y_change

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
