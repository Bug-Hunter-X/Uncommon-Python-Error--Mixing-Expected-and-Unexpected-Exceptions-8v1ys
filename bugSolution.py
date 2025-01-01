def improved_function(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Invalid input types: Inputs must be numbers")
    if b == 0:
        return 0  # Or raise a custom exception for more specific handling
    return a / b

# Example
print(improved_function(10, 2))  # Output: 5.0
print(improved_function(10, 0))  # Output: 0

try:
    print(improved_function(10, "a"))
except TypeError as e:
    print(f"Error: {e}") #Output: Error: Invalid input types: Inputs must be numbers