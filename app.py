# -*- coding: utf-8 -*-
import streamlit as st
from dotenv import load_dotenv

from app.view.categoria_despesa import create as categoria_despesa_create
from app.view.categoria_despesa import list as categoria_despesa_list
from app.view.categoria_despesa import update as categoria_despesa_update

# Carrega variaveis de ambiente
load_dotenv()

st.set_page_config(layout="wide")

# Inicializando session_state
if 'page' not in st.session_state:
    # Criando tabelas
    st.session_state['page'] = 'home'

# Definições do menu
with st.sidebar:
    st.subheader('Tipos Despesas')
    btn_d_insert = st.button('Novo', 'd-insert', use_container_width=True)
    btn_d_list = st.button('Listar', 'd-list', use_container_width=True)

    st.subheader('Tipos Rendimento')
    btn_r_insert = st.button('Novo', 'r-insert', use_container_width=True)
    btn_r_list = st.button('Listar', 'r-list', use_container_width=True)

    st.subheader('Lançamentos')
    btn_l_insert = st.button('Novo', 'l-insert', use_container_width=True)
    btn_l_list = st.button('Listar', 'l-list', use_container_width=True)

# Definindo página
if btn_d_insert:
    st.session_state.page = 'd-insert'
elif btn_d_list:
    st.session_state.page = 'd-list'


# Carregando view's
page = st.session_state.page
if page == 'd-insert':
    categoria_despesa_create.show()
elif page == 'd-list':
    categoria_despesa_list.show()
elif page == 'd-update':
    categoria_despesa_update.show()
else:
    st.title('Meu Saldo')