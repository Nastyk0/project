import sqlite3
import pygame
from random import randint
import random
import os
import sys

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
    pygame.draw.rect(screen, (0, 0, 0), (text_x1, text_y1, text_w, text_h), 1)
    pygame.draw.rect(screen, (140, 255, 50), (text_x1 + 1, text_y1 + 40, text_w, text_h - 35), 0)
    pygame.draw.rect(screen, (140, 255, 50), (text_x1 + 200, text_y1 + 1, text_w - 196, text_h + 4), 0)


FPS = 50
if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Змейка')
    size = width, height = 900, 500
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


group = pygame.sprite.Group()


class Snake(pygame.sprite.Sprite):
    imag = load_image("snake.png")
    image = pygame.transform.scale(imag, (110, 35))
    imag = load_image("snake.png")
    image0 = pygame.transform.scale(imag, (110, 35))
    imag = load_image("snake1.png")
    image1 = pygame.transform.scale(imag, (35, 110))
    imag = load_image("snake2.png")
    image2 = pygame.transform.scale(imag, (110, 35))
    imag = load_image("snake3.png")
    image3 = pygame.transform.scale(imag, (35, 110))

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Snake.image
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 200
        self.over = -1
        self.r = False
        self.d = False
        self.u = False
        self.le = False

    def left(self):
        self.le = True
        if self.u:
            self.rect.y -= 13
            self.rect.x += 10
            self.u = False
        elif self.r:
            self.rect.x += 50
            self.r = False
        elif self.d:
            self.rect.y += 30
            self.rect.x += 30
            self.d = False
        self.image = self.image0
        if not pygame.sprite.spritecollideany(self, meal):
            self.rect = self.rect.move(-2, 0)
        else:
            apple.update()
        if pygame.sprite.spritecollideany(self, horizontal_borders) \
                or pygame.sprite.spritecollideany(self, vertical_borders):
            self.over = 0

    def up(self):
        self.u = True
        if self.le:
            self.rect.x -= 20
            self.rect.y -= 20
            self.le = False
        elif self.r:
            self.rect.x += 70
            self.rect.y -= 30
            self.r = False
        elif self.d:
            self.d = False
        self.image = self.image1
        if not pygame.sprite.spritecollideany(self, meal):
            self.rect = self.rect.move(0, -2)
        else:
            apple.update()
        if pygame.sprite.spritecollideany(self, horizontal_borders) \
                or pygame.sprite.spritecollideany(self, vertical_borders):
            self.over = 0

    def right(self):
        self.r = True
        if self.u:
            self.u = False
        elif self.le:
            self.le = False
        elif self.d:
            self.rect.y += 50
            self.rect.x -= 50
            self.d = False
        self.image = self.image2
        if not pygame.sprite.spritecollideany(self, meal):
            self.rect = self.rect.move(2, 0)
        else:
            apple.update()
        if pygame.sprite.spritecollideany(self, horizontal_borders) \
                or pygame.sprite.spritecollideany(self, vertical_borders):
            self.over = 0

    def down(self):
        self.d = True
        if self.u:
            self.u = False
        elif self.r:
            self.rect.x += 65
            self.rect.y -= 20
            self.r = False
        elif self.le:
            self.rect.y -= 30
            self.le = False
        self.image = self.image3
        if not pygame.sprite.spritecollideany(self, meal):
            self.rect = self.rect.move(0, 2)
        else:
            apple.update()
        if pygame.sprite.spritecollideany(self, horizontal_borders) \
                or pygame.sprite.spritecollideany(self, vertical_borders):
            self.over = 0

    def game_over(self):
        return self.over


class Apple(pygame.sprite.Sprite):
    im = load_image("apple.png")
    image = pygame.transform.scale(im, (30, 30))

    def __init__(self):
        super().__init__(all_sprites)
        self.add(meal)
        self.image = Apple.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = randint(50, 850)
        self.rect.y = randint(50, 450)
        self.score = 0

    def update(self):
        self.rect.x = randint(50, 850)
        self.rect.y = randint(50, 450)
        self.score += 1
        self.count()

    def count(self):
        return self.score


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


def drew(screen, score, record):
    screen.fill((67, 97, 94))
    font = pygame.font.Font(None, 30)
    text = font.render(f"Съедено яблок: {score}", True, (100, 255, 100))
    text1 = font.render(f"Рекорд: {record}", True, (100, 255, 100))
    text_x = 10
    text_y = 10
    screen.blit(text, (text_x, text_y))
    screen.blit(text1, (210, 10))


def over(screen, score, record, victory):
    screen.fill((3, 97, 94))
    font = pygame.font.Font(None, 30)
    font0 = pygame.font.Font(None, 50)
    text0 = font0.render('Игра окончена!', True, (30, 30, 30))
    text = font.render(f"Съедено яблок: {score}", True, (190, 240, 100))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2 - 50
    screen.blit(text0, (text_x - 20, text_y))
    screen.blit(text, (text_x + 10, text_y + 50))
    text1 = font.render(f"Рекорд: {record}", True, (190, 240, 100))
    screen.blit(text1, (text_x + 10, text_y + 80))
    if victory:
        pygame.draw.rect(screen, (0, 255, 0), (300, 350, 170, 50), 3)
        text2 = font.render(f"Рекорд побит!", True, (0, 255, 0))
        screen.blit(text2, (310, 365))
    else:
        pygame.draw.rect(screen, (255, 0, 0), (280, 350, 190, 50), 3)
        text2 = font.render(f"Рекорд не побит", True, (255, 0, 0))
        screen.blit(text2, (290, 365))


meal = pygame.sprite.Group()
orientation = -1
all_sprites = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
apple = Apple()
snake = Snake()
Border(0, 30, width + 5, -5)
Border(0, height + 5, width + 5, height + 5)
Border(-5, 30, -5, height + 5)
Border(width + 5, 30, width + 5, height + 5)
score = 0
victory = False
con = sqlite3.connect('data/record.db')
cur = con.cursor()
records = cur.execute("SELECT first FROM rec").fetchall()
record = list(records[0])[0]


def games():
    global orientation
    global score
    global record
    global victory
    pygame.init()
    size = width, height = 900, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('level')
    fps = 60
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    orientation = 0
                elif event.key == pygame.K_RIGHT:
                    orientation = 2
                elif event.key == pygame.K_UP:
                    orientation = 1
                elif event.key == pygame.K_DOWN:
                    orientation = 3
            screen.fill((67, 97, 94))
            if snake.game_over() == -1 or snake.game_over() == 1:
                running = True
            else:
                running = False
            score = apple.count()
            if score > record:
                record = score
                cur.execute(f"UPDATE rec SET first={record};")
                con.commit()
                victory = True
            drew(screen, score, record)
            all_sprites.draw(screen)
            if orientation == 0:
                snake.left()
            if orientation == 1:
                snake.up()
            if orientation == 2:
                snake.right()
            if orientation == 3:
                snake.down()
        pygame.display.flip()
        clock.tick(fps)
    size1 = width, height = 900, 500
    screen1 = pygame.display.set_mode(size1)
    pygame.display.set_caption('Game over')
    fps = 50
    clock = pygame.time.Clock()
    running1 = True
    while running1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running1 = False
        screen1.fill((150, 97, 94))
        over(screen1, score, record, victory)
        pygame.display.flip()
        clock.tick(fps)


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
        global text_y1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONUP:
                x1, y1 = event.pos
                if text_x1 <= x1 <= text_w + text_x1 and text_y1 <= y1 <= text_h + text_y1:
                    return rules()
                elif text_x <= x1 <= text_w + text_x and text_y <= y1 <= text_h + text_y:
                    return games()
        draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


start_screen()
pygame.quit()
con.close()
