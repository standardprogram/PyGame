#encoding:utf8
'''
Created on 2016年2月28日

@author: zhao
'''

import math
import pygame
from pygame.locals import *
from random import random

   
if __name__ == '__main__':
    compeleted = False
    blue = 0, 0, 200
    color = 200, 80, 60
    width = 4
    x = 300
    y = 250
    radius = 200
    position = x - radius, y-radius, radius*2, radius*2
    
    pygame.init()
    screen = pygame.display.set_mode((600,500))
    pygame.display.set_caption('The Pie Game')
    myfont = pygame.font.Font(None, 60)
    
    piece1 = False
    piece2 = False
    piece3 = False
    piece4 = False

    while True:
        for event in pygame.event.get():
            
            if event.type == QUIT:
                exit()
            elif event.type == KEYUP:
                if compeleted:
                    color = (random()*255,random()*255,random()*255)
                    compeleted = False
                    piece1 = False
                    piece2 = False
                    piece3 = False
                    piece4 = False
                else:
                    if event.key == pygame.K_ESCAPE:
                        exit()
                    elif event.key == pygame.K_1:
                        piece1 = True
                    elif event.key == pygame.K_2:
                        piece2 = True
                    elif event.key == pygame.K_3:
                        piece3 = True
                    elif event.key == pygame.K_4:
                        piece4 = True
                    else:
                        piece1 = False
                        piece2 = False
                        piece3 = False
                        piece4 = False
                    
    
        #clear screen
        screen.fill(blue)
        
        #draw the four numbers
        textImg1 = myfont.render("1", True, color)
        screen.blit(textImg1, (x+radius/2-20, y-radius/2))
        
        textImg2 = myfont.render("2", True, color)
        screen.blit(textImg2, (x-radius/2, y-radius/2))
        
        textImg3 = myfont.render("3", True, color)
        screen.blit(textImg3, (x-radius/2, y+radius/2-20))
        
        textImg4 = myfont.render("4", True, color)
        screen.blit(textImg4, (x+radius/2-20, y+radius/2-20))
        
        #should the picece be drawn?
        if piece1:
            start_angle = math.radians(0)
            end_angle = math.radians(90)
            pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
            pygame.draw.line(screen, color, (x, y), (x,y-radius), width)
            pygame.draw.line(screen, color, (x, y), (x+radius, y), width)
        
        if piece2:
            start_angle = math.radians(90)
            end_angle = math.radians(180)
            pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
            pygame.draw.line(screen, color, (x, y), (x,y-radius), width)
            pygame.draw.line(screen, color, (x, y), (x-radius, y), width)
            
        if piece3:
            start_angle = math.radians(180)
            end_angle = math.radians(270)
            pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
            pygame.draw.line(screen, color, (x, y), (x-radius,y), width)
            pygame.draw.line(screen, color, (x, y)            , (x, y+radius), width)
            
        if piece4:
            start_angle = math.radians(270)
            end_angle = math.radians(360)
            pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
            pygame.draw.line(screen, color, (x, y), (x,y+radius), width)
            pygame.draw.line(screen, color, (x, y), (x+radius, y), width)
        
        pygame.display.update()
        
        if piece1 and piece2 and piece3 and piece4:
            compeleted = True
                 
        
        