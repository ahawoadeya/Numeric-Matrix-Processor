def add_vectors(v1, v2):
    return [elem1 + elem2 for elem1, elem2 in zip(v1, v2)]


def inner_product(v1, v2):
    return sum(elem1 * elem2 for elem1, elem2 in zip(v1, v2))


def add_matrices(m1, m2):
    return [add_vectors(row1, row2) for row1, row2 in zip(m1, m2)]


def matrix_dimensions(matrix):
    return len(matrix), len(matrix[0])


def scalar_mul_matrix(scalar, matrix):
    return [[round(scalar * elem, 3) for elem in row] for row in matrix]


def mul_matrices(m1, m2):
    return [[inner_product(m1_row, m2_col) for m2_col in zip(*m2)] for m1_row in m1]


def transpose_vertical(matrix):
    return [list(reversed(row)) for row in matrix]


def transpose_horizontal(matrix):
    return list(reversed(matrix))


def transpose_main(matrix):
    return [list(new_row) for new_row in zip(*matrix)]


def transpose_side(matrix):
    return transpose_main(transpose_horizontal(transpose_vertical(matrix)))


def del_row(row_target, matrix):
    return [row for row_num, row in enumerate(matrix) if row_num != row_target]


def del_col(col_target, matrix):
    return transpose_main(del_row(col_target, transpose_main(matrix)))


def minor(row, col, matrix):
    return determinant(del_row(row, del_col(col, matrix)))


def cofactor(row, col, matrix):
    return (-1) ** (row + col) * minor(row, col, matrix)


def cofactor_matrix(matrix):
    height, width = matrix_dimensions(matrix)
    return [[cofactor(row, col, matrix) for col in range(width)] for row in range(height)]


def determinant(matrix):
    height, width = matrix_dimensions(matrix)
    if (height, width) == (1, 1):
        return matrix[0][0]
    if (height, width) == (2, 2):
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    else:
        cofactors = [cofactor(0, col, matrix) for col in range(width)]
        return inner_product(matrix[0], cofactors)


def inverse_matrix(matrix):
    return scalar_mul_matrix(1 / determinant(matrix),
                             transpose_main(cofactor_matrix(matrix)))


def is_invertible(matrix):
    return determinant(matrix) != 0


def matrix_str(matrix):
    rows = (' '.join(map(str, row)) for row in matrix)
    return '\n'.join(rows)


def prompt_dimensions(query):
    height, width = [int(dimension) for dimension in input(query).split()]
    return height, width


def as_number(number_str):
    return int(number_str) if number_str.isnumeric() else float(number_str)


def prompt_matrix(height):
    return [[as_number(e) for e in input().split()] for _ in range(height)]


def prompt_two_matrices():
    m1_height, m1_width = prompt_dimensions('Enter size of first matrix: ')
    print('Enter first matrix: ')
    matrix1 = prompt_matrix(m1_height)

    m2_height, m2_width = prompt_dimensions('Enter size of second matrix: ')
    print('Enter second matrix: ')
    matrix2 = prompt_matrix(m2_height)
    return matrix1, matrix2


def matrix_addition_routine():
    matrix1, matrix2 = prompt_two_matrices()
    if matrix_dimensions(matrix1) != matrix_dimensions(matrix2):
        print('The operation cannot be performed')
    else:
        print(matrix_str(add_matrices(matrix1, matrix2)))


def matrix_scalar_multiplication_routine():
    m_height, m_width = prompt_dimensions('Enter size of matrix: ')
    print('Enter matrix: ')
    m = prompt_matrix(m_height)
    constant = float(input('Enter constant: '))
    print('The result is:')
    print(matrix_str(scalar_mul_matrix(constant, m)))


def multiply_matrices_routine():
    matrix1, matrix2 = prompt_two_matrices()
    height1, width1 = matrix_dimensions(matrix1)
    height2, width2 = matrix_dimensions(matrix2)
    if width1 != height2:
        print('The operation cannot be performed')
    else:
        print(matrix_str(mul_matrices(matrix1, matrix2)))


def transpose_matrix_routine():
    print('\n', '\n'.join(['1. Main diagonal', '2. Side diagonal',
                           '3. Vertical line', '4. Horizontal line']))
    transpose_choice = input('Your choice: ')
    height, width = prompt_dimensions('Enter matrix size: ')
    m = prompt_matrix(height)
    print('The result is:')
    if transpose_choice == '1':
        print(matrix_str(transpose_main(m)))
    elif transpose_choice == '2':
        print(matrix_str(transpose_side(m)))
    elif transpose_choice == '3':
        print(matrix_str(transpose_vertical(m)))
    elif transpose_choice == '4':
        print(matrix_str(transpose_horizontal(m)))


def matrix_determinant_routine():
    height, width = prompt_dimensions('Enter matrix size: ')
    print('Enter matrix:')
    m = prompt_matrix(height)
    print('The result is:')
    print(determinant(m))


def matrix_inverse_routine():
    height, width = prompt_dimensions('Enter matrix size: ')
    print('Enter matrix:')
    m = prompt_matrix(height)
    if not is_invertible(m):
        print("This matrix doesn't have an inverse.")
    else:
        print(matrix_str(inverse_matrix(m)))


while True:
    print('\n'.join(['1. Add matrices', '2. Multiply matrix by a constant',
                     '3. Multiply matrices', '4. Transpose matrix',
                     '5. Calculate a determinant', '0. Exit']))
    choice = input('Your choice: ')
    if choice == '1':
        matrix_addition_routine()
    elif choice == '2':
        matrix_scalar_multiplication_routine()
    elif choice == '3':
        multiply_matrices_routine()
    elif choice == '4':
        transpose_matrix_routine()
    elif choice == '5':
        matrix_determinant_routine()
    elif choice == '6':
        matrix_inverse_routine()
    else:
        break
