# data structures in Data Science

# python data structures
# vector

# vector as a row using np.array
import numpy as np

vector_row = np.array([1, 2, 3])
print(vector_row, "\n", "A vector as a row using np.array")

# vector as a column using np.array
vector_column = np.array([[1],
                          [2],
                          [3]])
print(vector_column, "\n", "A vector as a column using np.array")

# matrix using np.mat
matrix = np.mat([[1, 2],
                 [1, 2],
                 [1, 2]])
print(matrix, "\n", "A matrix using np.mat")

# array are multidimensional using data structures
# arrays are created using square brackets
# arrays are mutable which means they can be changed
# arrays can contain any data type

cars = ["bmw", "honda", "toyota", "ford"]
print(cars, "\n", "A list of cars")

import pandas as pd

# series are one-dimensional labeled array capable of holding any data type
# create a series using the array function
a = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(a)
print(s)

# data frames are two-dimensional labeled data structures with columns of potentially different types
# create a data frame using the array function
cars = {'Brand': ['Honda Civic', 'Toyota Corolla', 'Ford Focus', 'Audi A4'],
        'Price': [22000, 25000, 27000, 35000]
        }
df = pd.DataFrame(cars, columns=['Brand', 'Price'])
print(df)

# Lists are mutable which means they can be changed
# Lists can contain any data type
names = ["David", "John", "Michael", "James", (21, 32, 11), True, 51.23]
print(names, "\n", "A list of names with different data types")
