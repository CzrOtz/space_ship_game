import pygame

pygame.init()

def ship_move_pt0(event, moving_up, moving_down, moving_left, moving_right):
    if event.key == pygame.K_UP or event.key == pygame.K_w:
        moving_up = True
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        moving_down = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        moving_left = True
    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        moving_right = True
    
    return moving_up, moving_down, moving_left, moving_right


def ship_move_pt00(event, moving_up, moving_down, moving_left, moving_right):
     if event.key == pygame.K_UP or event.key == pygame.K_w:
        moving_up = False
     elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        moving_down = False
     elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        moving_left = False
     elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        moving_right = False

     return moving_up, moving_down, moving_left, moving_right
    



def ship_move_pt1(moving_up, moving_down, moving_left, moving_right, x_for_ship, y_for_ship, make_game_faster):

    if moving_up:
        y_for_ship -= 5 + make_game_faster
    if moving_down:
        y_for_ship += 5 + make_game_faster
    if moving_left:
        x_for_ship -= 5 + make_game_faster
    if moving_right:
        x_for_ship += 5 + make_game_faster
            
    return x_for_ship, y_for_ship



def ship_boundaries(x_for_ship, y_for_ship, ww, wh):
     if x_for_ship < -100:
          x_for_ship = ww - 100
     elif x_for_ship > ww:
          x_for_ship = -50
    
     if y_for_ship < 0:
          y_for_ship = wh - 64

     elif y_for_ship > wh:
          y_for_ship = 64

     return x_for_ship, y_for_ship
     



      







      