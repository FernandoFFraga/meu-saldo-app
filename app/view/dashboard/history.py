import streamlit as st
from babel.numbers import format_currency

from app.controller import lancamento_controller



def show():
    st.header('Custos por Categoria', divider='gray')
    df_lancamento_futuro = lancamento_controller.select_categorias_por_mes()
    st.bar_chart(df_lancamento_futuro, y="valor", x="mes", color="tipo", stack=False)
