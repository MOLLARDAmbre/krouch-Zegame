import pygame
import random
from krouch import Krouch
from threading import Thread
import time

class UI():
    def __init__(self, krouch_asset, insane_krouch_asset):
        pygame.font.init()
        self.krouch_asset = pygame.image.load(krouch_asset)
        self.krouch_asset = pygame.transform.scale(self.krouch_asset, (100, 100))
        self.reversed_asset = pygame.image.load(insane_krouch_asset)
        self.reversed_asset = pygame.transform.scale(self.reversed_asset, (100, 100))
        self.reversed_asset = pygame.transform.rotate(self.reversed_asset, 180)
        self.font = pygame.font.SysFont('comicsansms', 24)
        self.display = pygame.display.set_mode((1920, 1080))
        self.krouch_list = []
        self.points = 0
        self.init_krouchs()
        self.fill_thread = Thread(target=self.add_krouch, args=[])
        self.fill_thread.daemon = True
        self.fill_thread.start()

    def add_krouch(self):
        while True:
            self.create_and_add()
            time.sleep(0.01 * random.randint(10, 100))

    def create_and_add(self):
        d = random.choice([1, 1, 1, -1])
        if d == 1:
            self.krouch_list.append(Krouch([random.choice([455, 755, 1055, 1355]), 1080 - random.randint(600, 1000)], random.randint(1, 5)))
        else:
            self.krouch_list.append(Krouch([random.choice([455, 755, 1055, 1355]), random.randint(600, 1000)], -1 * random.randint(1, 5)))

    def init_krouchs(self):
        for i in range(random.randint(4, 12)):
            self.create_and_add()

    def update(self):
        for krouch in self.krouch_list:
            krouch.update()
        self.clean()

    def draw(self):
        self.display.fill((0, 0, 0))
        im = self.font.render(str(self.points), True, (255, 255, 255))
        self.display.blit(im, (20, 20))
        for krouch in self.krouch_list:
            if krouch.speed >= 1:
                self.display.blit(self.krouch_asset, (krouch.pos[0], krouch.pos[1]))
            else:
                self.display.blit(self.reversed_asset, (krouch.pos[0], krouch.pos[1]))
        for i in range(4):
            pygame.draw.circle(self.display, (255, 255, 255), (500 + 300 * i, 500), 75, width=10)

    def clean(self):
        l = []
        for krouch_id in range(len(self.krouch_list)):
            krouch = self.krouch_list[krouch_id]
            if not krouch.dispose:
                l.append(krouch)
        self.krouch_list = l

    def key(self, key):
        if key == 'q':
            x = 455
        if key == 'w':
            x = 755
        if key == 'e':
            x = 1055
        if key == 'r':
            x = 1355
        for krouch in self.krouch_list:
            if krouch.pos[0] == x and krouch.pos[1] < 500 and krouch.pos[1] > 350:
                self.points += krouch.hit()

