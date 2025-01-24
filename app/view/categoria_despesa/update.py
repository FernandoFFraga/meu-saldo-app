# -*- coding: utf-8 -*-

import streamlit as st
import app.controller.categoria_despesa_controller as controller
from app.model.categoria_despesa_model import CategoriaDespesa


def show():
    id = st.session_state.id_categoria_despesa
    if id == "":
        st.session_state.page = "despesas-categorias-list"
        st.rerun()

    item = controller.select_by_id(id)

    st.title("Alterar Categoria Despesa")
    with st.form(key="categoria_despesa_update"):
        inpt_name = st.text_input(label="Insira o nome da categoria: ", value=item.nome)
        inpt_limit = st.number_input(label="Insira o limite mensal: ", value=float(item.limite_mensal))
        btn_submit = st.form_submit_button("Alterar", type="primary", use_container_width=True)

        if btn_submit:
            instance = CategoriaDespesa(id=item.id, nome=inpt_name, limite_mensal=inpt_limit)
            controller.update(instance)
            st.success("Categoria alterada com sucesso!")

    if st.button("Voltar"):
        st.session_state.page = "despesas-categorias-list"
        st.rerun()
