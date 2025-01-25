# -*- coding: utf-8 -*-

import streamlit as st

import app.controller.categoria_despesa_controller as cd_controller
import app.controller.categoria_rendimento_controller as cr_controller
import app.controller.lancamento_despesa_controller as d_controller
import app.controller.lancamento_rendimento_controller as r_controller
from app.model.lancamento_despesa_model import LancamentoDespesa
from app.model.lancamento_rendimento_model import LancamentoRendimento


def show():
    id = st.session_state.id_lancamento
    tipo = st.session_state.tipo_lancamento
    if id == "":
        st.session_state.page = "lancamentos-list"
        st.rerun()

    controller = r_controller if tipo == 'rendimento' else d_controller
    cat_controller = cr_controller if tipo == 'rendimento' else cd_controller
    model = LancamentoRendimento if tipo == 'rendimento' else LancamentoDespesa

    item = controller.select_by_id(id)

    st.title(f"Alterar Lançamento {tipo.capitalize()}")
    with st.form(key="lancamento_update"):
        options_ids, options_names = cat_controller.select_options()

        inpt_tipo_idx = options_ids.index(item.id_categoria)
        inpt_tipo = st.selectbox(label=f"Selecione o tipo de {tipo}:", options=options_names, index=inpt_tipo_idx)
        inpt_desc = st.text_input(label=f"Insira a descrição do {tipo}:", value=item.descricao)
        inpt_vlor = st.number_input(label=f"Insira o valor do {tipo}:", format="%0.2f", min_value=0.0, value=float(item.valor))
        inpt_date = st.date_input(label="Insira a data de lançamento:", format="YYYY-MM-DD", value=item.data_efetiva)

        btn_submit = st.form_submit_button("Alterar", type="primary", use_container_width=True)

        if btn_submit:
            instance = model(
                id=item.id,
                id_categoria=options_ids[options_names.index(inpt_tipo)],
                descricao=inpt_desc,
                valor=inpt_vlor,
                data_efetiva=str(inpt_date)
            )

            controller.update(instance)
            st.toast("Lancamento alterado com sucesso!")

    if st.button("Voltar"):
        st.session_state.page = "lancamentos-list"
        st.rerun()
