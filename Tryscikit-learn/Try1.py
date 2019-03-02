from sklearn import datasets
import numpy as np
import pandas as pd

iris_data = pd.read_csv('iris_csv.csv', delimiter=',', header=None)
iris_data.tail()
print (iris_data)
Х = iris_data[:,[ 2 , 3 ]]
у= iris_data.target