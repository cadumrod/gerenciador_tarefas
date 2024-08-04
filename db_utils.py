import sqlite3
import json
import os


################################# FUNÇÕES BD #########################################

def conectar_banco_dados(tarefas_db):
    conexao = sqlite3.connect(tarefas_db)
    return conexao


conexao = conectar_banco_dados('tarefas.db')


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


criar_tabela(conexao)


################################# FUNÇÕES APP #########################################

# Lista para armazenar as IDs das tarefas inseridas durante a execução do programa
tarefas_inseridas = []


def adicionar_tarefas(conexao, tarefa):
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO Tarefas (tarefa,status) VALUES (?,?)",
                   (tarefa, 'pendente'))
    tarefas_inseridas.append(cursor.lastrowid)
    conexao.commit()


def visualizar_tarefas(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Tarefas")
    return cursor.fetchall()


def imprimir_tarefas():
    tarefas = visualizar_tarefas(conexao)
    for tarefa in tarefas:
        print(f'{tarefa[0]} - Tarefa: {tarefa[1]} / {tarefa[2]}')


def alterar_status(conexao, id, novo_status):
    cursor = conexao.cursor()
    cursor.execute("UPDATE Tarefas SET status = ? WHERE id = ?",
                   (novo_status, id))
    conexao.commit()


def excluir_tarefa(conexao, id):
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM Tarefas WHERE id = ?", (id,))
    conexao.commit()


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


def carregar_tarefas_json(arquivo):
    try:
        with open(arquivo, "r", encoding="utf-8") as file:
            tarefas_json = file.read()
            if not tarefas_json.strip():  # Verifica se o arquivo está vazio
                return []
            tarefas = json.loads(tarefas_json)

            print('#' * 20)
            print('Tarefas incluídas nessa sessão:')
            for tarefa in tarefas:
                print(f'- {tarefa[1]} / {tarefa[2]}')

            print()
            print("Todas as suas tarefas:")
            imprimir_tarefas()
            print('#' * 20)
            return tarefas

    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return []

    except json.JSONDecodeError:
        print("Erro ao decodificar o JSON.")
        return []


def esvaziar_arquivo_json(arquivo):
    with open(arquivo, 'w', encoding='utf-8') as f:
        f.write('')


def apagar_banco_de_dados(conexao):
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM Tarefas")
    conexao.commit()


def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
