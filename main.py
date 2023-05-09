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
First_Start_Flag = True
Go_Drive_Flag=False
Go_Back_Flag=False
Wait_Flag=False
Break_Flag =False
carModel = car()


pygame.init()
sounds=[pygame.mixer.Sound("Sound/crash.wav"),
        pygame.mixer.Sound("Sound/coin.wav"),
        pygame.mixer.Sound("Sound/revive.wav"),
        pygame.mixer.Sound("Sound/car_horn.wav"),
        pygame.mixer.Sound("Sound/starting_game.wav"),
        pygame.mixer.Sound("Sound/go_driving.wav"),
        pygame.mixer.Sound("Sound/car_reverse.wav"),
        pygame.mixer.Sound("Sound/car_break.wav"),
        pygame.mixer.Sound("Sound/song.wav")]


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
    global First_Start_Flag
    Wait_Flag=True
    
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    if test_car_walls(carModel, maze1):
        carModel.collosion = True
        sounds[0].set_volume(0.5)
        sounds[0].play(0)
        sounds[5].stop()
        sounds[6].stop()
    if test_car_bomb(carModel, bombs1):
        carModel.health = 0
        carModel.sound("Sound/bomb.wav",1,0)
    if test_car_coin(carModel, coins1):
        carModel.coins += 1
        sounds[1].play(0)
        
    if test_car_health(carModel,health1):
        carModel.health = carModel.health + 20 if carModel.health + 20 < 100 else 100
        sounds[2].set_volume(0.5)
        sounds[2].play(0)
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
    
    if First_Start_Flag is True:
        sounds[4].play(0)
        First_Start_Flag = False
    
        
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
    global carModel,Go_Drive_Flag,Go_Back_Flag,Break_Flag
    if key == b"w":
        carModel.speed = 1.5   # <ws----------------------- This is the edit of speed
        carModel.dir = 1
        if Go_Drive_Flag == False:
            sounds[5].set_volume(0.2)
            sounds[5].play(-1)
            Go_Drive_Flag = True
    if key == b"s":
        carModel.speed = -1.5
        carModel.dir = -1
        if Go_Back_Flag==False:
            sounds[6].set_volume(0.5)
            sounds[6].play(-1)
            Go_Back_Flag=True
    if key == b"d":
        carModel.rot = -1.5  # to make it smooths
    if key == b"a":
        carModel.rot = 1.5  # to make it smooth
    if key == b" ":
        if carModel.currSpeed==carModel.speed!=0 and Break_Flag==False:
            sounds[7].play(0)
            Break_Flag==True
        carModel.currSpeed = 0
        carModel.speed = 0
        sounds[6].stop()
        sounds[5].stop()
        
    if key == b"e":
        sounds[3].play(0)
    if key ==b'p':
        sounds[8].play(0)
    


def keyboardup(key, x, y):
    global carModel,Go_Drive_Flag,Go_Back_Flag,Break_Flag
    if key == b"w" or key == b"s":
        carModel.speed = 0
        carModel.dir = 0
        Go_Drive_Flag=False
        Go_Back_Flag=False
        sounds[5].stop()
        sounds[6].stop()
    if key == b"d" or key == b"a":
        carModel.rot = 0
    if key == b" ":
        Break_Flag=False
    if key ==b'o':
        sounds[8].stop()


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
