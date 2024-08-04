import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


values = [[1,2,3],[4,5,6],[7,8,9]]
index = ['one','two','three']
colums = ['A','B','C']
df = pd.DataFrame(values,index, colums)
print(df)

print(len(np.array([0,1,2,3,4,5]).shape))
print(np.arange(6).reshape((2,3)).shape)
print(tuple((1,)))

plt.title('test')
plt.plot([1,2,3,4],[2,4,6,8])
plt.show()