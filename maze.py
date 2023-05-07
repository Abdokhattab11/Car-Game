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
    def get_vertices(self):
        return [[self.x1,self.y1],[self.x2,self.y2]]


class box:
    def __init__(self, left, bottom, right, top):
        self.left = left
        self.bottom = bottom
        self.right = right
        self.top = top
        self.collected = False

    def draw(self):
        if self.collected == False:
            glBegin(GL_POLYGON)
            glVertex(self.left, self.bottom, 0)
            glVertex(self.right, self.bottom, 0)
            glVertex(self.right, self.top, 0)
            glVertex(self.left, self.top, 0)
            glEnd()

    def get_vertices(self):
        vertices = [
            [self.left, self.top],
            [self.left, self.bottom],
            [self.right, self.bottom],
            [self.right, self.top],
        ]
        return vertices


maze1 = [line(0, 100, 300, 100), line(
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


bombs1 =[]
coins1 = [box(400,40,420,60),box(850,140,870,160),box(50,140,70,160),box(50,540,70,560),box(50,630,70,650),
          box(225,440,245,460),box(375,440,395,460),box(750,440,770,460),box(525,40,545,60),box(675,540,695,560),
          box(1125,140,1145,160),box(1125,440,1145,460),box(850,340,870,360),box(975,640,995,660),box(500,240,520,260)]


def draw_line(line: line):
    glColor3f(1, 0, 0)
    glLineWidth(4)
    glBegin(GL_LINES)
    glVertex(line.x1, line.y1, 0)
    glVertex(line.x2, line.y2, 0)
    glEnd()


def draw_map():
    for i in range(len(maze1)):
        draw_line(maze1[i])

def draw_coins():
    glColor3f(1, 1, 0)
    for i in coins1:
        i.draw()

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
