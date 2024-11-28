import os
# Función lambda para limpiar la consola
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
clear()
import numpy as np

#SLICES 
a= np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)

print("[:,0] =",a[:,0])
print(a[:,:2])
print("\n")
b = np.array([[4,5,3],[6,3,1],[9,2,3],[3,1,6]])
print(b[2,1:])
print("\n")
print(b[:,:2])

print("\n")

mine = np.arange(56).reshape(7,8)
print(mine)

#Functions
#To see the rows and columns
print("Rows and columns:",mine.shape)
#To see the number of dimensiones
print("Dimensions:",mine.ndim)
#To see th number of elements in the matrix
print("Number of elements:",mine.size)
print("\n")

zero = np.zeros((3,4))
print(zero)

##Generating a sequence
c = np.linspace(30,10,15)
print(c)

##Generating a 3d array
##Reshape(a,b,c) => a: # of matrixes, b:# of rows, c:# of columns
print("\n3Dimension Array")
Matriz3Dimensiones = np.arange(30).reshape(3,5,2)
print(Matriz3Dimensiones)