import sqlite3
# Script que cria e/ou manipula o banco de dados


################################# FUNÇÕES BD #########################################

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


################################# FUNÇÕES APP #########################################

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


# Função para alterar status de tarefa
def alterar_status(conexao, id, novo_status):
    cursor = conexao.cursor()
    cursor.execute("UPDATE Tarefas SET status = ? WHERE id = ?",
                   (novo_status, id))
    conexao.commit()


# Função para remover tarefas
def excluir_tarefa(conexao, id):
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM Tarefas WHERE id = ?", (id,))
    conexao.commit()


excluir_tarefa(conexao, 1)
excluir_tarefa(conexao, 2)
print(visualizar_tarefas(conexao))

# Encerrar conexão
conexao.close()
