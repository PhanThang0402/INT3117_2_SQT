def find_S_rectangle(width, length):
    if length <= 0 or width <= 0:
        return "Error: Length and Width must be greater than 0"
    return length*width

import unittest

class TestArea(unittest.TestCase):
    def test_area_1(self):
        self.assertEqual(find_S_rectangle(10, 5), 50)
        
    def test_area_2(self):
        self.assertEqual(find_S_rectangle(-1, 5), "error: Invalid input")
        
if __name__ == '__main__':
    unittest.main()