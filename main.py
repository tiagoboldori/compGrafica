import glfw
from OpenGL.GL import *
import numpy as np

if not glfw.init():
    raise Exception("glfw can not be initialized!")


width = 800
height = 600

window = glfw.create_window(width, height, "My OpenGL window", None, None)

if not window:
    raise Exception("glfw window can not be created!")

glfw.make_context_current(window)

glClearColor(0.2, 0.3, 0.3, 1.0)

while not glfw.window_should_close(window):
    glfw.poll_events()

    glClear(GL_COLOR_BUFFER_BIT)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glTranslatef(0.4, 0.4, 0.0)
    glRotatef(45, 0, 0, 1)
    glScalef(1.5, 0.5, 1.0)

    #Vermelho
    glColor3f(1.0, 0.0, 0.0)

    glPointSize(7) 


    glBegin(GL_POINTS)
    glVertex2f(0.0, 0.5) 
    glEnd()


    #Verde
    glColor3f(0.0, 1.0, 0.0)

    glLineWidth(3)

    glBegin(GL_LINES)
    glVertex2f(-0.5, 0.0) 
    glVertex2f(0.5, 0.0)  
    glEnd()


    
    
    #Azul
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.0, -0.1)


    

    glEnd()

    



    glfw.swap_buffers(window)

    

glfw.terminate()

