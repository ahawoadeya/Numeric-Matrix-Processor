# read from input number of row and columns (in that order) of the matrix
number_rows_columns = [int(row_by_column) for row_by_column in input(' ').split()]
matrix = []
# populate the matrix row-wise
for x in range(number_rows_columns[0]):
    matrix.append([int(digit) for digit in input(' ').split()])

constant = int(input(' '))

# multiply each individual element in the matrix with the constant.
resultant_matrix = [[matrix[rows][columns] * constant for columns in range(number_rows_columns[1])] for rows in range(number_rows_columns[0])]

# iterate through the resulting matrix and display the unpacked data
for sections in resultant_matrix:
    print(*sections)
