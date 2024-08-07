import julia_serial
import julia_numba

x_min, x_max, y_min, y_max = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -.42193
c = complex(c_real, c_imag)
width = 1000
height = 1000
iter_max = 300
z_max = 2
sum_exp = 33219980 # only for width=1000 and iter_max=300


def test_serial_julia():
    iter_list = julia_serial.calc_julia_set(x_min, x_max, y_min, y_max, z_max, c, width, height, iter_max)
    assert sum(iter_list) == sum_exp


def test_numba_julia():
    iter_list = julia_numba.calc_julia_set(x_min, x_max, y_min, y_max, z_max, c, width, height, iter_max)
    assert sum(iter_list) == sum_exp

