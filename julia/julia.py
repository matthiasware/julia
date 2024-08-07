import time
from utils import plot
import julia_serial
import julia_np
import julia_numba

x_min, x_max, y_min, y_max = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -.42193
c = complex(c_real, c_imag)
width = 5000
height = 5000
iter_max = 300
z_max = 2


start = time.time()
iter_list = julia_np.calc_julia_set(x_min, x_max, y_min, y_max, z_max, c, width, height, iter_max)
end = time.time()

print("Execution in {:.3f} sec".format(end - start))
# plot(iter_list, width, height, iter_max)

"""
5000x5000
serial    57.5
numpy     49.8
numba      5.1
parallel
"""
