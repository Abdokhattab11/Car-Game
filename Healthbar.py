from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
def draw_white_bar(center):
    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)
    glVertex(center[0]-60, center[1]-7, 0)
    glVertex(center[0]+60, center[1]-7, 0)
    glVertex(center[0]+60, center[1]+7, 0)
    glVertex(center[0]-60, center[1]+7, 0)
    glEnd()

def draw_health_bar(health, center):
    glColor3f(1 - health/100, health/100, 0)
    Green_Section = (health * (116/100))
    glBegin(GL_POLYGON)
    glVertex(center[0] - 58, center[1] - 5, 0)
    glVertex(center[0] - 58 + Green_Section, center[1] - 5, 0)
    glVertex(center[0] - 58 + Green_Section, center[1] + 5, 0)
    glVertex(center[0] - 58, center[1] + 5, 0)
    glEnd()

def draw_health(health, center):
    glPushMatrix()
    draw_health_bar(health, center)
    draw_white_bar(center)
    glPopMatrix()