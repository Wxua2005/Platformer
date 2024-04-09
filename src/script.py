import pygame
def sprite_loader(spritesheet, x, y, width, height, scale):

    '''
    Loads a spritesheet and cuts the desired area of an individual sprite
    and transforms it according to the scale
    (width, height) = width and height in pixels of individual sprites in sheet
    '''
    
    temp_surf = pygame.Surface((width, height))  #temporary surface
    temp_surf.set_colorkey((0,0,0)) # sets the transparency
    image = pygame.image.load(spritesheet) #loads the spritesheet (with all the sprites in a row or table)
    temp_surf.blit(image, (0, 0), (x * width, y * width , width, height)) # blits the loaded sheet with specific area(i.e the individual sprite)
    image = pygame.transform.scale(temp_surf, (width * scale, height * scale))
    
    return image

def resetAnimation(player, state):
        player.idle = False
        player.run = False
        player.doubleJump = False
        player.state = True

