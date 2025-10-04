# from scipy.sparse import csr_matrix,csr_array

# print(csr_matrix(([1,2,3,4,5,6,7,8,9,10],([0,0,0,0,0,1,1,1,1,1],[0,0,2,1,2,0,0,4,0,1]))).toarray())

# Python program to create
# sparse matrix using csr_matrix()

# Import required package
# import numpy as np
# from scipy.sparse import csr_matrix

# # Creating a 3 * 4 sparse matrix
# sparseMatrix = csr_matrix((3, 4),
# 						dtype = np.int8).toarray()

# # Print the sparse matrix
# print(sparseMatrix)

# Python program to create
# sparse matrix using csr_matrix()

# Import required package
import numpy as np
from scipy.sparse import csr_matrix

row = np.array([0, 0, 1, 1, 2, 1])
col = np.array([0, 1, 2, 0, 2, 2])

# taking data
data = np.array([1, 4, 5, 8, 9, 6])

# creating sparse matrix
sparseMatrix = csr_matrix((data, (row, col)),
						shape = (3, 3))
# print the sparse matrix
print(sparseMatrix)
print(sparseMatrix.toarray())
