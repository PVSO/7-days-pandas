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
    layout='wide',
    initial_sidebar_state='collapsed'
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

col_graf1, col_graf2 = st.columns(2)

df['data_emprestimo'] = pd.to_datetime(df['data_emprestimo'], dayfirst=True, format='ISO8601')

qtd_por_ano = df['data_emprestimo'].value_counts().reset_index()

with col_graf1:
    if not df.empty:

        qtd_por_ano.rename(
            columns={
                'data_emprestimo': 'data',
                'count': 'quantidade'
            },
            inplace=True
        )

        qtd_por_ano_agrupado = qtd_por_ano.groupby(
            by=qtd_por_ano.data.dt.year).sum(numeric_only=True).reset_index()

        qtd_por_ano_agrupado.rename(
            columns={
                'data': 'ano'
            },
            inplace=True
        )

        fig = px.line(
            qtd_por_ano_agrupado,
            x='ano',
            y='quantidade',
            markers=True,
            title='Quantidade total de exemplares emprestados por ano'
        )

        st.plotly_chart(fig, use_container_width=True, key='Gráfico da quantidade total de exemplares emprestados por ano')

    else:
        st.warning('Não foi possível exibir o gráfico de exemplares emprestados por cada ano')

with col_graf2:
    if not df.empty:
        
        qtd_por_mes_agrupado = qtd_por_ano.groupby(
            by=qtd_por_ano.data.dt.month
            ).sum(numeric_only=True).reset_index()

        qtd_por_mes_agrupado.rename(
            columns={
                'data': 'mes'
            },
            inplace=True
        )

        mes_renomear = {
            1: 'jan',
            2: 'fev',
            3: 'mar',
            4: 'abr',
            5: 'mai',
            6: 'jun',
            7: 'jul',
            8: 'ago',
            9: 'set',
            10: 'out',
            11: 'nov',
            12: 'dez',
        }

        qtd_por_mes_agrupado['mes'] = qtd_por_mes_agrupado['mes'].map(mes_renomear)

        # Plote um gráfico de linhas.
        fig = px.line(
            qtd_por_mes_agrupado,
            x='mes',
            y='quantidade',
            markers=True,
            title='Quantidade total de exemplares emprestados por mês'
        )

        st.plotly_chart(fig, use_container_width=True, key='Gráfico da quantidade total de exemplares emprestados por mês')
        st.markdown("**Resumo:**\n")

    else:
        st.warning('Não foi possível exibir o gráfico de exemplares emprestados por cada ano')
