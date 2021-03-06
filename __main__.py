import pygame
import sys
import random


pygame.init()


display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Gayme')

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

cat_width = 25
cat_height = 25
clock = pygame.time.Clock()

catImg = pygame.image.load('cat.png')
catImg = pygame.transform.scale(catImg, (150,150))

catScene = pygame.image.load('catscene.jpg')
catScene = pygame.transform.scale(catScene, (800,600))

pickle = pygame.image.load('pickle.png')
pickle = pygame.transform.scale(pickle, (175,175))

catSong = pygame.mixer.music.load('song.mp3')


def pickle_num(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("mews: "+str(count), True, white)
    gameDisplay.blit(text(0,0))

def game_song(song):

    pygame.mixer.music.set_volume(0.55)
    pygame.mixer.music.play(loops=-1, start=0.0)

def things(thingx, thingy, thingw, thingh, image):
    gameDisplay.blit(pickle, (thingx,thingy,thingw,thingh))

def cat(x,y):

    gameDisplay.blit(catScene, ((x/(display_width)), (y/(display_height))))
    gameDisplay.blit(catImg, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def message(text):
    largeText = pygame.font.Font('freesansbold.ttf',80)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()


    pygame.time.delay(500)

    game_loop()

def pickle_num(count):
    font = pygame.font.SysFont(None, 50)
    text = font.render("mews: "+str(count), True, white)
    gameDisplay.blit(text, (0,0))

def crash():
    message("*blep*")
    return game_loop()

def game_loop():

    x = (display_width * 0.46)
    y = (display_height * 0.45)
    x_change = 0
    y_change = 0
    gameExit = False

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 50
    thing_height = 50

    dodged = 0




    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pygame.transform.flip(gameDisplay, 180, 0)
                    x_change = -10
                elif event.key == pygame.K_UP:
                    y_change = -10
                elif event.key == pygame.K_DOWN:
                    y_change = 10
                elif event.key == pygame.K_RIGHT:
                    x_change = 10
                elif event.key -- pygame.K_ESCAPE:
                    pygame.quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        x += x_change
        y += y_change

        gameDisplay.fill(white)
        cat(x,y)
        pickle_num(dodged)
        things(thing_startx, thing_starty, thing_width, thing_height, pickle)
        thing_starty += thing_speed


        if x > display_width - cat_width or x < 0:
            crash()
        if y > display_height - cat_height or y < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)



        if y > thing_starty and y < thing_starty + thing_height or y+cat_height > thing_starty and y + cat_height < thing_starty+thing_height:
            print("y crossover")
            if x > thing_startx and x < thing_startx + thing_width or x+cat_width > thing_startx and x + cat_width < thing_startx+thing_width:
                print("x crossover")
                crash()




        pygame.display.update()

game_song(catSong)
game_loop()
pygame.quit()
quit()
