if 'line_profiler' not in dir() and 'profile' not in dir():
    def profile(func):
        return func

from line_profiler import profile

@profile
def calc_z_pure_python_serial(zs, c, z_max, iter_max):
    iter_map = [0]*len(zs)
    for i in range(len(zs)):
        n = 0
        z = zs[i]
        while abs(z) < z_max and n < iter_max:  
            z = z*z + c
            n += 1
        iter_map[i] = n
    return iter_map

@profile
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

    # calculate iterations
    iter_map = calc_z_pure_python_serial(zs, c, z_max, iter_max)
    return iter_map


"""
Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     7                                           @profile
     8                                           def calc_z_pure_python_serial(zs, c, z_max, iter_max):
     9         1        655.0    655.0      0.0      iter_map = [0]*len(zs)
    10   1000001     117236.0      0.1      1.0      for i in range(len(zs)):
    11   1000000      92722.0      0.1      0.8          n = 0
    12   1000000     100723.0      0.1      0.8          z = zs[i]
    13  34219980    5117641.0      0.1     42.3          while abs(z) < z_max and n < iter_max:  
    14  33219980    3454951.0      0.1     28.6              z = z*z + c
    15  33219980    3118435.0      0.1     25.8              n += 1
    16   1000000      95198.0      0.1      0.8          iter_map[i] = n
    17         1          2.0      2.0      0.0      return iter_map

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    19                                           @profile
    20                                           def calc_julia_set(x_min, x_max, y_min, y_max, z_max, c, width, height, iter_max):
    21                                               # initialize zs
    22         1          1.0      1.0      0.0      x_step = (x_max - x_min) / width
    23         1          0.0      0.0      0.0      y_step = (y_max - y_min) / height
    24                                           
    25      1001        147.0      0.1      0.0      x_cords = [x_min + (i*x_step) for i in range(0, width, 1)]
    26      1001        142.0      0.1      0.0      y_cords = [y_min + (i*y_step) for i in range(0, height, 1)]
    27                                           
    28         1          0.0      0.0      0.0      zs = []
    29      1001        120.0      0.1      0.0      for x in x_cords:
    30   1001000      97811.0      0.1      0.4          for y in y_cords:
    31   1000000     129160.0      0.1      0.5              zs.append(complex(x, y))
    32                                           
    33                                               # calculate iterations
    34         1   25341192.0    3e+07     99.1      iter_map = calc_z_pure_python_serial(zs, c, z_max, iter_max)
    35         1          1.0      1.0      0.0      return iter_map
"""
