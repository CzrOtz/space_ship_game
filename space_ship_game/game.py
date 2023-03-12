import pygame
from sys import exit
from ship_logic import *
from asteroid_logic import *
import random


def game():
    
    pygame.init()
    
   

    WINDOW_WIDTH = 800

    WINDOW_HEIGHT = 600

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('SPACE RACE')

    #fps 
    clock = pygame.time.Clock()
    FPS = 60


    load_background = pygame.image.load('pictures/space_background.png')
    load_spaceship = pygame.image.load('pictures/new_spaceship.png')
    load_asteroid_1 =  pygame.image.load('pictures/meteor1.png')
    load_asteroid_2 =  pygame.image.load('pictures/meteor2.png')
    load_asteroid_3 =  pygame.image.load('pictures/meteor3.png')

    background = pygame.transform.scale(load_background, (1000, 1000))
    spaceship = pygame.transform.scale(load_spaceship, (200, 200))
    asteroid_1 = pygame.transform.scale(load_asteroid_1, (85, 85))
    asteroid_2 = pygame.transform.scale(load_asteroid_2, (85, 85))
    asteroid_3 = pygame.transform.scale(load_asteroid_3, (85, 85))


    #starting position of the ship is in the center of the screen
    x_for_ship = WINDOW_WIDTH // 2
    y_for_ship = WINDOW_HEIGHT // 2
    
    x_for_asteroid1 = 100
    y_for_asteroid1 = 100

    x_for_normal_asteroids2 = 100
    y_for_normal_asteroids2 = 100

    x_for_normal_asteroids3 = 500
    y_for_normal_asteroids3 = 500

    x_for_background_blit = 10

    make_game_faster = 0

    #the asteroids are always going to 
    moving_up = False
    moving_down = False
    moving_left = False
    moving_right = False


    #pygame.Rect(x, y, width, heigth)
    rect_for_spaceship = pygame.Rect(x_for_ship, y_for_ship, 100, 100)
    rect_for_asteroid1 = pygame.Rect(x_for_asteroid1, y_for_asteroid1, 100, 100)
    rect_for_asteroid2 = pygame.Rect(x_for_normal_asteroids2, y_for_normal_asteroids2, 100, 100)
    rect_for_asteroid3 = pygame.Rect(x_for_normal_asteroids3, y_for_normal_asteroids3, 100, 100)


    game_running = True

    while game_running:

        make_game_faster += 0.001


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


            if event.type == pygame.KEYDOWN:
                moving_up, moving_down, moving_left, moving_right = ship_move_pt0(
                    event, moving_up, moving_down, moving_left, moving_right
                )
              
            elif event.type == pygame.KEYUP:
               moving_up, moving_down, moving_left, moving_right = ship_move_pt00(
                   event, moving_up, moving_down, moving_left, moving_right
               )

        #############make the game faster

      


        #############

        # move the ship continuously as long as the corresponding key is pressed

        #the return statement is assigning the new values to the elements on the left hand side of the operator, wont 
        #work without it
        x_for_ship, y_for_ship = ship_move_pt1(moving_up, moving_down, moving_left, moving_right, x_for_ship, y_for_ship, make_game_faster)
      
        x_for_ship, y_for_ship = ship_boundaries(x_for_ship, y_for_ship, WINDOW_WIDTH, WINDOW_HEIGHT)



        ################################     
        x_for_background_blit -= 5 + make_game_faster

        if x_for_background_blit < -75:
            x_for_background_blit = 35

        ###############################    


        #asteroid 1 logic
        ###################################################
        x_for_asteroid1 -= 12 + make_game_faster
        y_for_asteroid1 = random.randint(0, WINDOW_HEIGHT - 50)

        rect_for_asteroid1.x = x_for_asteroid1 
        
        if x_for_asteroid1 < -85:
            rect_for_asteroid1.y = y_for_asteroid1
            x_for_asteroid1 = WINDOW_WIDTH + 100

        
            
        #######################################################

        ########Asteroid 2 logig ############
        x_for_normal_asteroids2 -= 8 + make_game_faster
        y_for_normal_asteroids2 = random.randint(0, WINDOW_HEIGHT - 50)

        rect_for_asteroid2.x = x_for_normal_asteroids2

        if x_for_normal_asteroids2 < -85:
            rect_for_asteroid2.y = y_for_normal_asteroids2
            x_for_normal_asteroids2 = WINDOW_WIDTH + 100 

        #####################################

        ##########  Asteroid 3 logic #############

        x_for_normal_asteroids3 -= 10 + make_game_faster
        y_for_normal_asteroids3 = random.randint(0, WINDOW_HEIGHT - 50)
        
        rect_for_asteroid3.x = x_for_normal_asteroids3

        if x_for_normal_asteroids3 < -85:
            rect_for_asteroid3.y= y_for_normal_asteroids3
            x_for_normal_asteroids3 = WINDOW_WIDTH + 100

        ##########################################


        ############### make the ship move #########

        rect_for_spaceship.x = x_for_ship
        rect_for_spaceship.y = y_for_ship

        ########## Make the ship move ######


        if rect_for_spaceship.colliderect(rect_for_asteroid1):
            print(' COLLIDE WORKS')
        
        
        
        screen.blit(background, (x_for_background_blit,0))
        screen.blit(spaceship, rect_for_spaceship)

        
        screen.blit(asteroid_1, rect_for_asteroid1)
        screen.blit(asteroid_2, rect_for_asteroid2)
        screen.blit(asteroid_3, rect_for_asteroid3)
            

        pygame.display.flip()

        clock.tick(FPS)




game()
            