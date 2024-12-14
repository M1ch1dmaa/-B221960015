
def calculate_unit_cost(n):
    # Function to check if a number is a power of two
    def is_power_of_two(x):
        return (x & (x - 1)) == 0 and x > 0

    # Dynamic programming array to store the cost of operations
    dp = [0] * (n + 1)

    # Base case
    dp[0] = 0

    # Calculate costs for each operation
    for i in range(1, n + 1):
        if is_power_of_two(i):
            dp[i] = dp[i - 1] + i  # Add i (since i is a power of two)
        else:
            dp[i] = dp[i - 1] + 1  # Add 1 (since i is not a power of two)

    # Total cost
    total_cost = dp[n]

    # Unit cost (average)
    unit_cost = total_cost / n

    return total_cost, unit_cost


# Example usage
if __name__ == "__main__":
    n = int(input("Enter the number of operations (n): "))
    total_cost, unit_cost = calculate_unit_cost(n)
    print(f"Total cost of {n} operations: {total_cost}")
    print(f"Unit cost (average cost per operation): {unit_cost:.2f}")
