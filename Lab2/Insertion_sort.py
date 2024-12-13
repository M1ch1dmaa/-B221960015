import unittest
import os

absolute_path = os.path.abspath(__file__)
file_path = os.path.join(os.path.dirname(absolute_path), "test.txt")

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr



class TestInsertionSort(unittest.TestCase):

    def test(self):
        with open(file_path, 'r') as f:
            line = f.readline()
            unsorted_str, sorted_str = line.split('    ')
            unsorted_arr = eval(unsorted_str)
            sorted_arr = eval(sorted_str)

        self.assertEqual(insertion_sort(unsorted_arr), sorted_arr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
