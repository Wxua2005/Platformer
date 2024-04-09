import pygame, sys
from player import Character
from constants import spriteSheets
from pytmx.util_pygame import load_pygame
from Tile import Tile
from script import resetAnimation

WIDTH , HEIGHT = 800, 500
FPS = 60

pygame.init()

display = pygame.display.set_mode((WIDTH, HEIGHT))
run = True
clock = pygame.time.Clock()
player_rect = pygame.Rect(100, 300, 32, 32)
tmx_data = load_pygame("C:\\Users\\drpre\\AppData\\Local\\Programs\\Python\\Python310\\game1\\map2.tmx")
layer = tmx_data.get_layer_by_name('Tile Layer 1')

mask_dude = Character(player_rect, spriteSheets, 32, 32)
player_group = pygame.sprite.Group()
player_group.add(mask_dude)
tile_group = pygame.sprite.Group()

for x, y, surf in layer.tiles():
    Tile(x, y, surf, tile_group)

vertical_momentum = 0
count = 0
airtimer = 0

while run:
    display.fill("Lightblue")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                mask_dude.run = True
                mask_dude.idle = False
                mask_dude.movement.x = 4

            if event.key == pygame.K_a:
                mask_dude.run = True
                mask_dude.idle = False
                mask_dude.movement.x = - 4

            if event.key == pygame.K_w:

                vertical_momentum = -4


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                mask_dude.run = False
                mask_dude.idle = True
                mask_dude.movement.x = 0

            if event.key == pygame.K_a:
                mask_dude.run = False
                mask_dude.idle = True
                mask_dude.movement.x = 0


    tile_group.draw(display)
    player_group.draw(display)
    direction = mask_dude.move(tile_group)

    if direction['Down']:
        vertical_momentum = 0
        count = 0
        airtimer = 0 # currently not using airtimer anywhere
    else:
        airtimer += 1
    mask_dude.movement.y = vertical_momentum
    vertical_momentum += 0.2

    # print(f'airtimer: {airtimer}')
    # print(f'count : {count}')
    player_group.update()
    clock.tick(FPS)
    pygame.display.update()


pygame.quit()
sys.exit()
