# -*- coding: utf-8 -*-

import streamlit as st
import app.controller.categoria_rendimento_controller as controller
from app.model.categoria_rendimento_model import CategoriaRendimento


def show():
    id = st.session_state.id_categoria_rendimento
    if id == "":
        st.session_state.page = "rendimento-categoria-list"
        st.rerun()

    item = controller.select_by_id(id)

    st.title("Alterar Categoria Rendimento")
    with st.form(key="categoria_rendimento_update"):
        inpt_name = st.text_input(label="Insira o nome da categoria: ", value=item.nome)
        btn_submit = st.form_submit_button("Alterar", type="primary", use_container_width=True)

        if btn_submit:
            instance = CategoriaRendimento(id=item.id, nome=inpt_name)
            controller.update(instance)
            st.success("Categoria alterada com sucesso!")

    if st.button("Voltar"):
        st.session_state.page = "rendimento-categoria-list"
        st.rerun()
