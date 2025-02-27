from datetime import datetime

from dateutil.relativedelta import relativedelta

import app.services.database_mysql as db
from app.constants.table_constants import TB_LAC_DEP as TBNAME
from app.model.lancamento_despesa_model import LancamentoDespesa


def insert(item: LancamentoDespesa):
    conn = db.get_conn()

    with conn.cursor() as cursor:
        cursor.execute(f"""
            INSERT INTO {TBNAME} (id_categoria, descricao, valor, uuid_sequencia, data_efetiva, data_inclusao) 
            VALUES (%s, %s, %s, %s, %s, now())
        """, (item.id_categoria, item.descricao, item.valor, item.uuid_sequencia, item.data_efetiva))

    conn.commit()


def insert_many(item: LancamentoDespesa, count: int):
    start_date = datetime.strptime(item.data_efetiva, "%Y-%m-%d")
    list_date = [start_date + relativedelta(months=i) for i in range(count)]
    descricao_default = item.descricao

    for idx, date in enumerate(list_date, start=1):
        handle = item

        handle.descricao = f"{descricao_default} ({idx}/{count})"
        handle.data_efetiva = date.strftime("%Y-%m-%d")

        insert(handle)


def delete(id: int):
    conn = db.get_conn()

    with conn.cursor() as cursor:
        cursor.execute(f"""DELETE FROM {TBNAME} WHERE id = %s""", id)

    conn.commit()


def select_by_id(id: int):
    conn = db.get_conn()

    with conn.cursor() as cursor:
        cursor.execute(f"""
            SELECT id, id_categoria, descricao, valor, uuid_sequencia, data_efetiva 
            FROM {TBNAME} WHERE id = %s 
            LIMIT 1""", id)

        return LancamentoDespesa().set(cursor.fetchone())


def update(item: LancamentoDespesa):
    conn = db.get_conn()

    with conn.cursor() as cursor:
        cursor.execute(f"""
            UPDATE {TBNAME} set id_categoria = %s, descricao = %s, valor = %s, data_efetiva = %s WHERE id = %s
        """, (item.id_categoria, item.descricao, item.valor, item.data_efetiva, item.id))

    conn.commit()
