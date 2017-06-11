"""
Image stratified sampler class
"""

import numpy as np
from .base import Strampler

class BoundaryError(Exception):
    """ Exception raised when requested tile exceeds image boundary

    :param message: message when the exception is raised
    """
    def __init__(self, message):
        super(BoundaryError, self).__init__(message)
        self.message = message

class ImageStrampler(Strampler):
    """Image stratified sampler that generates batches of tiles with equal
    probabilities of each class

    :param num_classes: number of label classes
    """
    def get_tile_from_PIL_image(self, image, point, size):
        """Get tile from a :class:`PIL.Image.Image` image

        :param image: a :class:`PIL.Image.Image` object
        :param point: top left coordinate of the tile, in (x, y) format
        :param size: size of the tile (height, width)
        :return: a :class:`numpy.ndarray` of tile
        """
        arr = np.asarray(image)
        x, y = point
        h, w = size

        if h <= 0 or w <= 0:
            raise ValueError("Tile size cannot be zero or negative!")

        if (x < 0 or y < 0 or
            x+h > image.size[1] or y+w > self.image.size[0]):
            raise BoundaryError("Request size exceeds image boundary!")

        return arr[x:(x+h), y:(y+w)]



