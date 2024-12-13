import unittest
import os

absolute_path = os.path.abspath(__file__)
file_path = os.path.join(os.path.dirname(absolute_path), "5-1.txt")

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    dp = [0] * (n+1)
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1]+ dp[i-2]

    return dp[n]



class TestFibonacci(unittest.TestCase):
    def test(self):
        with open(file_path, 'r') as f:
            line = f.readline()
            input, output = line.split(',')
            input_arr = eval(input)
            output_arr = eval(output)

        self.assertEqual(fibonacci(input_arr), output_arr)    


if __name__ == "__main__":
    unittest.main()
