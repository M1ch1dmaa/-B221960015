import unittest

def fractional_knapsack_greedy(weights, values, capacity):
    items = [(values[i] / weights[i], weights[i], values[i]) for i in range(len(weights))]
    items.sort(reverse=True, key=lambda x: x[0])

    total_value = 0
    for ratio, weight, value in items:
        if capacity >= weight:
            total_value += value
            capacity -= weight
        else:
            total_value += ratio * capacity
            break
    
    return total_value

class TestFractionalKnapsackGreedy(unittest.TestCase):
    def test_basic_case(self):
        weights = [10, 20, 30]
        values = [60, 100, 120]
        capacity = 50
        self.assertAlmostEqual(fractional_knapsack_greedy(weights, values, capacity), 240.0)
        
if __name__ == "__main__":
    unittest.main()
