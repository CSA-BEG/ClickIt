import pygame, sys
from pygame.locals import *
import time
'''-----------------------------------------------------------------
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
-----------------------------------------------------------------'''

pygame.init()

FPS = 20# frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 500))
pygame.display.set_caption('Mouseman')

WHITE = (255, 255, 255)#colors and pictures setup
GRAY = (211,211,211)
GREY = (170,170,170)
RED = (255,0,0)
BLACK = (0,0,0)
shipImg = pygame.image.load('kirk.png')
laserImg = pygame.image.load('lazer.jpg')

shots=[]

text=pygame.font.Font(None, 45)#text
text2=text.render("Save",6,WHITE)
saved=text.render("Saved",6,WHITE)
quit=text.render("Quit",6,WHITE)
load=text.render("Load",6,WHITE)

soundObj = pygame.mixer.Sound('beam.wav')#sound
rdse=pygame.mixer.Sound('RDSE.wav')

temp=0

mousex=200#start position
mousey=250

laserx=-100
lasery=-100

while True: # the main game loop
    DISPLAYSURF.fill(BLACK)
    DISPLAYSURF.blit(shipImg, ((mousex-30), (mousey-57)))
    laserx-=15
    for shot in shots:
        DISPLAYSURF.blit(laserImg, pygame.Rect(shot[0], shot[1], 0, 0))
    for b in range(len(shots)):
        shots[b][0] -= 10

    #    DISPLAYSURF.blit(laserImg, ((laserx), (lasery)))
    pygame.draw.rect(DISPLAYSURF, GRAY, (20, 20, 85, 40))
    pygame.draw.rect(DISPLAYSURF, GRAY, (295, 20, 85, 40))#drawing objects
    pygame.draw.rect(DISPLAYSURF, GRAY, (155, 20, 85, 40))
    pygame.draw.line(DISPLAYSURF, WHITE, (0, 70), (400, 70), 6)
    for event in pygame.event.get():
        if event.type == QUIT:#little red x
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONUP:#they done click-ed
            mx, my = event.pos
            temp=1
            if mx>=20 and mx<=105 and my>=20 and my<=60:#checking the various buttons
                posi=[mousex,mousey]
                file=open('lastposition.txt','w')
                pygame.draw.rect(DISPLAYSURF, GREY, (20, 20, 85, 40))
                DISPLAYSURF.blit(load, (160, 25))
                DISPLAYSURF.blit(text2, (25, 25))
                DISPLAYSURF.blit(quit, (305, 25))
                file.write(str(posi))
                DISPLAYSURF.blit(saved, (25, 455))
                pygame.display.update()
                time.sleep(3)
            elif mx>=295 and mx<=380 and my>=20 and my<=60:
                pygame.draw.rect(DISPLAYSURF, GREY, (295, 20, 85, 40))
                DISPLAYSURF.blit(load, (160, 25))
                DISPLAYSURF.blit(text2, (25, 25))
                DISPLAYSURF.blit(quit, (305, 25))
                pygame.display.update()
                time.sleep(.5)
                pygame.quit()
                sys.exit()
            elif mx>=155 and mx<=240 and my>=20 and my<=60:
                pygame.draw.rect(DISPLAYSURF, GREY, (155, 20, 85, 40))
                DISPLAYSURF.blit(load, (160, 25))
                DISPLAYSURF.blit(text2, (25, 25))
                DISPLAYSURF.blit(quit, (305, 25))
                pygame.display.update()
                file=open('lastposition.txt','r')
                line=file.readline()
                line=line.replace('[','')
                line=line.replace(']','')
                line=line.split(',')
                print(line)
                mousex=int(line[0])
                mousey=int(line[1])
                time.sleep(.5)
            else:#if they didn't click a button
                mousex=mx
                mousey=my
                soundObj.play()
                if mx>=370:#checking boundaries
                    mousex=370
                    mousey=my
                if mx<=30:
                    mousex=30
                    mousey=my
                if my>=450:
                    mousey=440
                    mousex=mx
                if my<=127:
                    mousey=135
                    mousex=mx


        elif (event.type == KEYUP and event.key == K_UP) or (event.type == KEYUP and event.key == K_w):#up
            my=mousey-5
            mx=mousex
            temp=1
            if mx>=20 and mx<=105 and my>=20 and my<=60:#checking the various buttons
                posi=[mousex,mousey]
                file=open('lastposition.txt','w')
                pygame.draw.rect(DISPLAYSURF, GREY, (20, 20, 85, 40))
                DISPLAYSURF.blit(load, (160, 25))
                DISPLAYSURF.blit(text2, (25, 25))
                DISPLAYSURF.blit(quit, (305, 25))
                file.write(str(posi))
                DISPLAYSURF.blit(saved, (25, 455))
                pygame.display.update()
                time.sleep(3)
            elif mx>=295 and mx<=380 and my>=20 and my<=60:
                pygame.draw.rect(DISPLAYSURF, GREY, (295, 20, 85, 40))
                DISPLAYSURF.blit(load, (160, 25))
                DISPLAYSURF.blit(text2, (25, 25))
                DISPLAYSURF.blit(quit, (305, 25))
                pygame.display.update()
                time.sleep(.5)
                pygame.quit()
                sys.exit()
            elif mx>=155 and mx<=240 and my>=20 and my<=60:
                pygame.draw.rect(DISPLAYSURF, GREY, (155, 20, 85, 40))
                DISPLAYSURF.blit(load, (160, 25))
                DISPLAYSURF.blit(text2, (25, 25))
                DISPLAYSURF.blit(quit, (305, 25))
                pygame.display.update()
                file=open('lastposition.txt','r')
                line=file.readline()
                line=line.replace('[','')
                line=line.replace(']','')
                line=line.split(',')
                print(line)
                mousex=int(line[0])
                mousey=int(line[1])
                time.sleep(.5)
            else:#if they didn't click a button
                mousex=mx
                mousey=my
                soundObj.play()
                if mx>=370:#checking boundaries
                    mousex=370
                    mousey=my
                if mx<=30:
                    mousex=30
                    mousey=my
                if my>=450:
                    mousey=440
                    mousex=mx
                if my<=127:
                    mousey=135
                    mousex=mx

        elif (event.type == KEYUP and event.key == K_DOWN) or (event.type == KEYUP and event.key == K_s):#down
            my=mousey+5
            mx=mousex
            temp=1
            if mx>=20 and mx<=105 and my>=20 and my<=60:#checking the various buttons
                posi=[mousex,mousey]
                file=open('lastposition.txt','w')
                pygame.draw.rect(DISPLAYSURF, GREY, (20, 20, 85, 40))
                DISPLAYSURF.blit(load, (160, 25))
                DISPLAYSURF.blit(text2, (25, 25))
                DISPLAYSURF.blit(quit, (305, 25))
                file.write(str(posi))
                DISPLAYSURF.blit(saved, (25, 455))
                pygame.display.update()
                time.sleep(3)
            elif mx>=295 and mx<=380 and my>=20 and my<=60:
                pygame.draw.rect(DISPLAYSURF, GREY, (295, 20, 85, 40))
                DISPLAYSURF.blit(load, (160, 25))
                DISPLAYSURF.blit(text2, (25, 25))
                DISPLAYSURF.blit(quit, (305, 25))
                pygame.display.update()
                time.sleep(.5)
                pygame.quit()
                sys.exit()
            elif mx>=155 and mx<=240 and my>=20 and my<=60:
                pygame.draw.rect(DISPLAYSURF, GREY, (155, 20, 85, 40))
                DISPLAYSURF.blit(load, (160, 25))
                DISPLAYSURF.blit(text2, (25, 25))
                DISPLAYSURF.blit(quit, (305, 25))
                pygame.display.update()
                file=open('lastposition.txt','r')
                line=file.readline()
                line=line.replace('[','')
                line=line.replace(']','')
                line=line.split(',')
                print(line)
                mousex=int(line[0])
                mousey=int(line[1])
                time.sleep(.5)
            else:#if they didn't click a button
                mousex=mx
                mousey=my
                soundObj.play()
                if mx>=370:#checking boundaries
                    mousex=370
                    mousey=my
                if mx<=30:
                    mousex=30
                    mousey=my
                if my>=450:
                    mousey=440
                    mousex=mx
                if my<=127:
                    mousey=135
                    mousex=mx

        elif (event.type == KEYUP and event.key == K_LEFT) or (event.type == KEYUP and event.key == K_a):#left
            my=mousey
            mx=mousex-5
            temp=1
            if mx>=20 and mx<=105 and my>=20 and my<=60:#checking the various buttons
                posi=[mousex,mousey]
                file=open('lastposition.txt','w')
                pygame.draw.rect(DISPLAYSURF, GREY, (20, 20, 85, 40))
                DISPLAYSURF.blit(load, (160, 25))
                DISPLAYSURF.blit(text2, (25, 25))
                DISPLAYSURF.blit(quit, (305, 25))
                file.write(str(posi))
                DISPLAYSURF.blit(saved, (25, 455))
                pygame.display.update()
                time.sleep(3)
            elif mx>=295 and mx<=380 and my>=20 and my<=60:
                pygame.draw.rect(DISPLAYSURF, GREY, (295, 20, 85, 40))
                DISPLAYSURF.blit(load, (160, 25))
                DISPLAYSURF.blit(text2, (25, 25))
                DISPLAYSURF.blit(quit, (305, 25))
                pygame.display.update()
                time.sleep(.5)
                pygame.quit()
                sys.exit()
            elif mx>=155 and mx<=240 and my>=20 and my<=60:
                pygame.draw.rect(DISPLAYSURF, GREY, (155, 20, 85, 40))
                DISPLAYSURF.blit(load, (160, 25))
                DISPLAYSURF.blit(text2, (25, 25))
                DISPLAYSURF.blit(quit, (305, 25))
                pygame.display.update()
                file=open('lastposition.txt','r')
                line=file.readline()
                line=line.replace('[','')
                line=line.replace(']','')
                line=line.split(',')
                print(line)
                mousex=int(line[0])
                mousey=int(line[1])
                time.sleep(.5)
            else:#if they didn't click a button
                mousex=mx
                mousey=my
                soundObj.play()
                if mx>=370:#checking boundaries
                    mousex=370
                    mousey=my
                if mx<=30:
                    mousex=30
                    mousey=my
                if my>=450:
                    mousey=440
                    mousex=mx
                if my<=127:
                    mousey=135
                    mousex=mx


        elif (event.type == KEYUP and event.key == K_RIGHT) or (event.type == KEYUP and event.key == K_d):#right
            my=mousey
            mx=mousex+5
            temp=1
            if mx>=20 and mx<=105 and my>=20 and my<=60:#checking the various buttons
                posi=[mousex,mousey]
                file=open('lastposition.txt','w')
                pygame.draw.rect(DISPLAYSURF, GREY, (20, 20, 85, 40))
                DISPLAYSURF.blit(load, (160, 25))
                DISPLAYSURF.blit(text2, (25, 25))
                DISPLAYSURF.blit(quit, (305, 25))
                file.write(str(posi))
                DISPLAYSURF.blit(saved, (25, 455))
                pygame.display.update()
                time.sleep(3)
            elif mx>=295 and mx<=380 and my>=20 and my<=60:
                pygame.draw.rect(DISPLAYSURF, GREY, (295, 20, 85, 40))
                DISPLAYSURF.blit(load, (160, 25))
                DISPLAYSURF.blit(text2, (25, 25))
                DISPLAYSURF.blit(quit, (305, 25))
                pygame.display.update()
                time.sleep(.5)
                pygame.quit()
                sys.exit()
            elif mx>=155 and mx<=240 and my>=20 and my<=60:
                pygame.draw.rect(DISPLAYSURF, GREY, (155, 20, 85, 40))
                DISPLAYSURF.blit(load, (160, 25))
                DISPLAYSURF.blit(text2, (25, 25))
                DISPLAYSURF.blit(quit, (305, 25))
                pygame.display.update()
                file=open('lastposition.txt','r')
                line=file.readline()
                line=line.replace('[','')
                line=line.replace(']','')
                line=line.split(',')
                print(line)
                mousex=int(line[0])
                mousey=int(line[1])
                time.sleep(.5)
            else:#if they didn't click a button
                mousex=mx
                mousey=my
                soundObj.play()
                if mx>=370:#checking boundaries
                    mousex=370
                    mousey=my
                if mx<=30:
                    mousex=30
                    mousey=my
                if my>=450:
                    mousey=440
                    mousex=mx
                if my<=127:
                    mousey=135
                    mousex=mx

        elif event.type == KEYUP and event.key == K_z:
            rdse.play(1)
            shots.append([mousex-39,mousey-44])

    DISPLAYSURF.blit(text2, (25, 25))
    DISPLAYSURF.blit(load, (160, 25))
    DISPLAYSURF.blit(quit, (305, 25))
    pygame.display.update()
    fpsClock.tick(FPS)
