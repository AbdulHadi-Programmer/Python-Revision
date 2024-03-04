def generate_pascals_triangle(n):
    triangle = [[1] * (i + 1) for i in range(n)]
    
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    
    return triangle

def print_pascals_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)).center(len(triangle[-1]) * 3))

# Example: Print Pascal's Triangle with 6 rows
rows = 6
pascals_triangle = generate_pascals_triangle(rows)
print_pascals_triangle(pascals_triangle)