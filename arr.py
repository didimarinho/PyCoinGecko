# import pandas as pd

# frame = pd.DataFrame({
#     'a': [1, 2, 3],
#     'b': [4, 5, 6],
#     'c': [7, 8, 9]
# })

# print(frame)

# print('\n')

# frame['d'] = frame['a'].apply(lambda x: x * 2)

# print(frame)

import pandas as pd
import numpy as np
print('\n')

t = ('#?##########################################################')

df = pd.DataFrame([[10, 20, 30], 
                  [40, 50, 60], 
                  [70, 80, 90], 
                  [100,110,120]], 
                 columns=['Col_A', 'Col_B', 
                          'Col_C']) 

#! printamos o data frame
print(df,'\n')
print(t,'\n')


#! usamos as funções sum e min em cada coluna
df2 = df.agg(['sum', 'min'])
print(df2,'\n')
print(t,'\n')


#! usamos novamente cada função em cada coluna
df3 = df.agg(['sum','mean', 'max'])
print(df3,'\n')
print(t,'\n')


#! aplicamos as funções diretamente por dicionário em cada coluna
#! podemos ver que as funções que não forma aplicadas ficaram NaN
df4 = df.agg({'Col_A' : ['sum', 'min'], 
        'Col_B' : ['min', 'max'], 
        'Col_C' : ['sum', 'mean']})

print(df4,'\n')
print(t,'\n')


#! selecionamos a coluna por eixo 
df5 = df.agg('mean', axis= 1) 
print(df5,'\n')
print(t,'\n')