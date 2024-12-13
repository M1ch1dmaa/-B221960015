import unittest

def numTrees(n: int) -> int:
    dp = [0] * (n + 1)
    
    dp[0] = 1 
    dp[1] = 1 
    
    for i in range(2, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - 1 - j]
    
    return dp[n]

class TestNumTrees(unittest.TestCase):
    def test_small_values(self):
        self.assertEqual(numTrees(2), 2)
        self.assertEqual(numTrees(3), 5)
if __name__ == '__main__':
    unittest.main()
