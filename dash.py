import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(layout="wide")

file_path = 'casecsv.csv'

st.title("Case AEVO")
st.write("")

df = pd.read_csv(file_path)

## Taxa de conclusão

total_atividades = df.groupby('Responsável').size()
concluidas = df[df['Status'] == 'Concluída'].groupby('Responsável').size()

taxa_conclusao = (concluidas / total_atividades * 100).fillna(0).reset_index()
taxa_conclusao.columns = ['Responsável', 'Taxa de Conclusão (%)']

## Grafico de barras

fig_conclusao = px.bar(taxa_conclusao,
                       x='Responsável',
                       y='Taxa de Conclusão (%)',
                       title='Taxa de Conclusão por Colaborador',
                       text='Taxa de Conclusão (%)',
                       template='plotly_white')

fig_conclusao.update_traces(
    marker_color='#1f77b4',
    texttemplate='%{text:.1f}%',
    textposition='outside'
)

fig_conclusao.update_layout(
    yaxis_title='Taxa de Conclusão (%)',
    xaxis_title='Responsável',
    yaxis_range=[0,105],
    uniformtext_minsize=8,
    uniformtext_mode='hide',
    title_font_size=18,
    height=450  
)

## Atividades por colaborador

quant_atividades = df.groupby('Responsável').size().reset_index(name='Quantidade de Atividades')

## Gráfico de dispersão

fig_disp = px.line(quant_atividades,
                   x='Responsável',
                   y='Quantidade de Atividades',
                   title='Atividades por Colaborador',
                   text='Quantidade de Atividades',
                   markers=True,
                   template='plotly_white',
                   color_discrete_sequence=['#1f77b4'])

fig_disp.update_traces(
    texttemplate='%{text}',
    textposition='top center'
)

fig_disp.update_layout(
    yaxis_title='Quantidade de Atividades',
    xaxis_title='Responsável',
    uniformtext_minsize=8,
    uniformtext_mode='hide',
    title_font_size=18,
    height=450  
)

## Definição do layout

col1, col2 = st.columns(2, gap="medium") 

with col1:
    st.subheader("Taxa de Conclusão por Colaborador")
    st.plotly_chart(fig_conclusao, use_container_width=True)

with col2:
    st.subheader("Atividades por Colaborador")
    st.plotly_chart(fig_disp, use_container_width=True)