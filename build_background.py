import random
import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)
        color = (17, 2, 39)
        self.width = width
        self.height = height
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
            
class Star_Background(pygame.sprite.Sprite):
    def __init__(self, width, height, speed, nums, is_alt=False):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.speed = speed
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.stars = [pygame.transform.scale(pygame.image.load('Image/Background/Star/Star_1.png').convert_alpha(), (3, 3)),
                      pygame.transform.scale(pygame.image.load('Image/Background/Star/Star_2.png').convert_alpha(), (15, 15)),
                      pygame.transform.scale(pygame.image.load('Image/Background/Star/Star_3.png').convert_alpha(), (15, 15)),
                      pygame.transform.scale(pygame.image.load('Image/Background/Star/Star_4.png').convert_alpha(), (15, 15)),
                      pygame.transform.scale(pygame.image.load('Image/Background/Star/Star_5.png').convert_alpha(), (15, 15))]
        
        for _ in range(nums):
            x = random.randrange(0, self.width)
            y = random.randrange(0, self.height)
            type_ = random.randrange(0, 5)
            self.image.blit(self.stars[type_], (x, y))
            
        # 判断是否是交替图像，如果是，需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height    
            
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= self.height:
            self.rect.y = -self.rect.height