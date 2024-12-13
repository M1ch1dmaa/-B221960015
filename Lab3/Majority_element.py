import unittest
import os
import json

absolute_path = os.path.abspath(__file__)
file_path = os.path.join(os.path.dirname(absolute_path), "3-1.txt")

class Solution:
    def majorityElement(self, nums) -> int:
        return self.helper(nums, 0, len(nums))[0]

    def helper(self, nums, l, r):
        if l == r - 1:
            return nums[l], 1
        mid = l + (r - l) // 2
        maj_left, extra_left = self.helper(nums, l, mid)
        maj_right, extra_right = self.helper(nums, mid, r)

        if maj_right == maj_left:
            maj = maj_left
            extra = extra_left + extra_right
        elif extra_right > extra_left:
            maj = maj_right
            extra = extra_right - extra_left
        else:
            maj = maj_left
            extra = extra_left - extra_right
        return maj, extra

class TestMajorityElement(unittest.TestCase):

    def test_majority_element(self):
        with open(file_path, 'r') as f:
            line = f.readline().strip()
            arr = json.loads(line)
        solution = Solution()
        self.assertEqual(solution.majorityElement(arr), 3)

if __name__ == "__main__":
    unittest.main(verbosity=2)
