import pandas as pd

import os
dirname = 'data'
filename = 'autism_screening.csv'
file = os.path.join(dirname, filename)


df = pd.read_csv(file)

df = df.replace({'yes':1, 'no':0, '?':'Others', 'others':'Others', 'YES':1, 'NO':0})
for col in df.columns:
    if df[col].isnull().sum() > 0:
        if df[col].dtype == 'float64':
            val = df[col].mean()
            df[col] = df[col].fillna(val)
        else:
            df = df.dropna(subset=df.select_dtypes(include=['object']).columns)
df.drop(df[df['age']>100].index, inplace=True)
df.drop(df[df['age']<=0].index, inplace=True)
dire = 'ndata'
name = 'autism_screening'
filename = os.path.join(dire, f'{name}.csv')
df.to_csv(filename, index=False)
print(f'Saved data for location {name} to file {filename}')

