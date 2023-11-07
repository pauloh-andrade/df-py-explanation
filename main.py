import pandas as pd

df = pd.read_excel('precos.xlsx')

df.head(10)

list = df['Tipo'].unique()

print(list)