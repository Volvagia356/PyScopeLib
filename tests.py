from pyscopelib import *
import unittest

class TestLineFunctions(unittest.TestCase):
    def setUp(self):
        self.hline = Line(0,0,1,0)
        self.vline = Line(0,0,0,1)
        self.dline = Line(0,0,1,1)

    def test_length(self):
        self.assertEqual(self.hline.get_length(), 1)
        self.assertEqual(self.vline.get_length(), 1)
        self.assertEqual(self.dline.get_length(), 2**0.5)

if __name__ == "__main__":
    unittest.main()
