import pgzrun
from random import randint

TITLE = 'Flappy Ball'
WIDTH = 800
HEIGHT = 600

r = randint(0,255)
g = randint(0,255)
b = randint(0,255)

clr = (r,g,b)

GRAVCONST= 2000.0

class ball:
    def __init__(self, pos_x, pos_y):
        self.x=pos_x
        self.y=pos_y
        self.velo_x=200
        self.velo_y=0
        self.rad=40
    def draw(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos, self.rad, clr)

ball_ = ball(50,100)
def draw():
    screen.clear()
    ball_.draw()

def update(dt):
    uy = ball_.velo_y
    ball_.velo_y += GRAVCONST * dt
    ball_.y += (uy + ball_.velo_y)*0.5*dt
    if ball_.y > HEIGHT-ball_.rad:
        ball_.y = HEIGHT- ball_.rad
        ball_.velo_y = - ball_.velo_y *0.9
    ball_.x += ball_.velo_x * dt
    if ball_.x > WIDTH - ball_.rad or ball_.x < ball_.rad:
        ball_.velo_x = -ball_.velo_x
        


def on_key_down(key):
    if key == keys.SPACE:
        ball_.velo_y = -300

pgzrun.go()     