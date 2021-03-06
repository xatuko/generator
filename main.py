import generator as gen
import random as rnd
import math as m
import conversions as cnv


h = m.pi / 180
theta = gen.theta_init(h)
phi = gen.phi_init(h)

ellipsoids = [[[80, 50, 50, 0, 0, 0], [50, 80, 50, 0, 0, 0], [50, 50, 80, 0, 60, 0]], #спб
              [[80, 50, 50, 0, 0, 30], [90, 80, 50, 45, 0, 0], [60, 50, 80, 0, 60, 0], [55, 30, 70, 0, 0, 0]], #калуга
              [[45, 60, 50, 45, 0, 30], [70, 90, 50, 45, 0, 0], [60, 50, 80, 0, 0, 90], [55, 80, 70, 0, 10, 0], [65, 75, 45, 30, 30, 0]], #тверь
              [[90, 30, 30, 30, 0, 0], [45, 20, 60, 0, 60, 0], [55, 40, 70, 0, 30, 0], [40, 80, 60, 0, 0, 0]], #сочи
              [[60, 50, 30, 0, 45, 0], [45, 70, 60, 45, 60, 0], [80, 20, 20, 0, 45, 0], [30, 55, 45, 0, 0, 30]], #великий новгород
              [[45, 75, 60, 30, 0, 0], [75, 40, 55, 0, 60, 30], [25, 60, 35, 0, 45, 0], [75, 40, 70, 0, 0, 30], [55, 80, 70, 0, 90, 0]], #ростов на дону
              [[25, 70, 40, 0, 30, 0], [65, 40, 80, 10, 0, 0], [50, 50, 80, 0, 60, 0]], #волгоград
              [[35, 80, 40, 0, 45, 0], [70, 50, 40, 60, 0, 30], [30, 50, 45, 0, 0, 60], [80, 50, 60, 30, 0, 30], [75, 55, 60, 0, 90, 0]], #воронеж
              [[40, 70, 50, 45, 0, 0], [35, 50, 80, 0, 60, 45], [70, 30, 45, 0, 45, 0], [75, 55, 35, 0, 0, 30]], #тула
              [[45, 75, 50, 20, 0, 30], [55, 70, 80, 30, 45, 30], [40, 60, 50, 45, 0, 0], [70, 20, 60, 0, 0, 30]] #брянск
              ]

for k in range(len(ellipsoids)):
    for num in range(50):
        ell = gen.add_error(ellipsoids[k])
        x, y, z = gen.generator(ell)
        a, e, rng = cnv.convert2aer(x,y,z)

        th = open("training/theta_" + str(k) + "_" + str(num) + ".txt", 'w')
        ph = open("training/phi_" + str(k) + "_" + str(num) + ".txt", 'w')
        ra = open("training/range_" + str(k) + "_" + str(num) + ".txt", 'w')
        for i in range(len(rng)):
            for j in range(len(rng[i])):
                th.write(str(theta[i][j]) + ':')
                ph.write(str(phi[i][j]) + ':')
                ra.write(str(rng[i][j]) + ':')
        th.close()
        ph.close()
        ra.close()

