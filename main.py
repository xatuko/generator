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


ellipsoids = [[3,1,1,0,0,0],
              [1,1,3,0,0,0]]

x,y,z = gen.generator(ellipsoids)

for i in range(361):
    for j in range(361):      
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

        


