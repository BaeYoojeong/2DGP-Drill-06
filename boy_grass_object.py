from pico2d import *
import random


# Game object class here


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)
    def update(self): pass

class Ball1:
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(30, 770), 599
        self.speed = random.randint(5, 15)
    def update(self):
        self.y -= self.speed
        if self.y <50:
            self.y=50

    def draw(self):
        self.image.clip_draw(0, 0, 21, 21, self.x, self.y)

class Ball2:
    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(30, 770), 599
        self.speed = random.randint(5, 20)
    def update(self):
        self.y -= self.speed
        if self.y <50:
            self.y=50

    def draw(self):
        self.image.clip_draw(0, 0, 41, 41, self.x, self.y)


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

def reset_world():
    global running
    global world

    running = True
    world = []

    grass = Grass()
    world.append(grass)

    team = [Boy() for i in range(11)]
    ball1 = [Ball1() for i in range(10)]
    ball2 = [Ball2() for i in range(10)]
    world += team
    world += ball2
    world += ball1


def update_world():
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


open_canvas()

reset_world()
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)






close_canvas()
