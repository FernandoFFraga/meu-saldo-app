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
        ) SELECT * FROM tb_final ORDER BY data_efetiva DESC, id DESC LIMIT 1000
    """

    df = pd.read_sql(query, con=db.get_engine())

    return df


def select_despesas_sumarizadas():
    query = f"""
        SELECT nome, limite_mensal, coalesce(sum(valor), 0) total, coalesce(LEAST(SUM(valor) / limite_mensal, 1), 0) AS porcentagem 
        FROM {TB_CAT_DEP} cd
        LEFT JOIN {TB_LAC_DEP} ld ON ld.id_categoria = cd.id
        WHERE year(coalesce(data_efetiva, now())) = year(now()) AND month(coalesce(data_efetiva, now())) = month(now()) 
        GROUP BY 1, 2
        ORDER BY nome ASC
    """

    df = pd.read_sql(query, con=db.get_engine())

    return df


def select_despesas_diarias_mes():
    query = f"""
        SELECT data_efetiva as dia, sum(valor) total
        FROM {TB_LAC_DEP}
        WHERE year(coalesce(data_efetiva, now())) = year(now()) AND month(coalesce(data_efetiva, now())) = month(now())
        GROUP BY 1
        ORDER BY 1 ASC
    """

    df = pd.read_sql(query, con=db.get_engine())

    return df

def select_despesas_total_mes():
    query = f"""
        WITH tb_atual AS (
            SELECT coalesce(SUM(valor), 0.00) total_atual
            FROM {TB_LAC_DEP} 
            WHERE year(coalesce(data_efetiva, now())) = year(now()) AND month(coalesce(data_efetiva, now())) = month(now())
        ), tb_passado AS (
            SELECT coalesce(SUM(valor), 0.00) total_passado
            FROM {TB_LAC_DEP} 
            WHERE YEAR(COALESCE(data_efetiva, NOW())) = YEAR(DATE_SUB(NOW(), INTERVAL 1 MONTH)) AND MONTH(COALESCE(data_efetiva, NOW())) = MONTH(DATE_SUB(NOW(), INTERVAL 1 MONTH))
        )
        SELECT 
            tb_atual.total_atual,
            tb_passado.total_passado,
            COALESCE(CASE 
                WHEN tb_passado.total_passado = 0 THEN NULL
                ELSE ROUND(((tb_atual.total_atual - tb_passado.total_passado) / tb_passado.total_passado) * 100, 1)
            END, 0) AS variacao_percentual
        FROM tb_atual
        JOIN tb_passado ON 1 = 1  
    """

    conn = db.get_conn()

    with conn.cursor() as cursor:
        cursor.execute(query)
        item = cursor.fetchone()
        return item.get('total_atual', 0), item.get('variacao_percentual', 0)


def select_rendimento_total_mes():
    query = f"""
        WITH tb_atual AS (
            SELECT coalesce(SUM(valor), 0.00) total_atual
            FROM {TB_LAC_REN} 
            WHERE year(coalesce(data_efetiva, now())) = year(now()) AND month(coalesce(data_efetiva, now())) = month(now())
        ), tb_passado AS (
            SELECT coalesce(SUM(valor), 0.00) total_passado
            FROM {TB_LAC_REN} 
            WHERE YEAR(COALESCE(data_efetiva, NOW())) = YEAR(DATE_SUB(NOW(), INTERVAL 1 MONTH)) AND MONTH(COALESCE(data_efetiva, NOW())) = MONTH(DATE_SUB(NOW(), INTERVAL 1 MONTH))
        )
        SELECT 
            tb_atual.total_atual,
            tb_passado.total_passado,
            COALESCE(CASE 
                WHEN tb_passado.total_passado = 0 THEN NULL
                ELSE ROUND(((tb_atual.total_atual - tb_passado.total_passado) / tb_passado.total_passado) * 100, 1)
            END, 0) AS variacao_percentual
        FROM tb_atual
        JOIN tb_passado ON 1 = 1  
    """

    conn = db.get_conn()

    with conn.cursor() as cursor:
        cursor.execute(query)
        item = cursor.fetchone()
        return item.get('total_atual', 0), item.get('variacao_percentual', 0)
