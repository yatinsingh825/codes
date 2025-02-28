def get_matrix_input(name):
    """Function to take matrix input from the user."""
    rows = int(input(f"Enter the number of rows for {name}: "))
    cols = int(input(f"Enter the number of columns for {name}: "))
    matrix = []
    print(f"Enter the elements of {name} row by row:")
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1} elements: ").split()))
        if len(row) != cols:
            print("Error: Number of elements in the row does not match the column count.")
            return None, None  # Return None for invalid input
        matrix.append(row)
    return matrix, rows, cols


def validate_matrix_sizes(rows_A, cols_A, rows_B, cols_B):
    """Function to validate if matrices have the same dimensions."""
    return rows_A == rows_B and cols_A == cols_B


def add_matrices(matrix_A, matrix_B):
    """Function to add two matrices of the same size."""
    rows = len(matrix_A)
    cols = len(matrix_A[0])
    result_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result_matrix[i][j] = matrix_A[i][j] + matrix_B[i][j]
    return result_matrix


def print_matrix(matrix, label):
    """Function to print a matrix with proper formatting."""
    print(f"\n{label}:")
    for row in matrix:
        print(" ".join(f"{num:3}" for num in row))
    print()


# Main Execution
print("Name: Bhawika  UID: 23BAI70725\n")

matrix_A, rows_A, cols_A = get_matrix_input("Matrix A")
if matrix_A is None:
    exit()

matrix_B, rows_B, cols_B = get_matrix_input("Matrix B")
if matrix_B is None:
    exit()

if not validate_matrix_sizes(rows_A, cols_A, rows_B, cols_B):
    print("Matrix sizes do not match. Unable to perform addition.")
    exit()

result_matrix = add_matrices(matrix_A, matrix_B)

print_matrix(matrix_A, "Matrix A")
print_matrix(matrix_B, "Matrix B")
print_matrix(result_matrix, "Resultant Matrix (A + B)")