from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
def draw_white_bar():
    glColor3f(1, 1, 1)
    glPushMatrix()
    glBegin(GL_POLYGON)
    glVertex(28, WINDOW_HEIGHT-30, 0)
    glVertex(182, WINDOW_HEIGHT-30, 0)
    glVertex(182, WINDOW_HEIGHT-10, 0)
    glVertex(28, WINDOW_HEIGHT-10, 0)
    glEnd()
    glPopMatrix()

def draw_health_bar(health):
    glColor3f(1 - health/100, health/100, 0)
    Green_Section = (health * (150/100)) + 30
    glPushMatrix()
    glBegin(GL_POLYGON)
    glVertex(30, WINDOW_HEIGHT - 28, 0)
    glVertex(Green_Section, WINDOW_HEIGHT - 28, 0)
    glVertex(Green_Section, WINDOW_HEIGHT - 12, 0)
    glVertex(30, WINDOW_HEIGHT - 12, 0)
    glEnd()
    glPopMatrix()

def draw_health(health):
    draw_health_bar(health)
    draw_white_bar()
