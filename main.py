import math as m
import random as rnd
import conversions as conv
import generator as gen


th = open("theta.txt", 'w')
ph = open("phi.txt", 'w')
ra = open("range.txt", 'w')

xfile = open("x.txt", 'w')
yfile = open("y.txt", 'w')
zfile = open("z.txt", 'w')

h = m.pi / 180

theta = gen.theta_init(h)
phi = gen.phi_init(h)

rng1 = gen.mrange_array(3,1,1)
rng2 = gen.mrange_array(1,3,1)

x1,y1,z1 = conv.convert2enu(phi, theta, rng1)
x2,y2,z2 = conv.convert2enu(phi, theta, rng2)

x = gen.sumatr(x1,x2)
y = gen.sumatr(y1,y2)
z = gen.sumatr(z1,z2)


p, t, rng = conv.convert2aer(x,y,z)

for i in range(361):
    for j in range(361):
        ra.write(str(rng[i][j])+':')
        th.write(str(theta[i][j]) + ':')
        ph.write(str(phi[i][j]) + ':')        
        xfile.write("" + str(x[i][j]) + ':')
        yfile.write("" + str(y[i][j]) + ':')
        zfile.write("" + str(z[i][j]) + ':')
        #if j == 361:    
            #xfile.write("" + str(x[i][j]) + '\n')
            #yfile.write("" + str(y[i][j]) + '\n')
            #zfile.write("" + str(z[i][j]) + '\n')
            #continue

xfile.close()
yfile.close()
zfile.close()

th.close()
ph.close()
ra.close()

        


