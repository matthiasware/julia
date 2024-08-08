import multiprocessing as mp

def calc_z(z, c, z_max, iter_max):
    n = 0
    while abs(z) < z_max and n < iter_max:
        z = z*z + c
        n += 1
    return n

def calc_zs_worker(iter_map, pid, width, height, c, iter_max, z_max, x_min, x_max, y_min, y_max, offset):
    x_step = (x_max - x_min) / width
    y_step = (y_max - y_min) / height

    for idx_y in range(pid, height, offset):
        z_imag = y_min + (idx_y * y_step)
        for idx_x in range(width):
            z_real = x_min + (idx_x * x_step)
            z = complex(z_real, z_imag)
            n = calc_z(z, c, z_max, iter_max)
            iter_map[(idx_y * width) + idx_x] = n

def calc_julia_set(x_min, x_max, y_min, y_max, z_max, c, width, height, iter_max, n_workers=None):
    if not n_workers:
        n_workers = mp.cpu_count()
    iter_map = mp.Array("i", width*height, lock=False)

    ps = [mp.Process(target=calc_zs_worker,
                     args=(iter_map, pid, width, height,
                           c, iter_max, z_max,
                           x_min, x_max, y_min, y_max, n_workers)) for pid in range(n_workers)]

    for p in ps:
        p.start()
    for p in ps:
        p.join()
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

    iter_map = calc_julia_set(x_min, x_max, y_min, y_max, z_max, c, width, height, iter_max)
    plot(iter_map, width, height, iter_max)

    # n_workers = mp.cpu_count()
    # iter_map = mp.Array("i", width*height, lock=False)

    # ps = [mp.Process(target=calc_zs_worker,
    #                  args=(iter_map, pid, width, height,
    #                        c, iter_max, z_max,
    #                        x_min, x_max, y_min, y_max, n_workers)) for pid in range(n_workers)]

    # for p in ps:
    #     p.start()
    # for p in ps:
    #     p.join()

    # iter_map = list(iter_map)
    # plot(iter_map, width, height, iter_max)

