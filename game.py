#!/usr/bin/env python

###########################################################################################################################
# Simplest Pseudo 3D Game
# (C) 2023 Norbert Michael Mayer
# GPL License 3.0
# No comments -- sorry!
###########################################################################################################################


#import everything
import os, pygame
from pygame.locals import *
from pygame import *
import math
import random

screen_size_x=1024
screen_size_y=800


def draw_stars(screen,stars,direction):
    global moon_image,dest_image, satu_image
    for i in stars:
        a=i[0]
        y=i[1]
        x=math.sin(a+direction)*screen_size_x
        x2 = math.cos(a+direction)
        if abs(x)<(screen_size_x/2) and x2>0. and random.random() < 0.995:
            screen.set_at((int(x+(screen_size_x/2)),int(y)),(255,255,255))


def lines_h(screen, offset):
    for i in range(screen_size_y/8):
       z=i*10+20-offset
       y = int((300.+3000.0/z)*screen_size_y/600)
       pygame.draw.line(screen, (255-i*2,255-i*2,255), (0,y),(screen_size_x-1,y) , 1) 


def lines_v(screen, offset):
    for i in range(-41,41):
       x=i*screen_size_x/5+offset
       pygame.draw.line(screen, (255,255,255), (screen_size_x/2,screen_size_y/2),(x,screen_size_y-1) , 1) 



def create_stars():
    li=[]
    for i in range(3500):
        a = random.random()*2*math.pi
        y = random.random()*screen_size_y/2
        li.append([a,y])
    return li



def main():
    pygame.init()
    pygame.key.set_repeat(50,50)
    screen = pygame.display.set_mode((screen_size_x,screen_size_y))
    x = 0.
    y = 0.
    clock = pygame.time.Clock()
    pygame.display.flip()
    going = True
    offset=0
    turn =0.
    sx=0.
    sy=0.
    direction = 0.
    speed=0.
    stars = create_stars()
    while going:
        clock.tick(40)
        screen.fill((10,10,10));
        lines_v(screen, int(turn))
        lines_h(screen, offset)
        draw_stars(screen,stars,direction)
        pygame.draw.line(screen, (0,0,255), (0,screen_size_y/2),(screen_size_x-1,screen_size_y/2) , int(screen_size_y/200+1))


        offset = offset + speed
        offset = offset % 10

        for event in pygame.event.get():
            if event == QUIT:
                going = False
            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    turn = turn -10
                    direction = direction + 0.01
                if event.key == K_RIGHT:
                    turn = turn +10
                    direction = direction - 0.01
                if event.key == K_UP:
                    speed +=0.05
                if event.key == K_DOWN:
                    speed -=0.05
                if event.key == K_ESCAPE:
                    pygame.display.toggle_fullscreen()
                if event.key == K_q:
                    going=false
                if event.key == K_SPACE:
                    sx=x
                    sy=y


        turn = turn %(screen_size_x/5)
        direction = (direction + 2*math.pi )% (2*math.pi)
        x -= math.sin(direction)*speed
        y += math.cos(direction)*speed
        sx -= 50*math.sin(direction)*speed
        sy += 50*math.cos(direction)*speed
        #print direction

        pygame.display.flip()
        
	
if __name__ == '__main__':
    main()

