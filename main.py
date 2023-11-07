import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('precos.xlsx')

df.head(10)

list = df['Tipo'].unique()

df_escola = df.query("Tipo=='Escola'")[["Tipo", "produto_marca", "Preço"]]

media = df_escola.groupby(['Tipo', 'produto_marca']).agg({'Preço': ['mean', 'min', 'max', 'count']})

print(media)

esfiha = df.query("produto_marca=='Esfiha '")[['Estabelecimento', 'Preço']]

print(esfiha)

plt.figure()
plt.bar(esfiha['Estabelecimento'], esfiha['Preço'], color='maroon')
plt.show()
