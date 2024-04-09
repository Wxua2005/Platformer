import pygame
from script import sprite_loader


def collision(player_rect, tilesets):
    hit_list = []
    for tile in tilesets:
        if player_rect.colliderect(tile.rect):
            hit_list.append(tile)
    return hit_list
class Character(pygame.sprite.Sprite):
    def __init__(self, position, spritesheet, width, height):
        super().__init__()
        self.rect = position #Rect
        self.width = width
        self.height = height
        self.current_sprite = 0
        self.animationSpeed = 0.2
        self.images = [self.load_animations(spritesheet[i][0],spritesheet[i][1], 1) for i in range(3)]
        self.image = self.images[0][self.current_sprite]
        self.movement = pygame.math.Vector2(0, 0)
        self.idle = True
        self.run = False
        self.jump = False

    def load_animations(self, spritesheet, animations, scale = 1):
        images = [sprite_loader(spritesheet, int(i), 0,self.width, self.height, scale) for i in range(animations)]
        return images

    def animateIdle(self):
        if int(self.current_sprite) >= len(self.images[0]) - 1:
            self.current_sprite = 0
        self.current_sprite += self.animationSpeed
        self.image = self.images[0][round(self.current_sprite)]

    def animateRun(self):
        if int(self.current_sprite) >= len(self.images[1]) - 1:
            self.current_sprite = 0
        self.current_sprite += self.animationSpeed
        self.image = self.images[1][round(self.current_sprite)]

    def animateJump(self):
        self.image = self.images[2][0]

    def update(self):
        if self.idle:
            self.animateIdle()
        if self.run:
            self.animateRun()
        if self.jump:
            self.animateJump()

    def move(self, tiles):
        collision_type = {'Right': False,
                               'Left': False,
                               'Up': False,
                               'Down': False}
        self.rect.x += self.movement.x
        hit_list = collision(self.rect, tiles)
        for tile in hit_list:
            if self.movement.x > 0:
                collision_type['Right'] = True
                self.rect.right = tile.rect.left
            if self.movement.x < 0:
                collision_type['Left'] = True
                self.rect.left = tile.rect.right

        self.rect.y += self.movement.y
        hit_list = collision(self.rect, tiles)
        for tile in hit_list:
            if self.movement.y > 0:
                collision_type['Down'] = True
                self.rect.bottom = tile.rect.top
            if self.movement.y < 0:
                collision_type['Up'] = True
                self.rect.top = tile.rect.bottom

        return collision_type



