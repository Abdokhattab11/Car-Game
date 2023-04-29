from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import pygame


class car:
    def __init__(self):
        # Coordinates
        self.left = 20
        self.bottom = 20
        self.right = 90
        self.top = 60
        # Car State
        self.health = 0
        self.light = False
        # Car Pyhsics
        self.rot = 0  # is am rotating or not -->> can be 1 or -1
        self.rotAngle = 0  # what value of rotation
        self.direction = 0  # 1 if 'w', -1 if 's, 0 else
        self.currSpeed = 0  # 1 if 'w' or 's' else 0
        self.speed = 0     # to be increment
        self.forwardAcc = 0.1
        self.backwardAcc = 0.1

    def draw(self):
        glColor3f(1, 1, 1)
        glBegin(GL_POLYGON)
        glVertex(self.left, self.bottom, 0)
        glVertex(self.right, self.bottom, 0)
        glVertex(self.right, self.top, 0)
        glVertex(self.left, self.top, 0)
        glEnd()

    def center(self):
        return [(self.left + self.right)/2, (self.top + self.bottom)/2]

    def animation(self):
        return

    def load_texture(self):
        return

    def sound(self):
        return
