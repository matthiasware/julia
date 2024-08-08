import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from typing import List
from PIL import Image


def plot(iter_list: List[int], width: int, height: int, iter_max: int):
    assert len(iter_list) == width * height
    iter_map = np.array(iter_list)
    iter_map = iter_map / iter_max
    iter_map = iter_map.reshape((width, height))
    plt.imshow(iter_map)
    plt.show()


def save_image(p_image, iter_list: List[int], width: int, height: int, iter_max: int):
    assert len(iter_list) == width * height
    iter_map = np.array(iter_list)
    iter_map = iter_map / iter_max
    iter_map = iter_map.reshape((width, height))

    im = Image.fromarray(np.uint8(cm.gist_earth(iter_map)*255))
    im.save(p_image)



