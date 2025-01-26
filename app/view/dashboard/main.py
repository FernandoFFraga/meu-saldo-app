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

    st.header('Visão Geral', divider='gray')
    df_lancamento_futuro = lancamento_controller.select_lancamento_futuros_df()
    st.bar_chart(df_lancamento_futuro, y="valor", x="mes", color="tipo", stack=False)

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



    st.header('Lançamentos Futuros', divider='gray')
    col_fut_01, col_fut_02 = st.columns((1, 1))

    tot_fut_dep, tot_fut_ren = lancamento_controller.select_lancamentos_futuros()

    col_fut_01.metric('Despesas', f'R$ {formatValue(tot_fut_dep)}')
    col_fut_02.metric('Rendimentos', f'R$ {formatValue(tot_fut_ren)}')



