import app.services.database_mysql as db
from app.constants.table_constants import TB_CAT_DEP as TBNAME
from app.model.categoria_despesa_model import CategoriaDespesa
import pandas as pd


def insert(instance: CategoriaDespesa):
    conn = db.get_conn()

    with conn.cursor() as cursor:
        cursor.execute(f"""
            INSERT INTO {TBNAME} (nome, limite_mensal, data_criacao) VALUES (%s, %s, now())
        """, (instance.nome, instance.limite_mensal))

    conn.commit()


def update(instance: CategoriaDespesa):
    conn = db.get_conn()

    with conn.cursor() as cursor:
        cursor.execute(f"""
            UPDATE {TBNAME} set nome = %s, limite_mensal = %s WHERE id = %s
        """, (instance.nome, instance.limite_mensal, instance.id))

    conn.commit()


def delete(id: int):
    conn = db.get_conn()

    with conn.cursor() as cursor:
        cursor.execute(f"""DELETE FROM {TBNAME}  WHERE id = %s""", id)

    conn.commit()


def select_by_id(id: int):
    conn = db.get_conn()

    with conn.cursor() as cursor:
        cursor.execute(f"""SELECT id, nome, limite_mensal FROM {TBNAME} WHERE id = %s LIMIT 1""", id)
        return CategoriaDespesa().set(cursor.fetchone())


def select_all():
    query = f"SELECT id, nome, limite_mensal FROM {TBNAME} ORDER BY nome ASC LIMIT 100"
    df = pd.read_sql(query, con=db.get_engine())

    return df