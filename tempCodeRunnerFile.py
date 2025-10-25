import numpy as np
import pandas as pd

data = pd.read_csv("Iris.csv")
n = 5
print(data.head(n))  # use to give data from the top & n represents the number of records
print(data.tail(n))  # use to give data from the bottom & n represents the number of records
print(data.describe())  # use to give the statistical data
arr1=np.array([[1, 2, 3], [4, 5, 6]])
print(arr1)
arr2=np.array([[7, 8, 9], [10, 11, 12]])
print(arr2)
print(arr1+arr2)    
dd=pd.DataFrame(data)
print(dd)
ds=pd.Series(data['Species'])
print(ds)