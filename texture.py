import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

texture_names = [0,1,2,3,4,5,6,7,8,9,10]
STAR = 0
CAR = 1
HEALTH = 2
EXIT_RED = 3
EXIT_YELLOW = 4
START_RED = 5
START_YELLOW = 6
START_SCREEN = 7

def load_texture():
    glEnable(GL_TEXTURE_2D)

    images = []

    images.append(pygame.image.load("texture/star.png"))
    images.append(pygame.image.load("texture/car.png"))
    images.append(pygame.image.load("texture/health.png"))
    images.append(pygame.image.load("texture/exit_red.png"))
    images.append(pygame.image.load("texture/exit_yellow.png"))
    images.append(pygame.image.load("texture/start_red.png"))
    images.append(pygame.image.load("texture/start_yellow.png"))
    images.append(pygame.image.load("texture/start_screen.png"))
    textures = [pygame.image.tostring(img,"RGBA", 1) for img in images]

    glGenTextures(len(images), texture_names)

    for i in range(len(images)):
        setup_texture(textures[i],
                      texture_names[i],
                      images[i].get_width(),
                      images[i].get_height())
        
def setup_texture(binary_img, texture_iden, width, height):
    glBindTexture(GL_TEXTURE_2D, texture_iden)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width,
                 height, 0, GL_RGBA, GL_UNSIGNED_BYTE, binary_img)
        