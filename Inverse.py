#!usr/bin/env python
from copy import deepcopy

#find the inverse of the matrix using the cofactor method

def minor(matrix, N, Q):
	#have to make a deepcopy o.w. the original matrix gets altered
	new_M = deepcopy(matrix)

	#this removes a column
	for b in range(len(new_M)):
		del new_M[b][N]

	#this removes the first row
	new_M.remove(new_M[Q])
	return new_M

def determinant(matrix):

	#base case, if len(matrix) < 2
	if(len(matrix) == 1):
		return matrix[0][0]
	elif(len(matrix) == 2):
		x = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
		return x	
	else:
		det = 0
		for i in range(len(matrix)):
			det = det + (-1)**i*matrix[0][i]*determinant(minor(matrix, i, 0))
		return det

def cofactor(matrix):

	#initialize a cofactor matrix
	cofactor = [0] * len(matrix)
	for i in range(len(matrix)):
		cofactor[i] = [0] * len(matrix[0])

	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			cofactor[i][j] = (-1)**(i+j)*determinant(minor(matrix, i, j))

	return cofactor

def inverse(matrix):
	det = determinant(matrix)
	if( det == 0):
		print("Not invertible")
		return
	cof = cofactor(matrix)

	for i in range(len(cof)):
		for j in range(len(cof)):
			cof[i][j] = cof[i][j]/det
	return cof

m1 = [ [7, 2, 1],
		[0, 3, -1],
		[-3, 4, -2] ]

#print(inverse(m1))