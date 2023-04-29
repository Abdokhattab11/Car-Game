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
        self.right = 80
        self.top = 50
        # Car State
        self.health = 0
        self.light = False
        # Car Pyhsics
        self.rot = 0  # is am rotating or not -->> can be 1 or -1
        self.rotAngle = 0  # what value of rotation
        self.currSpeed = 0  # 1 if 'w' or 's' else 0
        self.speed = 0     # to be increment
        self.forwardAcc = 0.1
        self.backwardAcc = -0.1

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
        # First of all we need to adjust rotation
        # To make car rotate around it self we need to do :
        # 1- Translate to Origin
        # 2- Rotate around z-Axis
        # 3- Translate Back
        glLoadIdentity()
        cen = self.center()
        glTranslate(cen[0], cen[1], 0)
        glRotate(self.rotAngle, 0, 0, 1)
        glTranslate(-cen[0], -cen[1], 0)
        #####################################
        # Now we need to adjust the Vertices
        theta = self.rotAngle*(pi/180)
        self.left = self.left + cos(theta)*self.currSpeed
        self.right = self.right + cos(theta)*self.currSpeed
        self.top = self.top + sin(theta)*self.currSpeed
        self.bottom = self.bottom + sin(theta)*self.currSpeed

        if abs(self.currSpeed - self.speed) <= 0.01:  # to avoid floating prection
            self.currSpeed = self.speed
        elif self.currSpeed < self.speed:
            self.currSpeed += self.forwardAcc
        elif self.currSpeed > self.speed:
            self.currSpeed += self.backwardAcc

        self.rotAngle += self.rot*self.currSpeed

    def load_texture(self):
        return

    def sound(self):
        return
