import time
from julia.utils import plot, save_image
import julia.julia_serial as julia_serial
import julia.julia_np as julia_np
import julia.julia_numba as julia_numba
import julia.julia_parallel as julia_parallel
import julia.julia_parallel_numba as julia_parallel_numba
import julia.julia_numba_parallel as julia_numba_parallel
import julia.julia_fast as julia_fast

"""
5000x5000
serial                57.5 (julia_serial)
numpy                 49.8 (julia_numpy)
parallel x2           31.8 (julia_parallel)
parallel x4           18.9 (julia_parallel)
parallel x8           14.3 (julia_parallel)
numba                  5.1 (julia_numba)
parallel x8 numba      3.9 (julia_parallel_numba)
numba parallel         3.2 (julia_numa_parallel)
parallel x8 numba shm  3.0 (julia_fast)

10000x10000
numba                  21.23
numba parallel         13.56
parallel x8 numba shm   9.40 (with memory leak xD)
"""

if __name__ == "__main__":
    x_min, x_max, y_min, y_max = -1.8, 1.8, -1.8, 1.8
    c_real, c_imag = -0.62772, -.42193
    c = complex(c_real, c_imag)
    width = 10000
    height = 10000
    iter_max = 600
    z_max = 2

    start = time.time()
    iter_list = julia_fast.calc_julia_set(x_min, x_max, y_min, y_max, z_max, c, width, height, iter_max)
    end = time.time()

    print("Execution in {:.3f} sec".format(end - start))
    # plot(iter_list, width, height, iter_max)
    # save_image("julia_set2.png", iter_list, width, height, iter_max)

