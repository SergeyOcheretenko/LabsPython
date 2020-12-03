def to_str(matrix):  # format matrix to string
    str_matrix = ''
    for row in matrix:
        for number in row:
            str_matrix += str(number) + ' '
        str_matrix += '\n'
    return str_matrix[:len(str_matrix) - 1]

m, n = map(int, input().split())  # input the size of the matrix
array = []  # creating a matrix
for _ in range(m):
    array.append(list(map(int, input().split())))  # input rows of the matrix
print('Created matrix:\n' + to_str(array))  # output of the created matrix
for i in range(m):
    for j in range(i + 1, m):
        if array[j][n - 1] < array[i][n - 1]:
            array[j], array[i] = array[i], array[j] # sorting rows
print('Sorted matrix:\n' + to_str(array))  # output of the sorted matrix
