import psycopg2


def conectar_banco_dados():
    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5432",
            database = "postgre.py",
            user = "postgres",
            password = "09082004@Vi",

        )
        return conn
    except psycopg2.Error as e:
        print("Erro ao conectar ao banco de dados:", e)
        return None


def desconectar():
    conn = conectar_banco_dados()

    if conn:
        conn.close()

    else:
        return None