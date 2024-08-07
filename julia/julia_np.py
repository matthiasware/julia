if 'line_profiler' not in dir() and 'profile' not in dir():
    def profile(func):
        return func

from line_profiler import profile
import numpy as np

@profile
def calc_single_z(z, c, z_max, iter_max):
    n = 0
    while n < iter_max and abs(z) < z_max:
        z = z*z + c
        n += 1
    return n

@profile
def calc_julia_set(x_min, x_max, y_min, y_max, z_max, c, width, height, iter_max):
    x_step = (x_max - x_min) / width
    y_step = (y_max - y_min) / height

    iter_map = np.zeros((height, width), dtype=np.int32)

    for ix in range(width):
        x_cord = x_min + (ix*x_step)
        for iy in range(height):
            y_cord = y_min + (iy*y_step)
            z = complex(x_cord, y_cord)
            n_iter = calc_single_z(z, c, z_max, iter_max)
            iter_map[ix, iy] = n_iter
    return iter_map.flatten()