"""
Test cases for `tilesampler.tilers.pil`
"""

from PIL import Image as pilimage
import numpy as np
import unittest

from tilesampler.tilers.base import BoundaryError
from tilesampler.tilers.pil import PILTiler

class TestPILTiler(unittest.TestCase):
    def setUp(self):
        arr = np.random.randint(0, 256, (100, 100, 3))
        self.image = pilimage.fromarray(arr.astype(np.uint8))
        self.piltiler = PILTiler(self.image)

    def test_get_tile(self):
        # test negative size
        with self.assertRaises(ValueError):
            self.piltiler.get_tile((0, 0), (-1, 1))

        with self.assertRaises(ValueError):
            self.piltiler.get_tile((0, 0), (0, 1))

        with self.assertRaises(ValueError):
            self.piltiler.get_tile((0, 0), (1, -1))

        with self.assertRaises(ValueError):
            self.piltiler.get_tile((0, 0), (1, 0))

        # test boundary error
        with self.assertRaises(BoundaryError):
            self.piltiler.get_tile((-1, 0), (10, 10))

        with self.assertRaises(BoundaryError):
            self.piltiler.get_tile((0, -1), (10, 10))

        with self.assertRaises(BoundaryError):
            self.piltiler.get_tile((95, 0), (10, 10))

        with self.assertRaises(BoundaryError):
            self.piltiler.get_tile((0, 95), (10, 10))

        # test tile output
        tile = self.piltiler.get_tile((25, 75), (3, 5))
        self.assertIsInstance(tile, np.ndarray)
        self.assertEqual(tile.shape, (3, 5, 3))


if __name__ == "__main__":
    unittest.main()
