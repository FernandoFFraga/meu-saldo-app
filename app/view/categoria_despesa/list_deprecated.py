# -*- coding: utf-8 -*-

import streamlit as st
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, ColumnsAutoSizeMode

import app.controller.categoria_despesa_controller as controller


def show():
    st.title("Listagem de categorias de despesas")
    df = controller.select_all()
    gb = GridOptionsBuilder.from_dataframe(df)

    # configure selection
    gb.configure_selection(selection_mode="single", use_checkbox=True)
    gb.configure_side_bar()
    gb.configure_column("id", filter='agTextColumnFilter')
    gb.configure_column("nome", filter='agTextColumnFilter')
    gb.configure_column("limite_mensal", filter='agTextColumnFilter')
    gridOptions = gb.build()

    data = AgGrid(df,
                  gridOptions=gridOptions,
                  enable_enterprise_modules=True,
                  allow_unsafe_jscode=True,
                  update_mode=GridUpdateMode.SELECTION_CHANGED,
                  columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS,
                  fit_columns_on_grid_load=True)

    row = data['selected_rows']

    if row is not None:

        col_action_delete, col_action_update = st.columns((1, 1))

        btn_action_delete = col_action_delete.empty()
        trigger_action_delete = btn_action_delete.button(
            'Excluir', f'btn-delete-categoria-despesa-{row.get('id').iloc[0]}'
        )

        btn_action_update = col_action_update.empty()
        trigger_action_update = btn_action_update.button(
            'Alterar', f'btn-update-categoria-despesa-{row.get('id').iloc[0]}'
        )

        # Trigger botões
        if trigger_action_delete:
            controller.delete(int(row.get('id').iloc[0]))
            st.rerun()

        if trigger_action_update:
            st.session_state.page = 'd-update'

            if 'id_categoria_despesa' not in st.session_state:
                st.session_state['id_categoria_despesa'] = ''

            st.session_state.id_categoria_despesa = int(row.get('id').iloc[0])
            st.rerun()
