import psycopg2
from db.postgre import conectar_banco_dados

def novoUsuario(codigo_sistema, nome_do_usuario, descricao_do_usuario, senha, cpf):
  try:
    conn = conectar_banco_dados()

    cursor = conn.cursor()
    insert_query = """
    INSERT INTO perfis_de_acesso (codigo_sistema, nome_do_perfil, descricao_do_usuario, senha, cpf)
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(insert_query, (codigo_sistema, nome_do_usuario, descricao_do_usuario, senha, cpf))
    conn.commit()

    cursor.close()
    conn.close()

  except psycopg2.Error as e:
    print(f"Erro ao criar novo perfil: {e}")

