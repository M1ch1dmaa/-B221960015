import unittest
import os
import json

absolute_path = os.path.abspath(__file__)
file_path = os.path.join(os.path.dirname(absolute_path), "3-3.txt")

class Solution:
    def merge(self, arr, l, m, r):
        temp = [0] * (r - l + 1)
        i, j, k = l, m + 1, 0

        while i <= m and j <= r:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                j += 1
            k += 1

        while i <= m:
            temp[k] = arr[i]
            i += 1
            k += 1

        while j <= r:
            temp[k] = arr[j]
            j += 1
            k += 1

        for i in range(l, r + 1):
            arr[i] = temp[i - l]

    def mergeSort(self, arr, l, r):
        if l >= r:
            return
        
        m = (l + r) // 2

        self.mergeSort(arr, l, m)
        self.mergeSort(arr, m + 1, r)

        self.merge(arr, l, m, r)

    def sortArray(self, nums):
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums
    
class TestSortArray(unittest.TestCase):

    def test_sort_array(self):
        with open(file_path, 'r') as f:
            line = f.readline().strip()
            arr = json.loads(line)
        solution = Solution()
        sorted_arr = solution.sortArray(arr)
        self.assertEqual(sorted_arr, sorted(arr))

if __name__ == "__main__":
    unittest.main(verbosity=2)
