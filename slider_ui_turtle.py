import ui
import scene
from turtle import *
import math
#from canvas import set_size, draw_rect, draw_line
from time import sleep
x = 0
x_max = 600
def s_action(sender):
    x = x_max*sender.value - 300
    sender.name = 'x='+str(int(x))
    moveTo(x)
    
s = ui.Slider()
s.action = s_action
s.width = 200
#self.ty.frame = (0, 0, w, h*0.25)
s.height = 100
#s.position = 200,200
s.name = 'x='+str(int(x))
s.present('sheet')
fd(-200)
rt(100)

speed(0)
#screen = Screen()
#s.frame = (0, 0, s.width, 200)
def draw():
	setpos(-x,-x)
	fd(sin(x))
	rt(-7-x)
	lt(-39-x)
def moveTo(x):
     setpos(x, x)
     fd(x)
     rt(x)
     dot(sin(x)*19)
     setpos(-x, x)
     fd(-x)
     rt(-x)
     dot(sin(x)*19)
     for x in range(int(x)):
     	draw()
S = getscreen()
S.touch_enabled = True
S.touch_began = x
#screen.onclick()
#scene.listen()

#import turtle, editor
#editor.open_file(turtle.__file__)