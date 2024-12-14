def compute_new_potential(phi_values):
    """
    Compute the new potential function Φ' given Φ using dynamic programming.
    Φ'(D_i) = Φ(D_i) - Φ(D_0).
    """
    # Get Φ(D_0), the initial potential
    phi_d0 = phi_values[0]

    # Calculate Φ' for all D_i
    phi_prime = [phi - phi_d0 for phi in phi_values]

    return phi_prime

def verify_potential(phi_values, phi_prime):
    """
    Verify the properties of Φ' and the cost equivalence.
    """
    phi_d0 = phi_values[0]

    # Check Φ'(D_0) = 0
    assert phi_prime[0] == 0, "Φ'(D_0) must be 0"

    # Check Φ'(D_i) ≥ 0 for all i
    assert all(phi >= 0 for phi in phi_prime), "All Φ'(D_i) must be non-negative"

    # Verify unit cost equivalence (relative differences remain the same)
    original_costs = [phi_values[i] - phi_values[i - 1] for i in range(1, len(phi_values))]
    new_costs = [phi_prime[i] - phi_prime[i - 1] for i in range(1, len(phi_prime))]
    assert original_costs == new_costs, "Unit costs of Φ and Φ' must be equal"

    return True

# Example usage
phi_values = [10, 12, 15, 20, 27]  # Example Φ(D_i) values

# Compute Φ'
phi_prime = compute_new_potential(phi_values)

# Verify properties
if verify_potential(phi_values, phi_prime):
    print("Φ' satisfies all conditions:")
    print("Original Φ:", phi_values)
    print("Transformed Φ':", phi_prime)
