import os
import random
import sys
from os.path import exists

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

try:
    os.stat('gen')
except:
    os.mkdir('gen')

if (not exists('gen/Red.npy')) or (not exists('gen/Green.npy')):
    np.save('gen/Red.npy', np.array([1, 50]))
    np.save('gen/Green.npy', np.array([1, 50, 30]))

# сетка 2 на 2
fig, axs = plt.subplots(2, 2)
fig.set_size_inches(8, 8)
axs = np.array(axs).reshape(4)
for ax in axs:
    # ax.set_xlim(-100, 100)
    # ax.set_ylim(-100, 100)
    ax.set_aspect('equal')
layers = [[], [], [], []]
ends = []
# время и максимальное время
t = 0
max_t = 200
dt = 0.5


# выходилка из приложения
def end():
    # лучшая популяция красных
    rr0 = list(filter(lambda item: isinstance(item, Red), layers[0]))
    gg0 = list(filter(lambda item: isinstance(item, Green), layers[0]))
    score = len(rr0) - len(gg0)
    rr = list(filter(lambda item: isinstance(item, Red), layers[1]))
    gg = list(filter(lambda item: isinstance(item, Green), layers[1]))
    if len(rr) - len(gg) > score:
        np.save('gen/Red.npy', np.array(rr0[0].save()))
    else:
        np.save('gen/Red.npy', np.array(rr[0].save()))

    # лучшая популяция зелёных
    rr0 = list(filter(lambda item: isinstance(item, Red), layers[2]))
    gg0 = list(filter(lambda item: isinstance(item, Green), layers[2]))
    score = len(rr0) - len(gg0)
    rr = list(filter(lambda item: isinstance(item, Red), layers[3]))
    gg = list(filter(lambda item: isinstance(item, Green), layers[3]))
    if len(rr) - len(gg) < score:
        np.save('gen/Green.npy', np.array(gg0[0].save()))
    else:
        np.save('gen/Green.npy', np.array(gg[0].save()))

    print("Новые параметры:")
    print(np.load('gen/Red.npy'), ': скорость / частота деления')
    print(np.load('gen/Green.npy'), ': скорость / частота деления / безопасное расстояние')

    sys.exit()


class Entity:
    def __init__(self, i, x, y, speed, energy, divtime):
        self.speed = speed
        self.energy = energy
        # время между делениями
        self.divtime = divtime
        self.time = 0
        self.x = x
        self.y = y
        self.i = i
        layers[i].append(self)

    def div(self):
        self.energy /= 2
        speed = self.speed
        energy = self.energy
        divtime = self.divtime
        x = self.x + random.uniform(-5, 5)
        y = self.y + random.uniform(-5, 5)
        if isinstance(self, Red):
            e = Red(self.i, x, y, speed, energy, divtime)
        if isinstance(self, Green):
            e = Green(self.i, x, y, speed, energy, divtime)
        layers[self.i].append(e)


class Red(Entity):
    def __init__(self, i, x, y, speed, energy, divtime):
        super().__init__(i, x, y, speed, energy, divtime)

    def div(self):
        super().div()

    def load(self):
        self.speed, self.divtime = np.load('gen/Red.npy')

    def save(self):
        return [self.speed, self.divtime]

    def step(self):
        self.time += dt
        if self.time >= self.divtime and self.energy > 200:
            self.energy -= 200
            self.time = 0
            self.div()
        if self.energy <= 0:
            layers[self.i].remove(self)
            # fig.canvas.resize_event()
        min_r, o = 2 ** 16, None
        for e in filter(lambda item: isinstance(item, Green), layers[self.i]):
            r = (self.x - e.x) ** 2 + (self.y - e.y) ** 2
            if r < min_r:
                min_r = r
                o = e
        if o != None:
            r = np.sqrt(min_r)
            if r < 5:
                layers[self.i].remove(o)
                # fig.canvas.resize_event()
                self.energy += 100 + o.energy / 2
            else:
                dir_x = (self.x - o.x) / r
                dir_y = (self.y - o.y) / r

                self.energy -= self.speed ** 2
                self.x -= dir_x * dt * self.speed
                self.y -= dir_y * dt * self.speed


class Green(Entity):
    def __init__(self, i, x, y, speed, energy, divtime):
        super().__init__(i, x, y, speed, energy, divtime)
        self.min_r = 30

    def div(self):
        super().div()

    def load(self):
        self.speed, self.divtime, self.min_r = np.load('gen/Green.npy')

    def save(self):
        return [self.speed, self.divtime, self.min_r]

    def step(self):
        self.time += dt
        if self.time >= self.divtime and self.energy > 100:
            self.energy -= 100
            self.time = 0
            self.div()
        if self.energy <= 0:
            layers[self.i].remove(self)
            # fig.canvas.resize_event()
        self.energy += 0.9
        min_r, o = 2 ** 16, None
        for e in filter(lambda item: isinstance(item, Red), layers[self.i]):
            r = (self.x - e.x) ** 2 + (self.y - e.y) ** 2
            if r < min_r:
                min_r = r
                o = e
        if o != None:
            r = np.sqrt(min_r)
            if 0 < r < self.min_r:
                dir_x = (self.x - o.x) / r
                dir_y = (self.y - o.y) / r

                self.energy -= self.speed ** 2
                self.x += dir_x * dt * self.speed
                self.y += dir_y * dt * self.speed


def update(t):
    t += dt
    if t > max_t:
        end()
    l = []
    for i in range(4):
        if not i in ends:
            r, g = 0, 0
            xs, ys = [], []
            for e in filter(lambda item: isinstance(item, Red), layers[i]):
                e.step()
                r += 1
                xs.append(e.x)
                ys.append(e.y)
            l.append(axs[i].scatter(xs, ys, lw=3, c="firebrick"))

            xs, ys = [], []
            for e in filter(lambda item: isinstance(item, Green), layers[i]):
                e.step()
                g += 1
                xs.append(e.x)
                ys.append(e.y)
            l.append(axs[i].scatter(xs, ys, lw=3, c="forestgreen"))
            if (g == 1):
                end()
            if (r == 1):
                end()

    return l


for I in range(4):
    for i in range(5):
        r = Red(I, random.randint(-10, 10), random.randint(-10, 10), 1, 1000, 20)
        r.load()

    for i in range(20):
        g = Green(I, random.randint(-10, 10), random.randint(-10, 10), 1, 1000, 20)
        g.load()
# end()
rr = random.randint(0, 1)
for e in filter(lambda item: isinstance(item, Red), layers[0]):
    if rr == 0:
        e.speed *= 1.1
    else:
        e.divtime *= 1.1

for e in filter(lambda item: isinstance(item, Red), layers[1]):
    if rr == 0:
        e.speed /= 1.1
    else:
        e.divtime /= 1.1
        if e.divtime < 20:
            e.divtime = 20

gg = random.randint(0, 2)
for e in filter(lambda item: isinstance(item, Green), layers[2]):
    if gg == 0:
        e.speed *= 1.1
    elif gg == 1:
        e.divtime *= 1.1
    else:
        e.min_r *= 1.1

for e in filter(lambda item: isinstance(item, Green), layers[3]):
    if gg == 0:
        e.speed /= 1.1
    elif gg == 1:
        e.divtime /= 1.1
        if e.divtime < 20:
            e.divtime = 20
    else:
        e.min_r /= 1.1

print("Старые параметры:")
print(np.load('gen/Red.npy'), ': скорость / частота деления')
print(np.load('gen/Green.npy'), ': скорость / частота деления / безопасное расстояние')
anim = FuncAnimation(fig, update, frames=300, interval=5, blit=True)
plt.show()
