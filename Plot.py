#!usr/bin/env python

from Main import Fit
import pylab
import numpy
import csv

def CheckDataStructures(dataX, dataY, n):
	if( len(dataX) != len(dataY) ):
		print("Data structure is not correct")
		return False
	elif(n > len(dataX) ):
		print("Too many fitting parameters")
		return False
	else:
		return True

file = open('data.dat', 'r')
dataX = []
dataY = []
with file as f:
     for line in f:
         x, y = line.split()
         dataX.append(int(x))
         dataY.append([int(y)])
file.close()

Situation = True
while(Situation):
	val = input("Enter a order of function: ")
	try:
		n = int(val)
		Situation = False
	except ValueError:
		print("You didn't input an integer")

if(CheckDataStructures(dataX, dataY, n)):
	x = numpy.linspace(-15,15,1000) # 100 linearly spaced numbers
	zig = Fit(dataX, dataY, n)

	j = 0
	y = 0
	for i in zig:
		y = y + i*x**j
		j = j + 1

	x_limithigh = int(dataX[len(dataX) - 1] * 1.1)+1
	x_limitlow = int(dataX[0] * 0.9)-1

	y_limithigh = int(dataY[len(dataY) - 1][0] * 1.1)+1
	y_limitlow = int(dataY[0][0] * 0.9)-1

	# compose plot
	pylab.axis([x_limitlow, x_limithigh, y_limitlow, y_limithigh])
	pylab.plot(x,y)
	pylab.plot(dataX, dataY, 'ro')
	pylab.show() # show the plot 