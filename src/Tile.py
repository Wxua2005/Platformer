import pygame

class Tile(pygame.sprite.Sprite):
    TILESIZE = 16
    def __init__(self, x, y, surface, group):
        super().__init__(group)
        self.image = surface
        self.rect = self.image.get_rect(topleft = (x * Tile.TILESIZE,y * Tile.TILESIZE))




