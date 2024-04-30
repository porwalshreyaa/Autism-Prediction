import pandas as pd

import os
dirname = 'data'
filename = 'autism_screening.csv'
file = os.path.join(dirname, filename)


df = pd.read_csv(file)


for col in df.columns:
    if df[col].isnull().sum() > 0:
        if df[col].dtype == 'float64':
            val = df[col].mean()
            df[col] = df[col].fillna(val)
        else:
            df = df.dropna(subset=df.select_dtypes(include=['object']).columns)

dire = 'ndata'
location = 'autism_screening'
filename = os.path.join(dire, f'{location}.csv')
df.to_csv(filename, index=False)
print(f'Saved data for location {location} to file {filename}')

