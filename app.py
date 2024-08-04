import db_utils
from time import sleep


def menu():
    print(f"\n{'*' * 20} Gerenciador de tarefas {'*' * 20}\n")
    print('Escolha uma das opções abaixo digitando o número respectivo: \n1 - Adicionar uma tarefa \n2 - Visualizar tarefas \n3 - Marcar uma tarefa como concluída \n4 - Excluir tarefa \n5 - Encerrar programa \n6 - Deletar TODAS as tarefas\n')


def escolha_usuario():
    while True:
        try:
            escolha = int(input("Digite sua escolha: "))
            if escolha in [1, 2, 3, 4, 5, 6]:
                return escolha
            else:
                print("Escolha inválida. Digite um número entre 1 e 6.")
        except:
            print("Por favor, utilize apenas números.")


def main():
    while True:
        conexao = db_utils.conectar_banco_dados('tarefas.db')
        db_utils.criar_tabela(conexao)

        try:
            menu()
            escolha = escolha_usuario()

            if escolha == 1:
                add_tarefa = input("Digite a tarefa a ser adicionada: ")
                db_utils.adicionar_tarefas(conexao, add_tarefa)
                db_utils.salvar_tarefas_json(conexao, 'tarefas.json')
                print(
                    "\n### Tarefa adicionada com sucesso ###\nRetornando ao menu principal...")
                sleep(2)
                db_utils.limpar_tela()

            elif escolha == 2:
                print()
                tarefas = db_utils.carregar_tarefas_json("tarefas.json")
                if not tarefas:
                    print("Sem tarefas adicionadas durante essa sessão.")
                    print()
                    print("Todas as suas tarefas:")
                    db_utils.imprimir_tarefas()

            elif escolha == 3:
                print()
                print("Suas tarefas:")
                db_utils.imprimir_tarefas()
                while True:
                    try:
                        alterar_tarefa = int(input(
                            "Escolha uma tarefa para CONCLUIR selecionando seu respectivo número: "))
                        lista_id = db_utils.visualizar_tarefas(conexao)
                        ids = [tarefa[0] for tarefa in lista_id]

                        if alterar_tarefa in ids:
                            db_utils.alterar_status(conexao, id=alterar_tarefa,
                                                    novo_status='concluída')
                            print(
                                "\n### Tarefa concluída com sucesso ###\nRetornando ao menu principal...")
                            sleep(2)
                            db_utils.limpar_tela()
                            break
                        else:
                            print(
                                "\nEscolha inválida. Digite o número existente na lista de tarefas.")
                            print("Suas tarefas:")
                            db_utils.imprimir_tarefas()
                    except:
                        print("\nPor favor, utilize apenas números.")
                        print("Suas tarefas:")
                        db_utils.imprimir_tarefas()

            elif escolha == 4:
                print()
                print("Suas tarefas:")
                db_utils.imprimir_tarefas()
                while True:
                    try:
                        excluir_tarefa = int(input(
                            "Escolha a tarefa para EXCLUIR selecionando seu número respectivo: "))
                        lista_id = db_utils.visualizar_tarefas(conexao)
                        ids = [tarefa[0] for tarefa in lista_id]

                        if excluir_tarefa in ids:
                            db_utils.excluir_tarefa(conexao, id=excluir_tarefa)
                            print(
                                "\n### Tarefa excluída com sucesso ###\nRetornando ao menu principal...")
                            sleep(2)
                            db_utils.limpar_tela()
                            break
                        else:
                            print(
                                "\nEscolha inválida. Digite o número existente na lista de tarefas.")
                            print("Suas tarefas:")
                            db_utils.imprimir_tarefas()
                    except:
                        print("\nPor favor, utilize apenas números.")
                        print("Suas tarefas:")
                        db_utils.imprimir_tarefas()

            elif escolha == 5:
                db_utils.esvaziar_arquivo_json('tarefas.json')
                print('Saindo...')
                sleep(1)
                break

            elif escolha == 6:
                while True:
                    apagar_todas_tarefas = str(input(
                        "Essa opção irá apagar TODAS as suas tarefas! Deseja continuar? [s]/[n]: ")).lower()

                    if apagar_todas_tarefas not in ['s', 'n']:
                        print("Digite apenas 's' ou 'n'.")

                    elif apagar_todas_tarefas == 's':
                        db_utils.apagar_banco_de_dados(conexao)
                        print()
                        print(
                            "\n### TODAS as tarefas excluídas com sucesso ###\nRetornando ao menu principal...")
                        sleep(2)
                        db_utils.limpar_tela()
                        break
                    else:
                        print(
                            "\nRetornando ao menu principal...")
                        sleep(2)
                        db_utils.limpar_tela()
                        break
        finally:
            conexao.close()


if __name__ == "__main__":
    main()
