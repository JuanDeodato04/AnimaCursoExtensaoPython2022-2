# Continuação da Aula4a e Aula4b - integração
import sqlite3

# Função conectar()
def conectar():
  conexao = sqlite3.connect("dc_universe.db")
  cursor = conexao.cursor()
  return conexao, cursor