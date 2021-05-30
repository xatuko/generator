import math as m
import random as rnd
import conversions as conv
import generator as gen


def m_range(a: int, b: int, c: int, t: float, p: float) -> float:
    return (a * b * c) / m.sqrt((b * c * m.cos(t) * m.cos(p)) ** 2 +
                                (a * c * m.cos(t) * m.sin(p)) ** 2 +
                                (b * a * m.sin(t)) ** 2)

th = open("theta.txt", 'w')
ph = open("phi.txt", 'w')
ra = open("range.txt", 'w')

theta = []
phi = []
rng = []

h = m.pi / 180

s_theta = -m.pi / 2
while s_theta <= m.pi / 2:
    theta.append(s_theta)
    th.write(str(s_theta) + '\n')
    s_theta += h / 2

s_phi = -m.pi
while s_phi < m.pi:
    phi.append(s_phi)
    ph.write(str(s_phi) + '\n')
    s_phi += h

for t in theta:
    rr = []
    for p in phi:
        rr.append(m_range(3, 1, 1, t, p))
    rng.append(rr)
    ra.write(conv.arr_to_str(rr))

print(len(gen.generator([],[])[0]))