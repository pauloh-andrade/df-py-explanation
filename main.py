import pandas as pd

df = pd.read_excel('precos.xlsx')

df.head(10)

list = df['Tipo'].unique()

df_escola = df.query("Tipo=='Escola'")[["Tipo", "produto marca", "Preço"]]

media = df_escola.groupby(['Tipo', 'produto marca']).mean()

print(media)