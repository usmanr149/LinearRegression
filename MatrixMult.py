#!usr/bin/env python

def MatrixMultiplication(matrix1, matrix2):
	if (len(matrix1[0]) != len(matrix2)):
		print("Matrix multiplication not possible")
		return
	else:
		matrixM = [0] * len(matrix1)
		for i in range(len(matrix1)):
			matrixM[i] = [0] * len(matrix2[0])

	for i in range(len(matrixM)):
		for j in range(len(matrixM[0])):
			for k in range(len(matrix1[0])):
				matrixM[i][j] = matrixM[i][j] + matrix1[i][k]*matrix2[k][j]
	return matrixM