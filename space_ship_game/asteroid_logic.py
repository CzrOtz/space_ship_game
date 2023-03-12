import pygame
import random

pygame.init

def asteroid_1_movement(x_for_asteroid1, y_for_asteroid1, rect_for_asteroid1, WINDOW_HEIGHT, WINDOW_WIDTH):
    x_for_asteroid1 -= 10
    y_for_asteroid1 = random.randint(0, WINDOW_HEIGHT - 50)

    rect_for_asteroid1.x = x_for_asteroid1

    if x_for_asteroid1 < -85:
        rect_for_asteroid1.y = y_for_asteroid1
    
    if x_for_asteroid1 < -85:
        x_for_asteroid1 = WINDOW_WIDTH + 100
    
    return x_for_asteroid1, y_for_asteroid1


    
    
