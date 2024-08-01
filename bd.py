import sqlite3
import json
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


# Lista para armazenar as IDs das tarefas inseridas durante a execução do programa
tarefas_inseridas = []

################################# FUNÇÕES APP #########################################

# Função para adicionar tarefas


def adicionar_tarefas(conexao, tarefa):
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO Tarefas (tarefa,status) VALUES (?,?)",
                   (tarefa, 'pendente'))
    tarefas_inseridas.append(cursor.lastrowid)
    conexao.commit()


# Função para visualizar tarefas
def visualizar_tarefas(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Tarefas")
    return cursor.fetchall()
# Variavel para imprimir tuplas do BD como lista
# tarefas = visualizar_tarefas(conexao)

# Função para imprimir as tarefas formatadas como lista


def imprimir_tarefas():
    tarefas = visualizar_tarefas(conexao)
    for tarefa in tarefas:
        print(f'{tarefa[0]} - Tarefa: {tarefa[1]} / {tarefa[2]}')


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


# Função para salvar tarefas no arquivo json
def salvar_tarefas_json(conexao, arquivo):
    cursor = conexao.cursor()
    if tarefas_inseridas:
        placeholders = ','.join(['?'] * len(tarefas_inseridas))
        cursor.execute(
            f'SELECT * FROM Tarefas WHERE id IN ({placeholders})', tarefas_inseridas)
        tarefas = cursor.fetchall()
        tarefas_json = json.dumps(tarefas, ensure_ascii=False, indent=4)

        with open(arquivo, "w", encoding='utf-8') as file:
            file.write(tarefas_json)
    else:
        []


# Função para carregar tarefas do arquivo json
def carregar_tarefas_json(arquivo):
    try:
        with open(arquivo, "r", encoding="utf-8") as file:
            tarefas_json = file.read()
            if not tarefas_json.strip():  # Verifica se o arquivo está vazio
                return []
            tarefas = json.loads(tarefas_json)

            print('Tarefas incluídas nessa sessão:')
            for tarefa in tarefas:
                print(f'- {tarefa[1]} / {tarefa[2]}')

            print()
            print("Todas as suas tarefas:")
            imprimir_tarefas()
            return tarefas

    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return []

    except json.JSONDecodeError:
        print("Erro ao decodificar o JSON.")
        return []


# Função para limpar arquivo json quando encerrar o app
def esvaziar_arquivo_json(arquivo):
    with open(arquivo, 'w', encoding='utf-8') as f:
        f.write('')


# Função criada para limpar o banco de dados. Utilize apenas se tiver CERTEZA que deseja excluir tudo da table Tarefas.
def apagar_banco_de_dados(conexao):
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM Tarefas")
    conexao.commit()


# adicionar_tarefas(conexao, 'tarefa8')
# adicionar_tarefas(conexao, 'tarefa9')
# adicionar_tarefas(conexao, 'tarefa10')
# salvar_tarefas_json(conexao, 'tarefas.json')
# carregar_tarefas_json("tarefas.json")
# esvaziar_arquivo_json('tarefas.json')
# lista_id = visualizar_tarefas(conexao)
# ids = [tarefa[0] for tarefa in lista_id]
# print(ids)
# print(visualizar_tarefas(conexao)[0][0])
# print('*' * 20)
# alterar_status(conexao, id=8, novo_status='concluido')
# imprimir_tarefas()

# Encerrar conexão
# conexao.close()
