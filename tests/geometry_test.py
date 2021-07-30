import unittest
from .context import src

class AreaTest(unittest.TestCase):
    def test_TrangleArea(self):
        self.assertEqual(src.trangelArea(4, 8), 16)

    def test_SquareArea(self):
        self.assertTrue(src.squareArea(5) == 25)
