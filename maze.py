from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

LINE_WIDTH = 10


class line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.vertical = (x1 == x2)


lst_of_lines = [line(0, 100, 300, 100), line(
    150, 200, 150, 600), line(0, 600, 150, 600),
    line(300, 200, 300, 600), line(300, 200, 900, 200),
    line(450, 300, 900, 300), line(600, 400, 900, 400),
    line(600, 500, 1200, 500), line(1050, 500, 1050, 200),
    line(600, 500, 600, 600), line(600, 600, 1050, 600),
    line(900, 400, 900, 300), line(450, 700, 450, 300),
    line(900, 200, 900, 100), line(450, 100, 1050, 100),
    line(450, 0, 450, 100), line(0, 0, 1200, 0),
    line(1200, 0, 1200, 700), line(1200, 700, 0, 700),
    line(0, 700, 0, 0,)]


def draw_line(line: line):
    glColor3f(1, 0, 0)
    glLineWidth(4)
    glBegin(GL_LINES)
    glVertex(line.x1, line.y1, 0)
    glVertex(line.x2, line.y2, 0)
    glEnd()


def draw_map():
    for i in range(len(lst_of_lines)):
        draw_line(lst_of_lines[i])


def draw_grid():
    glLineWidth(1)
    glColor3f(1, 0, 0)
    glBegin(GL_LINES)
    for i in range(8):
        glVertex(-1500, i*100, 0)
        glVertex(1200, i*100, 0)
    for i in range(9):
        glVertex(i*150, -1500, 0)
        glVertex(i*150, 1500, 0)
    glEnd()
