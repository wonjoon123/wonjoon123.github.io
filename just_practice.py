import pandas as pd

name = ['a','b','c','d','e']
births = [1,2,3,4,5]

babydataset = list(zip(name,births))
print(babydataset)

df = pd.DataFrame(babydataset,columns=['name','birth'])
print(df)
