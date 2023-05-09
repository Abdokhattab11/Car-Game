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
Break_Flag =False
mouse_x, mouse_y = 0, 0
start_game = 0
credits_sc = 0

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

sounds[4].play(0)

def init_proj():
    glClearColor(0, 0, 0, 0)
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
    if credits_sc == 1:
        # BACk Button
        if mouse_x >= 260 and mouse_x <= 460 and mouse_y >= 700-100 and mouse_y <= 700-20:
            draw_texture(260,20,460,100,BACK_RED)
        else:
            draw_texture(260,20,460,100,BACK_YELLOW)
        draw_texture(0,0,WINDOW_WIDTH,WINDOW_HEIGHT,CREDIT_SCREEN)
    elif start_game == 0:
        glLoadIdentity()
        # ON START Button
        if mouse_x >= 280 and mouse_x <= 520 and mouse_y >= 280 and mouse_y <= 360:
            draw_texture(280,340,520,420,START_RED)
        else:
            draw_texture(280,340,520,420,START_YELLOW)
        # On CREDITS button
        if mouse_x >= 280 and mouse_x <= 520 and mouse_y >= 380 and mouse_y <= 460:
            draw_texture(280,240,520,320,CREDIT_RED)
        else:
            draw_texture(280,240,520,320,CREDIT_YELLOW)

        # On RED button
        if mouse_x >= 280 and mouse_x <= 520 and mouse_y >= 480 and mouse_y <= 560:
            draw_texture(280,140,520,220,EXIT_RED)
        else:
            draw_texture(280,140,520,220,EXIT_YELLOW)
        draw_texture(0,0,WINDOW_WIDTH,WINDOW_HEIGHT,START_SCREEN)
        
    elif start_game == 1:
        if test_car_walls(carModel, maze1):
            carModel.collosion = True
            sounds[0].set_volume(0.5)
            sounds[0].play(0)
            sounds[5].stop()
            sounds[6].stop()
        if test_car_bomb(carModel, bombs1):
            carModel.health -= 50
            carModel.sound("Sound/bomb.wav",1,0)
        if test_car_coin(carModel, coins1):
            carModel.coins += 1
            sounds[1].play(0)
        if test_car_health(carModel,health1):
            carModel.health = carModel.health + 20 if carModel.health + 20 < 100 else 100
            sounds[2].set_volume(0.5)
            sounds[2].play(0)
        if carModel.health < 0:
            os._exit(0)

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

def draw_texture(left,bottom, right,top,tex_iden):
    glBindTexture(GL_TEXTURE_2D, tex_iden)
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    glTexCoord(0,0)
    glVertex2d(left,bottom)
    glTexCoord(1,0)
    glVertex2d(right,bottom)
    glTexCoord(1,1)
    glVertex2d(right,top)
    glTexCoord(0,1)
    glVertex2d(left,top)
    glEnd()
    glBindTexture(GL_TEXTURE_2D, -1)

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

def mousePass(x,y):
    global mouse_x,mouse_y
    mouse_x = x
    mouse_y = y

def mouse(state,key,x,y):
    global start_game, credits_sc
    if x >= 280 and x <= 520 and y >= 280 and y <= 360 and key == GLUT_LEFT_BUTTON  and start_game == 0:
        start_game = 1
    if x >= 280 and x <= 520 and y >= 380 and y <= 460 and key == GLUT_LEFT_BUTTON  and start_game == 0 and credits_sc == 0:
        credits_sc = 1
    if mouse_x >= 280 and mouse_x <= 520 and mouse_y >= 580 and mouse_y <= 560 and start_game == 0:
        os._exit(0) 
    if x >= 260 and x <= 460 and y >= 600 and y <= 680 and key ==GLUT_LEFT_BUTTON and credits_sc == 1:
        credits_sc = 0




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
    glutPassiveMotionFunc(mousePass)
    glutMouseFunc(mouse)
    init_proj()
    glutMainLoop()
