"""
Tiler classes and functions based on PIL
"""

import numpy as np
from .base import Tiler, BoundaryError


class PILTiler(Tiler):
    """ Tiler on PIL images

    :param image: a :class:`PIL.Image` object
    """
    def __init__(self, image):
        self.image = image
        self.image_size = image.size
        self.arr = np.asarray(image)

    def get_tile(self, point, size):
        """Get tile from image

        :param point: top left coordinate of the tile, in (x, y) format
        :param size: size of the tile (height, width)
        :return: a :class:`numpy.ndarray` of tile
        """
        x, y = point
        h, w = size

        if h <= 0 or w <= 0:
            raise ValueError("Tile size cannot be zero or negative!")

        if (x < 0 or y < 0 or
            x+h > self.image_size[1] or y+w > self.image_size[0]):
            raise BoundaryError("Request size exceeds image boundary!")

        return self.arr[x:(x+h), y:(y+w)]


