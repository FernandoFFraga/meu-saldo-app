# -*- coding: utf-8 -*-

import streamlit as st
from dotenv import load_dotenv

from app.view.categoria_despesa import create as categoria_despesa_create
from app.view.categoria_despesa import list as categoria_despesa_list
from app.view.categoria_despesa import update as categoria_despesa_update
from app.view.categoria_rendimento import create as categoria_rendimento_create
from app.view.categoria_rendimento import list as categoria_rendimento_list
from app.view.categoria_rendimento import update as categoria_rendimento_update
from app.view.dashboard import main
from app.view.lancamento import update as lancamento_update
from app.view.lancamento import create as lancamento_create
from app.view.lancamento import list as lancamento_list

# Carrega variaveis de ambiente
load_dotenv()

st.set_page_config(layout="wide")

# Inicializando session_state
if 'page' not in st.session_state:
    # Criando tabelas
    st.session_state['page'] = 'home'

# Definições do menu
with st.sidebar:
    st.subheader('Dashboard')
    btn_dashboard_inicial = st.button('Inicial', 'btn-7', use_container_width=True)

    st.subheader('Lançamentos')
    btn_lancamentos_insert = st.button('Nova', 'btn-1', use_container_width=True)
    btn_lancamentos_list = st.button('Extrato', 'btn-2', use_container_width=True)

    st.subheader('Categorias Despesas')
    btn_despesas_categorias_insert = st.button('Novo', 'btn-3', use_container_width=True)
    btn_despesas_categorias_list = st.button('Listar', 'btn-4', use_container_width=True)

    st.subheader('Categorias Rendimento')
    btn_rendimento_categorias_insert = st.button('Novo', 'btn-5', use_container_width=True)
    btn_rendimento_categorias_list = st.button('Listar', 'btn-6', use_container_width=True)


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
elif btn_dashboard_inicial:
    st.session_state.page = 'dashboard-inicial'

# Mapeando páginas para suas respectivas views
page_view_map = {
    'despesas-categorias-insert': categoria_despesa_create.show,
    'despesas-categorias-list': categoria_despesa_list.show,
    'despesas-categoria-update': categoria_despesa_update.show,
    'rendimento-categoria-insert': categoria_rendimento_create.show,
    'rendimento-categoria-list': categoria_rendimento_list.show,
    'rendimento-categoria-update': categoria_rendimento_update.show,
    'lancamentos-insert': lancamento_create.show,
    'lancamentos-list': lancamento_list.show,
    'lancamentos-update': lancamento_update.show,
    'dashboard-inicial': main.show,
}

# Carregando view's
page = st.session_state.get('page', '')
view_function = page_view_map.get(page, main.show)
view_function()