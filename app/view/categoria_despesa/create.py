# -*- coding: utf-8 -*-

import streamlit as st

from app.model.categoria_despesa_model import CategoriaDespesa
import app.controller.categoria_despesa_controller as controller


def show():
    st.title("Nova Categoria de Despesa")
    with st.form(key="cateogria_despesa_insert"):
        inpt_name = st.text_input(label="Insira o nome da categoria: ")
        inpt_limit = st.number_input(label="Insira o limite mensal: ")
        btn_submit = st.form_submit_button("Criar", type="primary", use_container_width=True)

        if btn_submit:
            instance = CategoriaDespesa(nome=inpt_name, limite_mensal=inpt_limit)
            controller.insert(instance)

            st.toast("Categoria incluída com sucesso!")

