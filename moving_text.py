import pygame
import os
from random import randrange

os.environ['SDL_VIDEO_CENTERED'] = '1'
RES = WIDTH, HEIGHT = 800, 600
FPS = 60

y_speed = 1

font_size = 20
input_text = "GIOVANNI CODE"
input_color = 'yellow'

pygame.init()
screen = pygame.display.set_mode(RES)
pygame.display.set_caption("Text")
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', font_size, bold=True)


def text_display(x, y, chars, color):
    text_length = len(chars)
    while text_length > 0:
        text = font.render(str(chars[text_length - 1]), True, color)
        text_rect = text.get_rect(center=(x, y + font_size * text_length))
        screen.blit(text, text_rect)
        text_length -= 1


x_start = randrange(50, WIDTH - 50, 50)
y_start = randrange(-400, -200, 20)
x_coord = x_start
y_coord = -400

running = True
while running:
    clock.tick(FPS)
    screen.fill('black')

    x_coord = x_coord if y_coord < HEIGHT else randrange(0, WIDTH, 50)
    y_coord = y_coord + y_speed if y_coord < HEIGHT else y_start

    text_display(x_coord, y_coord, input_text, input_color)
    text_display(x_coord, y_coord, input_text, input_color)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
