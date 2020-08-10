# number of rows and columns (in that order) for the first matrix
number_rows_columns = [int(row_by_column) for row_by_column in input(' ').split()]
matrix1 = []
# populate the first matrix row-wise
for x in range(number_rows_columns[0]):
    matrix1.append([int(digit) for digit in input(' ').split()])

# number of rows and columns (in that order) for the second matrix
number_rows2_columns2 = [int(row2_by_column2) for row2_by_column2 in input(' ').split()]
matrix2 = []
# populate the second matrix row-wise
for x in range(number_rows2_columns2[0]):
    matrix2.append([int(digit2) for digit2 in input(' ').split()])

# check if the number of rows and columns are equal for both matrices
if number_rows_columns[0] == number_rows2_columns2[0] and number_rows_columns[1] == number_rows2_columns2[1]:
    # add the matrices
    resultant_matrix = [[matrix1[i][j] + matrix2[i][j] for j in range(number_rows2_columns2[1])]
                        for i in range(number_rows2_columns2[0])]
    # display unpacked result matrix
    for R in resultant_matrix:
        print(*R)
else:
    print('ERROR')

