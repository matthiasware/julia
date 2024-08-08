import julia.julia_serial as julia_serial
import julia.julia_np as julia_np
import julia.julia_numba as julia_numba
import julia.julia_parallel as julia_parallel
import julia.julia_parallel_numba as julia_parallel_numba
import julia.julia_numba_parallel as julia_numba_parallel
import julia.julia_fast as julia_fast

x_min, x_max, y_min, y_max = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -.42193
c = complex(c_real, c_imag)
width = 1000
height = 1000
iter_max = 300
z_max = 2

# only for width=1000 and iter_max=300
sum_exp = 33219980

def test_serial():
    iter_list = julia_serial.calc_julia_set(x_min, x_max, y_min, y_max, z_max, c, width, height, iter_max)
    assert sum(iter_list) == sum_exp

def test_numba():
    iter_list = julia_numba.calc_julia_set(x_min, x_max, y_min, y_max, z_max, c, width, height, iter_max)
    assert sum(iter_list) == sum_exp

def test_parallel():
    iter_map = julia_parallel.calc_julia_set(x_min, x_max, y_min, y_max, z_max, c, width, height, iter_max)
    assert sum(list(iter_map)) == sum_exp

def test_parallel_numba():
    iter_map = julia_parallel_numba.calc_julia_set(x_min, x_max, y_min, y_max, z_max, c, width, height, iter_max)
    assert sum(list(iter_map)) == sum_exp

def test_numba_parallel():
    iter_map = julia_numba_parallel.calc_julia_set(x_min, x_max, y_min, y_max, z_max, c, width, height, iter_max)
    assert sum(list(iter_map)) == sum_exp

def test_fast():
    iter_map = julia_fast.calc_julia_set(x_min, x_max, y_min, y_max, z_max, c, width, height, iter_max)
    assert sum(list(iter_map)) == sum_exp

