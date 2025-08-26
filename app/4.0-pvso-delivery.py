import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pycountry
import streamlit as st

caminho_base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
caminho_arquivo = os.path.join(caminho_base, 'data', 'processed', 'emprestimos_exemplares.parquet')
df = pd.read_parquet(caminho_arquivo)

caminho_percentual = os.path.join(caminho_base, 'data', 'processed', 'students_records', 'records_percentual_pos_graduacao.parquet')
df_percentual = pd.read_parquet(caminho_percentual)

st.set_page_config(
    page_title='Dashboard dos empréstimos dos acervos do sistema de bibliotecas da UFRN',
    page_icon='📚',
    layout='wide'
)

st.title("🎲 Dashboard de Análise de empréstimos dos acervos do sistema de bibliotecas da UFRN")
st.markdown("Explore os empréstimos dos acervos do sistema de bibliotecas da UFRN.")

st.markdown('---')

def gerar_tabela_frequencia(campo):
    df_tabela = pd.DataFrame(df[campo].value_counts().reset_index())

    df_tabela.rename(
        columns={
            'count':'quantidade'
        },
        inplace=True
    )

    df_tabela['porcentagem'] = round((df_tabela['quantidade'] / df_tabela['quantidade'].sum())*100, 10)

    return df_tabela.loc[df_tabela['quantidade'].idxmax(), campo]

st.subheader('Métricas gerais')

if not df.empty:
    colecao = gerar_tabela_frequencia('colecao')
    usuario = gerar_tabela_frequencia('tipo_vinculo_usuario')
    biblioteca = gerar_tabela_frequencia('biblioteca')
    tema = gerar_tabela_frequencia('CDU')
    total_registros = df.shape[0]
else:
    colecao, usuario, biblioteca, tema, total_registros = '', '', '', ''

col1, col2, col3 = st.columns(3)
col1.metric("Total de registros", f"{total_registros}")
col2.metric("Tipo de vinculo de usuário que mais usa o arcevo", f"{usuario}")
col3.metric("Coleção mais frequente", f"{colecao}")

col4, col5 = st.columns(2)
col4.metric("Biblioteca com maior arcevo", f"{biblioteca}")
col5.metric("Tema mais emprestado", tema)

st.markdown('---')

if not df_percentual.empty:
    st.header('Diferença percentual de empréstimos dos cursos de Pós-Graduação')
    st.markdown('A tabela apresenta a variação percentual no número de empréstimos durante os anos')
    st.dataframe(df_percentual)
else:
    st.write('Dataframe indisponivel')
