# -*- coding: utf-8 -*-
import uuid

import streamlit as st
from dotenv import load_dotenv

from app.controller.lancamento_rendimento_controller import insert, insert_many
from app.model.lancamento_rendimento_model import LancamentoRendimento
from app.view.categoria_despesa import create as categoria_despesa_create
from app.view.categoria_despesa import list as categoria_despesa_list
from app.view.categoria_despesa import update as categoria_despesa_update
from app.view.categoria_rendimento import create as categoria_rendimento_create
from app.view.categoria_rendimento import list as categoria_rendimento_list
from app.view.categoria_rendimento import update as categoria_rendimento_update
from app.view.lancamento import create as lancamento_create

# Carrega variaveis de ambiente
load_dotenv()

st.set_page_config(layout="wide")

# Inicializando session_state
if 'page' not in st.session_state:
    # Criando tabelas
    st.session_state['page'] = 'home'

# Definições do menu
with st.sidebar:
    st.subheader('Lançamentos')
    btn_lancamentos_insert = st.button('Nova', 'lancamentos-insert', use_container_width=True)
    btn_lancamentos_list = st.button('Buscar', 'lancamentos-list', use_container_width=True)

    st.subheader('Categorias Rendimento')
    btn_despesas_categorias_insert = st.button('Novo', 'despesas-categorias-insert', use_container_width=True)
    btn_despesas_categorias_list = st.button('Listar', 'despesas-categorias-list', use_container_width=True)

    st.subheader('Categorias Rendimento')
    btn_rendimento_categorias_insert = st.button('Novo', 'rendimento-categoria-insert', use_container_width=True)
    btn_rendimento_categorias_list = st.button('Listar', 'rendimento-categoria-list', use_container_width=True)


# Definindo página
if btn_despesas_categorias_insert:
    st.session_state.page = 'despesas-categorias-insert'
elif btn_despesas_categorias_list:
    st.session_state.page = 'despesas-categorias-list'
elif btn_rendimento_categorias_insert:
    st.session_state.page = 'rendimento-categoria-insert'
elif btn_rendimento_categorias_list:
    st.session_state.page = 'rendimento-categoria-list'
elif btn_lancamentos_insert:
    st.session_state.page = 'lancamentos-insert'
elif btn_lancamentos_list:
    st.session_state.page = 'lancamentos-list'

# Carregando view's
page = st.session_state.page
if page == 'despesas-categorias-insert':
    categoria_despesa_create.show()
elif page == 'despesas-categorias-list':
    categoria_despesa_list.show()
elif page == 'despesas-categoria-update':
    categoria_despesa_update.show()
elif page == 'rendimento-categoria-insert':
    categoria_rendimento_create.show()
elif page == 'rendimento-categoria-list':
    categoria_rendimento_list.show()
elif page == 'rendimento-categoria-update':
    categoria_rendimento_update.show()
elif page == 'lancamentos-insert':
    lancamento_create.show()
elif page == 'lancamentos-list':
    lancamento_create.show()
else:
    st.title('Meu Saldo')
