import app.services.database_mysql as db
from app.constants.table_constants import TB_CAT_REN as TBNAME
from app.model.categoria_rendimento_model import CategoriaRendimento
import pandas as pd


def insert(instance: CategoriaRendimento):
    conn = db.get_conn()

    with conn.cursor() as cursor:
        cursor.execute(f"""
            INSERT INTO {TBNAME} (nome, data_criacao) VALUES (%s, now())
        """, (instance.nome))

    conn.commit()


def update(instance: CategoriaRendimento):
    conn = db.get_conn()

    with conn.cursor() as cursor:
        cursor.execute(f"""
            UPDATE {TBNAME} set nome = %s WHERE id = %s
        """, (instance.nome, instance.id))

    conn.commit()


def delete(id: int):
    conn = db.get_conn()

    with conn.cursor() as cursor:
        cursor.execute(f"""DELETE FROM {TBNAME} WHERE id = %s""", id)

    conn.commit()


def select_by_id(id: int):
    conn = db.get_conn()

    with conn.cursor() as cursor:
        cursor.execute(f"""SELECT id, nome FROM {TBNAME} WHERE id = %s LIMIT 1""", id)
        return CategoriaRendimento().set(cursor.fetchone())


def select_all():
    query = f"SELECT id, nome FROM {TBNAME} ORDER BY nome ASC LIMIT 100"
    df = pd.read_sql(query, con=db.get_engine())

    return df


def select_options():
    df = select_all()

    return df['id'].tolist(), df['nome'].tolist()
