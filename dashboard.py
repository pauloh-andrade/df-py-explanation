import pandas as pd
import streamlit as st

df = pd.read_excel('precos.xlsx')

st.set_page_config(layout='wide')
st.title('Estatísticas de preços')

(col1, col2) = st.columns(2)

with col1:
    lista = df['Tipo'].unique()
    tipo = st.selectbox('Tipo', lista)

    df_tipo = df.query(f"Tipo=='{tipo}'")

    df_tipo[['Coleta', 'Tipo', 'Semana', 'Estabelecimento', 'produto_marca', 'Preço']]

with col2:
    