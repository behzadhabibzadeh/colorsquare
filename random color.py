import pygame
from pygame.locals import *
from sys import exit
from random import *

pygame.init()

screen_h = 1080
screen_w = 1080
shape_h = 45
shape_w = 45
colorcount = 3
isgrayBackground = False
patterncolor = Color(250, 250, 250)

screen = pygame.display.set_mode((screen_w, screen_h), 0, 32)
screen.fill((255, 255, 255))


class Rectangle:
    def __init__(self, pos, color, size):
        self.pos = pos
        self.color = color
        self.size = size

    def draw(self):
        pygame.draw.rect(screen, self.color, Rect(self.pos, self.size))


class Pattern:

    def __init__(self, x, y, color):
        self.rList = []
        self.x = x
        self.y = y
        self.color = color
        self.rList.append(Rectangle((x+0, y+0), color, (shape_h, shape_w)))
        for i in range(7):
            self.rList.append(Rectangle((x + (shape_w * randint(1, 4)),
                                         y + (shape_h * randint(1, 4))), color, (shape_h, shape_w)))

    def draw(self):
        for shape in self.rList:
            shape.draw()
          #  pygame.draw.rect(screen, self.color, Rect(self.pos, self.size))


rectangles = []
shapes = []


def initBackground(rList):
    rList.clear()
    colors = []
    if isgrayBackground:
        for c in range(colorcount):
            graycode = randint(200, 255)
            colors.append(Color(graycode, graycode, graycode))

    else:
        for c in range(colorcount):
            colors.append(
                Color(randint(0, 255), randint(0, 255), randint(0, 255)))

    looper = round(screen_w / shape_w)
    print(looper)
    print(len(rList))
    for j in range(round(screen_h / shape_h)):
        for i in range(round(screen_w / shape_w)):
            random_color = colors[randint(0, colorcount - 1)]
            random_pos = (i*shape_w, j*shape_h)
            random_size = (shape_h, shape_w)
            rList.append(Rectangle(random_pos, random_color, random_size))

    # make shape


def initShapes(sList):
    sList.clear()
    patterncolor = Color(randint(0, 255), randint(0, 255), randint(0, 255))
    x = shape_w * (randint(0, round(screen_w / shape_w)) - 1)
    y = shape_h * (randint(0, round(screen_h / shape_h)) - 1)
    sList.append(Pattern(x, y, patterncolor))


while True:
  #  screen.fill((255, 255, 255))
   # pygame.display.update()

    pygame.time.delay(2000)
    print('yes')
    initBackground(rectangles)
    for rectangle in rectangles:
        rectangle.draw()
    initShapes(shapes)
    for shape in shapes:
        shape.draw()
    pygame.display.update()

    for event in pygame.event.get():
       # if event.type == QUIT:
        #  exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                pygame.image.save(screen, str(
                    pygame.time.get_ticks()) + ".png")

        if event.type == pygame.MOUSEBUTTONUP:
            print(pygame.mouse.get_pos())
          #  screen.lock()
           # screen.unlock()
