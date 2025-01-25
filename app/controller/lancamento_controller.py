from app.constants.table_constants import TB_LAC_REN, TB_CAT_REN, TB_CAT_DEP, TB_LAC_DEP
import pandas as pd
import app.services.database_mysql as db


def select_lancamentos(date_start, date_end):
    query = f"""
        WITH tb_rendimento AS (
            SELECT lr.id, descricao, nome as categoria, valor, 'rendimento' as tipo,  data_efetiva 
            FROM {TB_LAC_REN} lr
            INNER JOIN {TB_CAT_REN} cr ON cr.id = lr.id_categoria 
            WHERE data_efetiva >= "{date_start.strftime("%Y-%m-%d")}" AND data_efetiva <= "{date_end.strftime("%Y-%m-%d")}"
        ), tb_despesa AS (
            SELECT ld.id, descricao, nome as categoria, valor, 'despesa' as tipo, data_efetiva 
            FROM {TB_LAC_DEP} ld
            INNER JOIN {TB_CAT_DEP} cd ON cd.id = ld.id_categoria 
            WHERE data_efetiva >= "{date_start.strftime("%Y-%m-%d")}" AND data_efetiva <= "{date_end.strftime("%Y-%m-%d")}"
        ), tb_final as (
            SELECT * FROM tb_rendimento
            UNION ALL
            SELECT * FROM tb_despesa
        ) SELECT * FROM tb_final ORDER BY data_efetiva DESC, descricao ASC LIMIT 1000
    """

    df = pd.read_sql(query, con=db.get_engine())

    return df
