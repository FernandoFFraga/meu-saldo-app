from datetime import datetime

import streamlit as st

from app.controller.lancamento_controller import select_lancamentos
import app.controller.lancamento_rendimento_controller as r_controller
import app.controller.lancamento_despesa_controller as d_controller


def show():
    st.title("Extrato")

    col_inpt_1, col_inpt_2 = st.columns((1, 1))

    d_start = col_inpt_1.date_input("Data Inicial", value=datetime.now().replace(day=1), format="DD/MM/YYYY")
    d_end = col_inpt_2.date_input("Data Final", format="DD/MM/YYYY")

    df = select_lancamentos(d_start, d_end)

    df['tipo_icon'] = df['tipo'].map({
        'despesa': '❌',
        'rendimento': '✅'
    })

    event = st.dataframe(df[['tipo_icon', 'descricao', 'valor', 'categoria',  'data_efetiva']],
                         selection_mode="single-row",
                         use_container_width=True,
                         key="data",
                         on_select="rerun",
                         hide_index=True,
                         column_config={
                             "tipo_icon": "Tipo",
                             "descricao": "Descrição",
                             "valor": st.column_config.NumberColumn("Valor", format="R$ %.2f"),
                             "categoria": "Categoria",
                             "data_efetiva": st.column_config.DateColumn("Data Lançamento", format="DD/MM/YYYY")
                            }
                         )

    if event.selection.rows:
        idx = event.selection.rows[0]
        tb_select = df.loc[idx, ['id', 'tipo']]

        col_action_delete, col_action_update = st.columns((1, 1))

        btn_action_delete = col_action_delete.empty()
        trigger_action_delete = btn_action_delete.button('Excluir', f'btn-delete-lancamento', use_container_width=True)

        btn_action_update = col_action_update.empty()
        trigger_action_update = btn_action_update.button('Alterar', f'btn-update-lancamento', use_container_width=True)

        # Trigger botões
        if trigger_action_delete:
            delete_function = r_controller.delete if tb_select.get('tipo') == 'rendimento' else d_controller.delete
            delete_function(int(tb_select.get('id')))

            st.rerun()

        if trigger_action_update:
            st.session_state.page = f'lancamentos-update'

            if f'id_lancamento' not in st.session_state:
                st.session_state[f'id_lancamento'] = ''

            if f'tipo_lancamento' not in st.session_state:
                st.session_state[f'tipo_lancamento'] = ''

            st.session_state.id_lancamento = int(tb_select.get('id'))
            st.session_state.tipo_lancamento = str(tb_select.get('tipo'))

            st.rerun()
