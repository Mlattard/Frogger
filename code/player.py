import pygame, sys
from os import walk

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprite):
        super().__init__(groups)
        
        # image
        self.import_assets()
        self.frame_index = 0
        self.status = 'down'
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)

        # float based movement
        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2()
        self.speed = 200

        # collisions
        self.collisions_sprite = collision_sprite


    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.collisions_sprite.sprites():
                if sprite.rect.colliderect(self.rect):
                    if hasattr(sprite, 'name') and sprite.name == 'car':
                        pygame.quit()
                        sys.exit()
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                        self.pos.x = self.rect.centerx
                    if self.direction.x < 0 :
                        self.rect.left = sprite.rect.right
                        self.pos.x = self.rect.centerx

        else:
            for sprite in self.collisions_sprite.sprites():
                if sprite.rect.colliderect(self.rect):
                    if hasattr(sprite, 'name') and sprite.name == 'car':
                        pygame.quit()
                        sys.exit()
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                        self.pos.y = self.rect.centery
                    if self.direction.y < 0 :
                        self.rect.top = sprite.rect.bottom
                        self.pos.y = self.rect.centery
        

    def import_assets(self):
        self.animations = {}
        for index, folder in enumerate(walk('graphics/player')):
            if index == 0:
                for name in folder[1]:
                    self.animations[name] = []
            else: 
                for file_name in folder[2]:
                    path = folder[0].replace('\\', '/') + '/' + file_name
                    surf = pygame.image.load(path).convert_alpha()
                    key = folder[0].split('\\')[1]
                    self.animations[key].append(surf)

    def animate(self, dt):
        current_animation = self.animations[self.status]
        if self.direction.magnitude() != 0:
            self.frame_index += 10 * dt
            if self.frame_index > len(current_animation):
                self.frame_index = 0
        else:
            self.frame_index = 0
        
        self.image = current_animation[int(self.frame_index)]

    def move(self, dt):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        # horizontal movement + collision
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = (round(self.pos.x))
        self.collision('horizontal')

        # vertical movement + collision
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = (round(self.pos.y))
        self.collision('vertical')
        

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        else:
            self.direction.x = 0

        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0          

    def update(self, dt):
        self.input()
        self.move(dt)
        self.animate(dt)