import math as m


def aer2enu(a: float, e: float, r: float) -> list:
    z = m.sin(e) * r
    rs = m.cos(e) * r
    x = m.cos(a) * rs
    y = m.sin(a) * rs
    return x, y, z


def enu2aer(x: float, y: float, z: float) -> list:
    r = m.sqrt(x**2 + y**2 + z**2)
    e = m.atan2(z,r)
    a = m.atan2(x,y) % 2*m.pi
    return [a, e, r]


def rotate_by_x(x: float, y: float, z: float, angle: float) -> list:
    m_y = y*m.cos(angle) - z*m.sin(angle)
    m_z = y*m.sin(angle) + z*m.cos(angle)
    m_x = x
    return [m_x, m_y, m_z]


def rotate_by_z(x: float, y: float, z: float, angle: float) -> list:
    m_x = x*m.cos(angle) - y*m.sin(angle)
    m_y = x*m.sin(angle) + y*m.cos(angle)
    m_z = z
    return [m_x, m_y, m_z]


def rotate_by_y(x: float, y: float, z: float, angle: float) -> list:
    m_x = x*m.cos(angle) + z*m.sin(angle)
    m_z = -x*m.sin(angle) + z*m.cos(angle)
    m_y = y
    return [m_x, m_y, m_z]


def arr_to_str(arr: list) -> str:
    res = ""
    for val in arr:
        res = res + str(val) + ' : '
    res = res[:len(res) - 3] + '\n'
    return res


def convert2aer(x: list, y: list, z: list) -> list:
    if len(x) != len(y) or len(y) != len(z) or len(x) != len(z):
        return [0]
    a = [[0 for j in range(361)] for i in range(361)]
    e = [[0 for j in range(361)] for i in range(361)]
    r = [[0 for j in range(361)] for i in range(361)]
    for i in range(361):
        for j in range(361):
            a[i][j], e[i][j], r[i][j] = enu2aer(x[i][j], y[i][j], z[i][j])
    return [a, e, r]


def convert2enu(a: list, e: list, r: list) -> list:
    if len(a) != len(e):
        return [0]
    x = [[0 for j in range(361)] for i in range(361)]
    y = [[0 for j in range(361)] for i in range(361)]
    z = [[0 for j in range(361)] for i in range(361)]
    for i in range(361):
        for j in range(361):
            x[i][j], y[i][j], z[i][j] = aer2enu(a[i][j], e[i][j], r[i][j])
    return x, y, z

