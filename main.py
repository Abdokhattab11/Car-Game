from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from maze import *
from car import *
from collosion import *
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
PERIOD = 10

carModel = car()
Box = box(350, 100, 400, 150)
collosion = Collosion()

def init_proj():
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glOrtho(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, 0, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    if collosion.line_polygon_intersect(lst_of_lines, carModel):
        carModel.collosion = True
    #if collosionModeltest_car_box(carModel, Box):
     #   os._exit(0)
    glPushMatrix()
    draw_map()
    s = "Health : " + str(carModel.health)
    print_text(s, 20, WINDOW_HEIGHT-20)

    glPopMatrix()

    glPushMatrix()
    Box.draw()
    glPopMatrix()

    glPushMatrix()
    carModel.animation()
    carModel.draw()
    glPopMatrix()
    glutSwapBuffers()
    print(carModel.currSpeed, carModel.speed)


def Timer(v):
    display()
    glutTimerFunc(PERIOD, Timer, 1)


def print_text(s, x, y):
    glLineWidth(2)
    glColor3f(1, 1, 0)
    glTranslate(x, y, 0)
    glScale(0.15, 0.15, 1)
    s = s.encode()
    for char in s:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, char)


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
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutDisplayFunc(display)
    glutTimerFunc(PERIOD, Timer, 1)
    glutKeyboardFunc(keyboard)
    glutKeyboardUpFunc(keyboardup)
    init_proj()
    glutMainLoop()
