import numpy as np

array_1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array_2 = np.array([10, dtype=np.float64])

print(array_1)

matrix_from_1 = array_1.reshape(2, 4)
matrix_from_2 = array_2.reshape(5, 2)

print(matrix_from_1)
print(matrix_from_2)

copy_matrix_2 = matrix_from_2.copy()
copy_matrix[1] = [9, 3]

print(matrix_from_2)
print(copy_matrix_2)

matrix = np.zero((5, 5))
matrix_ones = np.ones((5, 5))
matrix_randoms = np.random.randint(0, 10, (5, 5))

print("----")
print(matrix)
print(matrix_ones)
print(matrix_randoms)