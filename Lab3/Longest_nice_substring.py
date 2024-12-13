import unittest
import os

absolute_path = os.path.abspath(__file__)
file_path = os.path.join(os.path.dirname(absolute_path), "3-2.txt")

def longestNiceSubstring(s: str) -> str:
    ans = ""
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if all(s[k].swapcase() in s[i:j] for k in range(i, j)): 
                ans = max(ans, s[i:j], key=len)
    return ans

class TestLongestNiceSubstring(unittest.TestCase):

    def test_longest(self):
        with open(file_path, 'r') as f:
            line = f.readline().strip()
            arr = eval(line)
        self.assertEqual(longestNiceSubstring(arr), 'aAa')

if __name__ == "__main__":
    unittest.main(verbosity=2)
