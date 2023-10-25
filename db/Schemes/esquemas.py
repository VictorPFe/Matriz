import psycopg2
from db.postgre import conectar_banco_dados


def esquemas():
    conn = conectar_banco_dados()
    try:
        if conn:
            cursor = conn.cursor()

            # Tabela Sistemas
            create_table_sistemas = '''
            CREATE TABLE IF NOT EXISTS sistemas (
                codigo text PRIMARY KEY,
                nome_do_sistema VARCHAR(20)
            );
           '''

            cursor.execute(create_table_sistemas)
            
            # Tabela perfis
            create_table_perfis = '''
            CREATE TABLE IF NOT EXISTS perfis_de_acesso (
                id SERIAL PRIMARY KEY,
                codigo_sistema CHAR(15) REFERENCES sistemas(codigo),
                nome_do_perfil VARCHAR(20),
                descricao_do_usuario VARCHAR(200),
                senha VARCHAR(20),
                cpf VARCHAR(11),
                adm BOOLEAN
            );
           '''

            cursor.execute(create_table_perfis)

            # Confirme as alterações no banco de dados
            conn.commit()

        else:
            # Trate o erro de conexão aqui
            return None
    
    except psycopg2.Error as e:
        print("Erro ao conectar ao banco de dados:", e)