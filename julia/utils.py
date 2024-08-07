import matplotlib.pyplot as plt
import numpy as np
from typing import List


def plot(iter_list: List[int], width: int, height: int, iter_max: int):
    assert len(iter_list) == width * height
    iter_map = np.array(iter_list)
    iter_map = iter_map / iter_max
    iter_map = iter_map.reshape((width, height))
    plt.imshow(iter_map)
    plt.show()
