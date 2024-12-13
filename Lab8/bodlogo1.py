def coin_change(coins, amount):
    memo = {}
    
    def dp(remaining):
        if remaining == 0:
            return 0
        if remaining < 0:
            return float('inf')
        
        if remaining in memo:
            return memo[remaining]
        
        result = float('inf')
        for coin in coins:
            result = min(result, 1 + dp(remaining - coin))
        
        memo[remaining] = result
        return result
    
    result = dp(amount)
    return result if result != float('inf') else -1

# Unit Test
import unittest

class TestCoinChange(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(coin_change([1, 2, 5], 11), 3)  # 5 + 5 + 1
        self.assertEqual(coin_change([2], 3), -1)        # Not possible
        self.assertEqual(coin_change([1], 0), 0)        # Zero amount, zero coins
        self.assertEqual(coin_change([1, 2, 5], 7), 2)  # 5 + 2
        self.assertEqual(coin_change([3, 4, 5], 6), 2)  # 3 + 3

# Run the tests
if __name__ == "__main__":
    unittest.main()
