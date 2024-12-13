import unittest
import os

absolute_path = os.path.abspath(__file__)
file_path = os.path.join(os.path.dirname(absolute_path), "test.txt")

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

class TestInsertionSort(unittest.TestCase):

    def test(self):
        with open(file_path, 'r') as f:
            line = f.readline()
            unsorted_str, sorted_str = line.split('    ')
            unsorted_arr = eval(unsorted_str)
            sorted_arr = eval(sorted_str)
        self.assertEqual(merge_sort(unsorted_arr), sorted_arr)

if __name__ == '__main__':
    unittest.main(verbosity=2)
