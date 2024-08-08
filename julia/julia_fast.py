import multiprocessing as mp
from numba import njit
from multiprocessing import shared_memory
import numpy as np

@njit
def calc_z(z, c, z_max, iter_max):
    n = 0
    while n < iter_max and (z.real * z.real +z.imag * z.imag) < 4:
        z = z*z + c
        n += 1
    return n

@njit
def inner_loop(c, idx_y, idx_x, y_min, x_min, y_step, x_step, z_max, iter_max):
    z_imag = y_min + (idx_y * y_step)
    z_real = x_min + (idx_x * x_step)
    z = complex(z_real, z_imag)
    n = calc_z(z, c, z_max, iter_max)
    return n

def calc_zs_worker(shm_name, pid, width, height, c, iter_max, z_max, x_min, x_max, y_min, y_max, offset):
    shm = shared_memory.SharedMemory(name=shm_name)
    iter_map = np.ndarray(width*height, dtype=np.int32, buffer=shm.buf)
    x_step = (x_max - x_min) / width
    y_step = (y_max - y_min) / height

    for idx_y in range(pid, height, offset):
        for idx_x in range(width):
            n = inner_loop(c, idx_y, idx_x, y_min, x_min, y_step, x_step, z_max, iter_max)
            iter_map[(idx_y * width) + idx_x] = n
    shm.close()

def calc_julia_set(x_min, x_max, y_min, y_max, z_max, c, width, height, iter_max, n_workers=None):
    if not n_workers:
        n_workers = mp.cpu_count()
    #iter_map = mp.Array("i", width*height, lock=False)

    iter_map_init = np.zeros(width*height, dtype=np.int32)
    shm = shared_memory.SharedMemory(create=True, size=iter_map_init.nbytes)
    iter_map = np.ndarray(iter_map_init.shape, dtype=iter_map_init.dtype, buffer=shm.buf)
    iter_map[:] = iter_map_init[:]

    ps = [mp.Process(target=calc_zs_worker,
                     args=(shm.name, pid, width, height,
                           c, iter_max, z_max,
                           x_min, x_max, y_min, y_max, n_workers)) for pid in range(n_workers)]

    for p in ps:
        p.start()
    for p in ps:
        p.join()
    # should be done like this, otherwise leak!
    # shm.close()
    # shm.unlink()
    return list(iter_map)


if __name__ == "__main__":
    from utils import plot

    x_min, x_max, y_min, y_max = -1.8, 1.8, -1.8, 1.8
    c_real, c_imag = -0.62772, -.42193
    c = complex(c_real, c_imag)
    width = 1000
    height = 1000
    iter_max = 300
    z_max = 2
    n_workers = 1

    iter_map = calc_julia_set(x_min, x_max, y_min, y_max, z_max, c, width, height, iter_max, n_workers)
    plot(iter_map, width, height, iter_max)
