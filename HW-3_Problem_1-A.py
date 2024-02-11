#Chat GPT aided in writing this program

import math #imports math function

# Function to check if a matrix is symmetric
def is_symmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


# Function to check if a matrix is positive definite
def is_positive_definite(matrix):
    # Check if the matrix is symmetric
    if not is_symmetric(matrix):
        return False

    n = len(matrix)
    for i in range(n):
        # Check if the leading principal minors are positive
        submatrix = [row[:i + 1] for row in matrix[:i + 1]]
        determinant = calculate_determinant(submatrix)
        if determinant <= 0:
            return False
    return True


# Function to calculate the determinant of a matrix
def calculate_determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        determinant = 0
        for j in range(n):
            submatrix = [row[:j] + row[j + 1:] for row in matrix[1:]]
            determinant += matrix[0][j] * calculate_determinant(submatrix) * (-1) ** j
        return determinant


# Function to perform Cholesky decomposition
def cholesky_decomposition(matrix):
    n = len(matrix)
    L = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if i == j:
                sum_val = sum(L[i][k] ** 2 for k in range(j))
                L[i][j] = math.sqrt(matrix[i][i] - sum_val)
            else:
                sum_val = sum(L[i][k] * L[j][k] for k in range(j))
                L[i][j] = (matrix[i][j] - sum_val) / L[j][j]
    return L


# Function to solve the equation using forward and backward substitution
def solve_cholesky(L, b):
    n = len(L)
    y = [0.0] * n
    x = [0.0] * n

    # Forward substitution
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i][j] * y[j]
        y[i] /= L[i][i]

    # Backward substitution
    for i in range(n - 1, -1, -1):
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= L[j][i] * x[j]
        x[i] /= L[i][i]

    return x


# Function to perform LU decomposition using Doolittle's method
def lu_decomposition(matrix):
    n = len(matrix)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]
    for i in range(n):
        L[i][i] = 1.0
        for j in range(i, n):
            sum_val = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = matrix[i][j] - sum_val
        for j in range(i + 1, n):
            sum_val = sum(L[j][k] * U[k][i] for k in range(i))
            L[j][i] = (matrix[j][i] - sum_val) / U[i][i]
    return L, U


# Function to solve the equation using forward and backward substitution
def solve_doolittle(L, U, b):
    n = len(L)
    y = [0.0] * n
    x = [0.0] * n

    # Forward substitution
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i][j] * y[j]

    # Backward substitution
    for i in range(n - 1, -1, -1):
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]

    return x


# Problem 1-A matrices
problem_matrices = [
    ([[1, -1, 3, 2], [-1, 5, -5, -2], [3, -5, 19, 3], [2, -2, 3, 21]], [5, -35, 94, 1]),]

# Loop through problem matrices
for index, (matrix, b) in enumerate(problem_matrices, start=1):
    print(f"Problem {index}:")
    print("Matrix:")
    for row in matrix:
        print(row)
    print("Right-hand side (b):", b)

    if is_symmetric(matrix) and is_positive_definite(matrix):
        print("Matrix is symmetric and positive definite. Using Cholesky Method.")
        L = cholesky_decomposition(matrix)
        solution = solve_cholesky(L, b)
    else:
        print("Matrix is not symmetric and positive definite. Using Doolittle Method.")
        L, U = lu_decomposition(matrix)
        solution = solve_doolittle(L, U, b)

    print("Solution vector:", solution)
    print()



