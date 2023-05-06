from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from maze import *
from car import *
from collision import *

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

cnt =1

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    draw_map()
    draw_rects()
    glPopMatrix()
    glPushMatrix()
    carModel.animation()
    carModel.draw()
    glPopMatrix()
    glutSwapBuffers()



def Timer(v):
    global cnt
    display()
    if detect_collision(carModel,lst_of_lines):
        carModel.currSpeed *= -1
        # print("collision ", cnt)
        # cnt = cnt + 1
    glutTimerFunc(PERIOD, Timer, 1)


def keyboard(key, x, y):
    global carModel
    if key == b"w": 
        carModel.speed = 1.5   # <----------------------- This is the edit of speed
    if key == b"s":
        carModel.speed = -1.5
    if key == b"d":
        carModel.rot = -1.5  # to make it smooth
    if key == b"a":
        carModel.rot = 1.5  # to make it smooth
    if key == b" ":
        carModel.currSpeed = 0
        carModel.speed = 0


def keyboardup(key, x, y):
    global carModel
    if key == b"w" or key == b"s":
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
    glutKeyboardFunc(keyboard)
    glutKeyboardUpFunc(keyboardup)
    init_proj()
    glutMainLoop()
