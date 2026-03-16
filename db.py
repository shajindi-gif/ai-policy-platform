import psycopg2

def get_conn():
    return psycopg2.connect(
        dbname="ai_company",
        user="shajindi",
        password="",
        host="localhost",
        port=5432,
    )
