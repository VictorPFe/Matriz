from psycopg2 import *
from db.postgre import conectar_banco_dados

def deletarSistema(codigo):
  try:
    conn = conectar_banco_dados()
    cursor = conn.cursor()

    sql = "DELETE FROM sistemas WHERE codigo = %s"
    cursor.execute(sql, (codigo,))

    
    conn.commit()
    
    cursor.close()
    conn.close()

    print(f"Registro com código {codigo} excluído com sucesso.")

  except (Exception, Error) as error:
    print(f"Ocorreu o seguinte erro: {error}")