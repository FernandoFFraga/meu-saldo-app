# -*- coding: utf-8 -*-

import streamlit as st

from app.model.categoria_rendimento_model import CategoriaRendimento
import app.controller.categoria_rendimento_controller as controller


def show():
    st.title("Nova Categoria de Rendimento")
    with st.form(key="cateogria_rendimento_insert"):
        inpt_name = st.text_input(label="Insira o nome da categoria: ")
        btn_submit = st.form_submit_button("Criar", type="primary", use_container_width=True)

        if btn_submit:
            instance = CategoriaRendimento(nome=inpt_name)
            controller.insert(instance)

            st.toast("Categoria incluída com sucesso!")

