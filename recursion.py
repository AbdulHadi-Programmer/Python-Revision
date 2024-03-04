# Recursion:
# Recursion is also a function and the function call itself inside a function 

# Factorial (7) = 7 * 6 * 5 * 4 * 3 * 2 * 1
# Factorial (0) = 1
# Factorial(n) = n * Factorial(n-1)
def factorial(n):
    if (n == 0) or (n==1):
        return 1
    else:
        return n * factorial(n-1)

n = 5
print(f"Factorial of num {n} is", factorial(n))
# Other Example 
def lst_sum(arr):
    # Base case: an empty array has a sum of 0
    if not arr:
        return 0
    # Recursive case: sum the first element and the sum of the rest of the elements
    else:
        return arr[0] + lst_sum(arr[1:])

# Example usage
result = lst_sum([1, 2, 3, 4, 5])
print(result)  # Output: 15
print(sum([1, 2, 3, 4, 5]))