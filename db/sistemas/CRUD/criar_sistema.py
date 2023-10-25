import psycopg2
from db.postgre import conectar_banco_dados

def novoSistema(codigo, nome_do_sistema):
  try:
    conn = conectar_banco_dados()

    cursor = conn.cursor()
    insert_query = "INSERT INTO sistemas (codigo, nome_do_sistema) VALUES (%s, %s)"

    cursor.execute(insert_query, (codigo, nome_do_sistema))
    conn.commit()

    cursor.close()
    conn.close()

  except psycopg2.Error as e:
    print(f"Erro ao criar novo sistema: {e}")