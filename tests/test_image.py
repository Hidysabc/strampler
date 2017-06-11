"""
Test cases for `strampler.image`
"""

from PIL import Image as pilimage
import numpy as np
import unittest

from strampler.image import BoundaryError, ImageStrampler

class TestImageStrampler(unittest.TestCase):
    def setUp(self):
        self.imgstrampler = ImageStrampler(2)

    def test_get_tile_from_PIL_image(self):
        # setup test data
        arr = np.random.randint(0, 256, (100, 100, 3))
        image = pilimage.fromarray(arr.astype(np.uint8))

        # test negative size
        with self.assertRaises(ValueError):
            self.imgstrampler.get_tile_from_PIL_image(image, (0, 0), (-1, 1))

        with self.assertRaises(ValueError):
            self.imgstrampler.get_tile_from_PIL_image(image, (0, 0), (0, 1))

        with self.assertRaises(ValueError):
            self.imgstrampler.get_tile_from_PIL_image(image, (0, 0), (1, -1))

        with self.assertRaises(ValueError):
            self.imgstrampler.get_tile_from_PIL_image(image, (0, 0), (1, 0))

        # test boundary error
        with self.assertRaises(BoundaryError):
            self.imgstrampler.get_tile_from_PIL_image(image, (-1, 0), (10, 10))

        with self.assertRaises(BoundaryError):
            self.imgstrampler.get_tile_from_PIL_image(image, (0, -1), (10, 10))

        with self.assertRaises(BoundaryError):
            self.imgstrampler.get_tile_from_PIL_image(image, (95, 0), (10, 10))

        with self.assertRaises(BoundaryError):
            self.imgstrampler.get_tile_from_PIL_image(image, (0, 95), (10, 10))

        # test tile output
        tile = self.imgstrampler.get_tile_from_PIL_image(image, (25, 75),
                                                         (3, 5))
        self.assertIsInstance(tile, np.ndarray)
        self.assertEqual(tile.shape, (3, 5, 3))


if __name__ == "__main__":
    unittest.main()
