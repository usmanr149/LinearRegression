#!usr/bin/env python
from MatrixMult import MatrixMultiplication
from Inverse import inverse
#This is where the data will be read

#First form the equation (X^T X)^-1 X^T Y

#Form the xmatrix
def XMatrix(n, dataX):
	#Initialize a matrix of the right size
	#number of rows
	xmatrix = [0] * len(dataX)
	#number of column
	for i in range(len(dataX)):
		xmatrix[i] = [0]*(n+1)

	for i in range(len(dataX)):
		for j in range(n+1):
			xmatrix[i][j] = dataX[i]**j
	return xmatrix

def XMatrixT(xmatrix):
	#Initialize a matrix of the right size
	#len(xmatrixis the number of rows)
	xmatrixT = [0]*len(xmatrix[0])

	for i in range(len(xmatrix[0])):
		xmatrixT[i] = [0]*len(xmatrix)

	for i in range(len(xmatrix)):
		for j in range(len(xmatrix[0])):
			xmatrixT[j][i] = xmatrix[i][j]
	return xmatrixT


def Fit(dataX, dataY, n):

	xmatrix = XMatrix(n, dataX)
	xmatrixT = XMatrixT(xmatrix)
	#print (xmatrix)
	#print (xmatrixT)

	xtx = MatrixMultiplication(xmatrixT, xmatrix)
	inv = inverse(xtx)
	theta = MatrixMultiplication(inv, xmatrixT)
	theta = MatrixMultiplication(theta, dataY)
	j=0
	for i in theta:
		print ("x_",j, " = ", i)
		j = j + 1
	return theta