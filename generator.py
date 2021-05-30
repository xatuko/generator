import math as m


def generator(ell_params: list, rotate_angles: list) -> list:
    h = m.pi / 180
    theta = [-m.pi / 2]
    while theta[len(theta)-1] < m.pi / 2:
        theta.append(theta[len(theta)-1] + h / 2)
    return [theta]
