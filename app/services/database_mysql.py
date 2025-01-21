# -*- coding: utf-8 -*-

import os

import pymysql.cursors
from sqlalchemy import create_engine


def get_conn():
    # Cria conexao com o Mysql extraindo informacoes do arquivo .env
    connection = pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        cursorclass=pymysql.cursors.DictCursor
    )

    return connection


def get_engine():
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    dbname = os.getenv("DB_NAME")

    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{dbname}")

    return engine
