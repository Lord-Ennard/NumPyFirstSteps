import array as arreglo
import numpy as np
#To declare an array you must place the data type before the array itself
#For integers it is 'i', for decimals it is 'd'
matriz = arreglo.array('i',[1,2,3])

## A list is a collection of data
lista = [1,2,3]
print(lista)

##An array is a data structure, each number occupies a space in memory
nuevaMatriz = np.array([1,2,3])
print(nuevaMatriz)

##The good thing about numpy is that you don't have to declare the data type of your array

##Adding values

lista.append(8)
nuevaMatriz = nuevaMatriz + np.array([8])
print(lista)
print(nuevaMatriz)

print("\n")

##With lists you cannot perform mathematical operations
a = [1,2,3]
b = [4,5,6]
print(a+b)

##On the other hand, You can perform mathematical operations with arrays
x = np.array([1,2,3])
y = np.array([4,5,6])
print(x*y)
print(x+y)

print("\n")
##A 2 Dimension array declared
m = np.array([[10,20,30],[40,50,60]])
print(m)
print("\n")
m1 = np.array(a)
print(m1)

##Inserting a list into a matrix
a1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 = np.array(a1)
print(m2)

##Generating a new matrix
print("\n")
##arange(19), the number indicates the cuantity of elements in the matrix
##reshape(2,5) the first parameter indicates the number of rows, whereas the second
# parameter indicates the number of columns
generated = np.arange(10).reshape(2,5)
print(generated)
