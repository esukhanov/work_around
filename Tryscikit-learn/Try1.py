from sklearn import datasets
import numpy as np
import pandas as pd
from sklearn .datasets import load_iris

iris_data = load_iris()

print (iris_data)
Х = iris_data.data[:,[ 2 , 3 ]]
у= iris_data.target

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test  = train_test_split(Х , у , test_size=0.3, random_state=0)
from sklearn .preprocessing import StandardScaler
sc = StandardScaler()
sc.fit (X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)