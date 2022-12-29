import pygame
from random import randint
import os
import sys

pygame.init()
size = width, height = 900, 500
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


pygame.display.set_caption("Easy level")

all_sprites_list = pygame.sprite.Group()
zmeyka_image1 = load_image("zmeyka3.png")
zmeyka_image1.set_colorkey((255, 255, 255))
zmeyka_image = pygame.transform.scale(zmeyka_image1, (50, 30))
zmeyka = pygame.sprite.Sprite(all_sprites_list)
zmeyka.image = zmeyka_image
zmeyka.rect = zmeyka.image.get_rect()
zmeyka.rect.x = 400
zmeyka.rect.y = 200


all_sprites_list1 = pygame.sprite.Group()
meyka_image1 = load_image("zmeyka4.png")
meyka_image1.set_colorkey((255, 255, 255))
meyka_image = pygame.transform.scale(meyka_image1, (50, 19))
meyka = pygame.sprite.Sprite(all_sprites_list1)
meyka.image = meyka_image
meyka.rect = zmeyka.image.get_rect()
meyka.rect.x = 448
meyka.rect.y = 206


all_sprites_list2 = pygame.sprite.Group()
apple_image1 = load_image("apple.png")
apple_image1.set_colorkey((255, 255, 255))
apple_image = pygame.transform.scale(apple_image1, (50, 50))
apple = pygame.sprite.Sprite(all_sprites_list1)
apple.image = apple_image
apple.rect = apple.image.get_rect()
apple.rect.x = randint(0, 900)
apple.rect.y = randint(0, 500)

exit = True
clock = pygame.time.Clock()
while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
    screen.fill((159, 200, 200))
    all_sprites_list.update()
    all_sprites_list1.update()
    all_sprites_list.draw(screen)
    all_sprites_list1.draw(screen)
    all_sprites_list2.update()
    all_sprites_list2.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()