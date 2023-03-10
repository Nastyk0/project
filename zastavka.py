import sys
import os
import pygame

text_x = 10
text_y = 190
text_w = 200
text_h = 40
text_x1 = 10
text_y1 = 240


def draw(screen):
    global text_h
    global text_w
    global text_y
    global text_x
    global text_x1
    global text_y1
    font = pygame.font.Font(None, 50)
    text = font.render("1 уровень", True, (0, 0, 0))
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 0, 0), (text_x, text_y, text_w, text_h), 1)
    pygame.draw.rect(screen, (140, 255, 50), (text_x + 1, text_y + 40, text_w, text_h - 35), 0)
    pygame.draw.rect(screen, (140, 255, 50), (text_x + 200, text_y + 1, text_w - 196, text_h + 4), 0)
    font = pygame.font.Font(None, 40)
    text = font.render("Правила игры", True, (0, 0, 0))
    screen.blit(text, (text_x1, text_y1))
    pygame.draw.rect(screen, (0, 0, 0), (text_x1, text_y1 , text_w, text_h), 1)
    pygame.draw.rect(screen, (140, 255, 50), (text_x1 + 1, text_y1 + 40, text_w, text_h - 35), 0)
    pygame.draw.rect(screen, (140, 255, 50), (text_x1 + 200, text_y1 + 1, text_w - 196, text_h + 4), 0)



FPS = 50
if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Змейка')
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
                return start_screen()
        pygame.display.flip()
        clock.tick(FPS)
def start_screen():
    intro_text = ["Змейка", "",
                  "Привет, друг",
                  "Предлагаем тебе поиграть в змейку"]
    running = True
    fon = pygame.transform.scale(load_image('змейка2.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 50)
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
        global text_h
        global text_w
        global text_y
        global text_x
        global text_x1
        global text_x2
        global text_y1
        global text_y2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONUP:
                x1, y1 = event.pos
                if text_x1 <= x1 <= text_w + text_x1 and text_y1 <= y1 <= text_h + text_y1:
                    return rules()
        draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


start_screen()
