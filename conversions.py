import math as m


def aer2enu(a: float, e: float, r: float) -> list:
    z = m.sin(e) * r
    rs = m.cos(e) * r
    x = m.cos(a) * rs
    y = m.sin(a) * rs
    return [x, y, z]


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
