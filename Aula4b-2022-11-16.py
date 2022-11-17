# Continuação da Aula4a - integração
import sqlite3

conexao = sqlite3.connect("dc_universe.db")
cursor = conexao.cursor()

# Comando para inserir um herói/vilão
sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (12, 'The Flash', 'Barry Allen', 'Herói(na)')"

# Executar o comando SQL
cursor.execute(sql)

# Confirmar o INSERT com commit() e fechar o banco
conexao.commit()
conexao.close()