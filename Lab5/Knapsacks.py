import unittest
import os

absolute_path = os.path.abspath(__file__)
file_path = os.path.join(os.path.dirname(absolute_path), "5-2.txt")

def knapsack(W, weights, values, n):
    dp = [[0 for _ in range(W+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(W+1):
            if weights[i-1]<=w:
                dp[i][w] = max(values[i-1]+dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][W]
          


class TestInsertionSort(unittest.TestCase):

    def test(self):
        with open(file_path, 'r') as f:
            line = f.readline().strip()
            W, weights, values, n, output = eval(line)
            W = int(W)
            weights = list(map(int, weights))
            values = list(map(int, values))
            n = int(n)
            output = int(output)
        self.assertEqual(knapsack(W, weights, values, n), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
