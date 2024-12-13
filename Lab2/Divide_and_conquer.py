import unittest
import os

absolute_path = os.path.abspath(__file__)
file_path = os.path.join(os.path.dirname(absolute_path), "testdivide.txt")

def find_max(arr, low, high):
    if low == high:
        return arr[low]

    mid = (low + high) // 2
    left_max = find_max(arr, low, mid)
    right_max = find_max(arr, mid + 1, high)
    
    return max(left_max, right_max)

class TestFindMax(unittest.TestCase):

    def test(self):
        with open(file_path, 'r') as f:
            line = f.readline()
            a, b = line.split('    ')
            a = eval(a)
            b = eval(b)
        self.assertEqual(find_max(a, 0, len(a) - 1), b)

if __name__ == '__main__':
    unittest.main(verbosity=2)
