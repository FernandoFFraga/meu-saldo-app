# -*- coding: utf-8 -*-
import uuid

import streamlit as st

import app.controller.lancamento_rendimento_controller as controller_lancamento_rendimento
import app.controller.lancamento_despesa_controller as controller_lancamento_despesa
import app.controller.categoria_rendimento_controller as controller_categoria_rendimento
import app.controller.categoria_despesa_controller as controller_categoria_despesa
from app.model.lancamento_despesa_model import LancamentoDespesa
from app.model.lancamento_rendimento_model import LancamentoRendimento


def show():
    st.title("Lançamentos")

    col_despesa, col_rendimento = st.columns((1, 1))

    btn_despesa = col_despesa.empty()
    tggr_despesa = btn_despesa.button('Despesas', f'btn-lancamento-depesas-mode', use_container_width=True)

    btn_rendimento = col_rendimento.empty()
    tggr_rendimento = btn_rendimento.button('Rendimento', f'btn-lancamento-rendimento-mode', use_container_width=True)

    if 'lancamento' not in st.session_state:
        st.session_state['lancamento'] = 'despesa'

    if tggr_rendimento:
        st.session_state.lancamento = 'rendimento'

    if tggr_despesa:
        st.session_state.lancamento = 'despesa'

    st.info(f'Selecionado: {st.session_state.lancamento.capitalize()}')

    if st.session_state.lancamento == 'rendimento':
        form_rendimento()
    else:
        form_despesa()


def form_rendimento():
    options_ids, options_names = controller_categoria_rendimento.select_options()

    with st.form(key="novo_lancamento_rendimento"):
        inpt_tipo = st.selectbox(label="Selecione o tipo de redimento:", options=options_names)
        inpt_desc = st.text_input(label="Insira a descrição do rendimento:")
        inpt_vlor = st.number_input(label="Insira o valor do rendimento:", format="%0.2f", min_value=0.0)
        inpt_date = st.date_input(label="Insira a data de lançamento:", format="YYYY-MM-DD")
        inpt_month = st.number_input(label="Insira a quantidade de meses na recorrência: ", min_value=1)

        btn_submit = st.form_submit_button("Criar", type="primary", use_container_width=True)

        if btn_submit:
            instance = LancamentoRendimento(
                id_categoria=options_ids[options_names.index(inpt_tipo)],
                descricao=inpt_desc,
                valor=inpt_vlor,
                uuid_sequencia=uuid.uuid4(),
                data_efetiva=str(inpt_date)
            )

            if inpt_month > 1:
                controller_lancamento_rendimento.insert_many(instance, inpt_month)
            else:
                controller_lancamento_rendimento.insert(instance)

            st.toast("Lançamento inserido com sucesso!")


def form_despesa():
    options_ids, options_names = controller_categoria_despesa.select_options()

    with st.form(key="novo_lancamento_despesa"):
        inpt_tipo = st.selectbox(label="Selecione o tipo de despesa:", options=options_names)
        inpt_desc = st.text_input(label="Insira a descrição do despesa:")
        inpt_vlor = st.number_input(label="Insira o valor do despesa:", format="%0.2f", min_value=0.0)
        inpt_date = st.date_input(label="Insira a data de lançamento:", format="YYYY-MM-DD")
        inpt_month = st.number_input(label="Insira a quantidade de meses na recorrência: ", min_value=1)

        btn_submit = st.form_submit_button("Criar", type="primary", use_container_width=True)

        if btn_submit:
            instance = LancamentoDespesa(
                id_categoria=options_ids[options_names.index(inpt_tipo)],
                descricao=inpt_desc,
                valor=inpt_vlor,
                uuid_sequencia=uuid.uuid4(),
                data_efetiva=str(inpt_date)
            )

            if inpt_month > 1:
                controller_lancamento_despesa.insert_many(instance, inpt_month)
            else:
                controller_lancamento_despesa.insert(instance)

            st.toast("Lançamento inserido com sucesso!")
