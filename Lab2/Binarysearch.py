import unittest
import os

absolute_path = os.path.abspath(__file__)
file_path = os.path.join(os.path.dirname(absolute_path), "testbinary.txt")

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        return -1

class TestBinarySearch(unittest.TestCase):

    def test(self):
        with open(file_path, "r") as f:
            line = f.readline()
            a, b = line.split('    ')
            a = eval(a)
            b = eval(b)
        self.assertEqual(binary_search(a, 0, len(a) - 1, 7), b)


if __name__ == '__main__':
    unittest.main(verbosity=2)
