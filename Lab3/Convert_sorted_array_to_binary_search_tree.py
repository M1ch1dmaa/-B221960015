import unittest
import os
from typing import List, Optional

absolute_path = os.path.abspath(__file__)
file_path = os.path.join(os.path.dirname(absolute_path), "3-4.txt")


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.buildTree(nums, 0, len(nums) - 1)
    
    def buildTree(self, nums, left, right):
        if left > right:
            return None

        mid = (left + right) // 2
        root = TreeNode(nums[mid])

        root.left = self.buildTree(nums, left, mid - 1)
        root.right = self.buildTree(nums, mid + 1, right)

        return root

class TestSortedArrayToBST(unittest.TestCase):

    def treeToList(self, root: Optional[TreeNode]) -> List[int]:
        """Helper function to convert tree to list using in-order traversal."""
        result = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        inorder(root)
        return result

    def test_sort_array_to_bst(self):
        with open(file_path, 'r') as f:
            line = f.readline().strip()
        solution = Solution()
        best_root = solution.sortedArrayToBST(line)
        bst_list = self.treeToList(best_root)
        self.assertEqual(bst_list, sorted(line))
       
if __name__ == "__main__":
    unittest.main(verbosity=2)
