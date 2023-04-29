from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from maze import *
from car import *

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
PERIOD = 10

carModel = car()


def init_proj():
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glOrtho(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, 0, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glPushMatrix()
    draw_map()
    glPopMatrix()
    glPushMatrix()
    carModel.draw()
    glPopMatrix()
    glutSwapBuffers()


def Timer(v):
    display()
    glutTimerFunc(PERIOD, Timer, 1)


def keyboard(key, x, y):
    global carModel
    if key == b"w":
        carModel.direction = 1
        carModel.speed = 1
    if key == b"s":
        carModel.direction = -1
        carModel.speed = 1
    if key == b"d":
        carModel.rot = 1
    if key == b"a":
        carModel.rot = -1


def keyboardup(key, x, y):
    global carModel
    if key == b"w" or key == b"s":
        carModel.direction = 0
        carModel.speed = 0
    if key == b"d" or key == b"a":
        carModel.rot = 0


if __name__ == "__main__":
    glutInit()
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b"Need For Speed")
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutDisplayFunc(display)
    glutTimerFunc(PERIOD, Timer, 1)
    init_proj()
    glutMainLoop()
