import math as m
import conversions as cnv


def sumatr(arr1: list, arr2: list) -> list:
    if len(arr1) != len(arr2):
        return [0]
    res = [[0 for i in range(len(arr1))] for j in range(len(arr2))]
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            res[i][j] = arr1[i][j] + arr2[i][j]
    return res


def theta_init(h: float) -> list:
    beg = -m.pi / 2
    theta = []
    while beg <= m.pi / 2:
        t = []
        for i in range(361):
            t.append(beg)
        theta.append(t)
        beg += h / 2
    return theta


def phi_init(h: float) -> list:
    beg = -m.pi
    phi = []
    p = []
    while beg <= m.pi:
        p.append(beg)
        beg += h
    for i in range(361):
        phi.append(p)
    return phi


def mrange(a: int, b: int, c: int, t: float, p: float) -> float:
    return (a * b * c) / m.sqrt((b * c * m.cos(t) * m.cos(p)) ** 2 +
                                (a * c * m.cos(t) * m.sin(p)) ** 2 +
                                (b * a * m.sin(t)) ** 2)


def mrange_array(a: int, b: int, c: int) -> list:
    h = m.pi / 180
    theta = theta_init(h)
    phi = phi_init(h)
    rng = theta
    for i in range(361):
        for j in range(361):
            rng[i][j] = mrange(a,b,c,theta[i][j],phi[i][j])
    return rng


def generator(ell_params: list) -> list:
    if len(ell_params) == 0:
        return [0]
    h = m.pi / 180
    theta = theta_init(h)
    phi = phi_init(h)

    x = [[0 for j in range(361)] for i in range(361)]
    y = [[0 for j in range(361)] for i in range(361)]
    z = [[0 for j in range(361)] for i in range(361)]

    for param in ell_params:
        a,b,c,rx,ry,rz = param
        rng = mrange_array(a,b,c)
        xb,yb,zb = cnv.convert2enu(phi,theta,rng)
        if rx != 0:
            for i in range(361):
                for j in range(361):
                    xb[i][j],yb[i][j],zb[i][j] = cnv.rotate_by_x(xb[i][j],yb[i][j],zb[i][j], m.pi/180*rx)
        if ry != 0:
            for i in range(361):
                for j in range(361):
                    xb[i][j],yb[i][j],zb[i][j] = cnv.rotate_by_x(xb[i][j],yb[i][j],zb[i][j], m.pi/180*ry)
        if rz != 0:
            for i in range(361):
                for j in range(361):
                    xb[i][j],yb[i][j],zb[i][j] = cnv.rotate_by_x(xb[i][j],yb[i][j],zb[i][j], m.pi/180*rz)
        x = sumatr(x,xb)
        y = sumatr(y,yb)
        z = sumatr(z,zb)
    
    return x,y,z

        







