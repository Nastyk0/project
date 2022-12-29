import sys
import os
import pygame

FPS = 50
if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Правила игры')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()


def terminate():
    pygame.quit()
    sys.exit()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    return image


def rules():
    intro_text = ["Правила игры:", "",
                "Игрок управляет змейкой при помощи кнопок ",
                "направления — вверх, вниз, влево, вправо.",
                "Ползая, змейка должна собирать яблоки, ",
                "за которые начисляются очки.",
                "Игра заканчивается, если змейка ",
                    "врезается в стену или в препятствие",
                    "Цель игры — набрать как можно",
                    "больше очков. Приятной игры!"]
    running = True
    fon = pygame.transform.scale(load_image('змейка2.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 40)
    text_coord = 10
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Rule.terminate()
        pygame.display.flip()
        clock.tick(FPS)


rules()
