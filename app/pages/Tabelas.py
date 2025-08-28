import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pycountry
import streamlit as st


# caminho_base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
caminho_base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
caminho_df = os.path.join(caminho_base, 'data', 'processed', 'emprestimos_exemplares.parquet')
df = pd.read_parquet(caminho_df)

caminho_percentual = os.path.join(caminho_base, 'data', 'processed', 'students_records', 'records_percentual_pos_graduacao.parquet')
df_percentual = pd.read_parquet(caminho_percentual)

st.set_page_config(
    page_title='Dashboard das tabelas dos empréstimos dos acervos do sistema de bibliotecas da UFRN',
    page_icon='📚',
    layout='wide'
)

st.title("🎲 Dashboard de Análise de empréstimos dos acervos do sistema de bibliotecas da UFRN")
st.markdown("Explore as tabelas dos empréstimos dos acervos do sistema de bibliotecas da UFRN.")
st.markdown("---")

if not df_percentual.empty:
    st.header('Diferença percentual de empréstimos dos cursos de Pós-Graduação')
    st.markdown('A tabela apresenta a variação percentual no número de empréstimos durante os anos')
    st.dataframe(df_percentual)
else:
    st.write('Dataframe indisponivel')