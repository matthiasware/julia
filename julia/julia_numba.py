import numpy as np
from numba import njit

@njit
def calc_z_numba(zs, iter_map, cs, z_max, iter_max):
    for i in range(len(zs)):
        iter_map[i] = calc_single_z(zs[i], cs[i], iter_max)


@njit
def calc_single_z(z, c, iter_max):
    n = 0
    while n < iter_max and (z.real * z.real +z.imag * z.imag) < 4:  
        z = z*z + c
        n += 1
    return n


def calc_julia_set(x_min, x_max, y_min, y_max, z_max, c, width, height, iter_max):
    # initialize zs
    x_step = (x_max - x_min) / width
    y_step = (y_max - y_min) / height

    x_cords = [x_min + (i*x_step) for i in range(0, width, 1)]
    y_cords = [y_min + (i*y_step) for i in range(0, height, 1)]

    zs = []
    for x in x_cords:
        for y in y_cords:
            zs.append(complex(x, y))
    zs = np.array(zs)
    cs = np.zeros_like(zs, dtype=np.complex128) + c
    iter_map = np.zeros_like(zs, dtype=np.int32)
    # calculate iterations
    calc_z_numba(zs, iter_map, cs, z_max, iter_max)
    return iter_map
