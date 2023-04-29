from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from maze import *
from car import *

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
PERIOD = 10


def init_proj():
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glOrtho(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, 0, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# iam youssef elfeky
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_map()
    glutSwapBuffers()


def Timer(v):
    display()
    glutTimerFunc(PERIOD, Timer, 1)


def keyboardup(key, x, y):
    return


def keyboard(key, x, y):
    return


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
