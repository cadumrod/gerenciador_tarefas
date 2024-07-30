import sqlite3
# Script que cria e/ou manipula o banco de dados


# Função para conectar no banco de dados
def conectar_banco_dados(tarefas_db):
    conexao = sqlite3.connect(tarefas_db)
    return conexao


# Função para criar tabela
def criar_tabela(conexao):
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Tarefas(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   tarefa TEXT NOT NULL,
                   status TEXT NOT NULL
        )
    ''')
    conexao.commit()


# Conectar no banco de dados
conexao = conectar_banco_dados('tarefas.db')


# Criar tabela
criar_tabela(conexao)


# Função para adicionar tarefas
def adicionar_tarefas(conexao, tarefa):
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO Tarefas (tarefa,status) VALUES (?,?)",
                   (tarefa, 'pendente'))
    conexao.commit()


# Função para visualizar tarefas
def visualizar_tarefas(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Tarefas")
    return cursor.fetchall()


adicionar_tarefas(conexao, 'Limpar sala')
adicionar_tarefas(conexao, 'Limpar cozinha')
print(visualizar_tarefas(conexao))

# Encerrar conexão
conexao.close()
