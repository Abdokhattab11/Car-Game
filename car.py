from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import pygame


class car:
    def __init__(self):
        # Coordinates
        self.left = 0
        self.bottom = 0
        self.right = 0
        self.top = 0
        # Car State
        self.health = 0
        self.light = False
        # Car Pyhsics
        self.rotAngle = 0
        self.direction = 0
        self.currSpeed = 0
        self.speed = 0
        self.forwardAcc = 0
        self.backwardAcc = 0

    def draw(self):
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
