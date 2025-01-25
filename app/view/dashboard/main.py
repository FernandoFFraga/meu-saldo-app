import streamlit as st

from app.controller import lancamento_controller


def show():
    st.header('Balanço Mensal', divider='gray')
    col_bal_left, col_bal_midle, col_bal_right = st.columns((1, 1, 1))

    tot_dep, per_dep = lancamento_controller.select_despesas_total_mes()
    tot_ren, per_ren = lancamento_controller.select_rendimento_total_mes()

    col_bal_left.metric('Total Despesas', f'R$ {tot_dep}', f"{per_dep}%")
    col_bal_midle.metric('Total Rendimentos', f'R$ {tot_ren}', f"{per_ren}%")
    col_bal_right.metric('Profit', f'R$ {tot_ren - tot_dep}')

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
