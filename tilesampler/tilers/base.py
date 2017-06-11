"""
Base class for Tiler
"""

class BoundaryError(Exception):
    """ Exception raised when requested tile exceeds image boundary

    :param message: message when the exception is raised
    """
    def __init__(self, message):
        super(BoundaryError, self).__init__(message)
        self.message = message

class Tiler(object):
    """ Base Tiler class to be inherited by Tiler from other sources"""
    def get_tile(self, point, size):
        """ Get tile from image

        :param point: top left coordinate of the tile, in (x, y) format
        :param size: size of the tile (width, height)
        :raise: :error: NotImplementedError
        """
        raise NotImplementedError
