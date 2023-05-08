import os
try:
    del os.environ['DISPLAY']
except:
    pass
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from maze import *
from car import *
from collosion import *
from Healthbar import *
from texture import *
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
PERIOD = 10

carModel = car()

def init_proj():
    glClearColor(0.2, 0.2, 0.2, 0)
    glMatrixMode(GL_PROJECTION)
    glOrtho(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, 0, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    load_texture()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    if test_car_walls(carModel, maze1):
        carModel.collosion = True
    if test_car_bomb(carModel, bombs1):
        carModel.health = 0
    if test_car_coin(carModel, coins1):
        carModel.coins += 1
    if test_car_health(carModel,health1):
        carModel.health = carModel.health + 20 if carModel.health + 20 < 100 else 100
    #if carModel.health < 0:
    #    os._exit(0)

    draw_map()
    draw_coins()
    draw_healthkit()
    
    glPushMatrix()
    glTranslate(-20,5,0)
    draw_health(carModel.health)
    glPopMatrix()

    glPushMatrix()
    s = "Coins : " + str(carModel.coins)
    print_text(s,20,WINDOW_HEIGHT - 40)
    glPopMatrix()

    glPushMatrix()
    carModel.animation()
    carModel.draw()
    glPopMatrix()
    glutSwapBuffers()


def Timer(v):
    display()
    glutTimerFunc(PERIOD, Timer, 1)


def print_text(s, x, y):
    glLineWidth(2)
    glColor3f(1, 1, 0)
    glTranslate(x, y, 0)
    glScale(0.1, 0.1, 1)
    s = s.encode()
    for char in s:
        glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, char)


def keyboard(key, x, y):
    global carModel
    if key == b"w":
        carModel.speed = 1.5   # <ws----------------------- This is the edit of speed
        carModel.dir = 1
    if key == b"s":
        carModel.speed = -1.5
        carModel.dir = -1
    if key == b"d":
        carModel.rot = -1.5  # to make it smooths
    if key == b"a":
        carModel.rot = 1.5  # to make it smooth
    if key == b" ":
        carModel.currSpeed = 0
        carModel.speed = 0


def keyboardup(key, x, y):
    global carModel
    if key == b"w" or key == b"s":
        carModel.speed = 0
        carModel.dir = 0
    if key == b"d" or key == b"a":
        carModel.rot = 0


if __name__ == "__main__":
    glutInit()
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b"Need For Speed")
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA|GLUT_DEPTH)
    glutDisplayFunc(display)
    glutTimerFunc(PERIOD, Timer, 1)
    glutKeyboardFunc(keyboard)
    glutKeyboardUpFunc(keyboardup)
    init_proj()
    glutMainLoop()
