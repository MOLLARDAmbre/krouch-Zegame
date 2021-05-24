import pygame

class Krouch():
    def __init__(self, pos, speed):
        self.pos = pos
        self.speed = speed
        self.dispose = False

    def hit(self):
        self.dispose = True
        return self.speed

    def update(self):
        self.pos[1] += self.speed
        if self.pos[1] > 400 and self.speed > 0:
            self.dispose = True
        if self.pos[1] < 450 and self.speed < 0:
            self.dispose = True
