import streamlit as st
from babel.numbers import format_currency

from app.controller import lancamento_controller


def formatValue(n):
    return format_currency(n, '', locale='pt_BR')


def show():
    st.header('Balanço Mensal', divider='gray')
    col_bal_01, col_bal_02, col_bal_03, col_bal_04 = st.columns((1, 1, 1, 1))

    tot_dep, per_dep = lancamento_controller.select_despesas_total_mes()
    tot_ren, per_ren = lancamento_controller.select_rendimento_total_mes()
    saldo = lancamento_controller.select_saldo()

    col_bal_01.metric('Total Despesas', f'R$ {formatValue(tot_dep)}', f"{per_dep}%")
    col_bal_02.metric('Total Rendimentos', f'R$ {formatValue(tot_ren)}', f"{per_ren}%")
    col_bal_03.metric('Profit', f'R$ {formatValue(tot_ren - tot_dep)}')
    col_bal_04.metric('Saldo', f'R$ {formatValue(saldo)}')

    col_left, col_right = st.columns((1, 1))

    with col_left:
        st.header('Despesas Planejadas', divider='gray')
        df_despesas_sumarizadas = lancamento_controller.select_despesas_sumarizadas()

        for index, row in df_despesas_sumarizadas.iterrows():
            st.progress(row['porcentagem'],
                        text=f'{row['nome'].capitalize()} ({row['total']} de {row['limite_mensal']})')

    with col_right:
        st.header('Despesas Diárias', divider='gray')
        df_despesas_diarias = lancamento_controller.select_despesas_diarias_mes()

        st.line_chart(df_despesas_diarias, x='dia', y='total')
