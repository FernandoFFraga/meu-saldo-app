# -*- coding: utf-8 -*-

import streamlit as st
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, ColumnsAutoSizeMode

import app.controller.categoria_despesa_controller as controller


def show():
    st.title("Categorias de Despesas")
    df = controller.select_all()

    event = st.dataframe(df,
                         selection_mode="single-row",
                         use_container_width=True,
                         key="data",
                         on_select="rerun",
                         hide_index=True,
                         column_config={
                             "nome": "Nome",
                             "limite_mensal": st.column_config.NumberColumn("Limite Mensal", format="R$ %d")
                         }
                         )

    if event.selection.rows:
        idx = event.selection.rows[0]
        tb_id = df.loc[idx, 'id']

        col_action_delete, col_action_update = st.columns((1, 1))

        btn_action_delete = col_action_delete.empty()
        trigger_action_delete = btn_action_delete.button(
            'Excluir', f'btn-delete-categoria-despesa-{tb_id}', use_container_width=True
        )

        btn_action_update = col_action_update.empty()
        trigger_action_update = btn_action_update.button(
            'Alterar', f'btn-update-categoria-despesa-{tb_id}', use_container_width=True
        )

        # Trigger botões
        if trigger_action_delete:
            controller.delete(int(tb_id))
            st.rerun()

        if trigger_action_update:
            st.session_state.page = 'd-update'

            if 'id_categoria_despesa' not in st.session_state:
                st.session_state['id_categoria_despesa'] = ''

            st.session_state.id_categoria_despesa = int(tb_id)
            st.rerun()
