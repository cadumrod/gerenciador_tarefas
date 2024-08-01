import bd
from time import sleep


def menu():
    print(f"\n{'*' * 20} Gerenciador de tarefas {'*' * 20}\n")
    print('Escolha uma das opções abaixo digitando o número respectivo: \n1 - Adicionar uma tarefa \n2 - Visualizar tarefas \n3 - Marcar uma tarefa como concluída \n4 - Remover tarefas \n5 - Encerrar programa \n6 - Deletar TODAS as tarefas')


def escolha_usuario():
    while True:
        try:
            escolha = int(input("Digite sua escolha: "))
            if escolha in [1, 2, 3, 4, 5, 6]:
                return escolha
            else:
                print("Escolha inválida. Digite um número entre 1 e 5.")
        except:
            print("Por favor, utilize apenas números.")


def main():
    while True:
        conexao = bd.conectar_banco_dados('tarefas.db')
        bd.criar_tabela(conexao)

        menu()
        escolha = escolha_usuario()

        if escolha == 1:
            add_tarefa = input("Digite a tarefa a ser adicionada: ")
            bd.adicionar_tarefas(conexao, add_tarefa)
            bd.salvar_tarefas_json(conexao, 'tarefas.json')
            print("### Tarefa adicionada com sucesso! ###\n")

        elif escolha == 2:
            print()
            tarefas = bd.carregar_tarefas_json("tarefas.json")
            if not tarefas:
                print("Sem tarefas adicionadas durante essa sessão.")
                print()
                print("Todas as suas tarefas:")
                bd.imprimir_tarefas()

        elif escolha == 3:
            print()
            print("Suas tarefas:")
            bd.imprimir_tarefas()
            while True:
                try:
                    excluir_tarefa = int(input(
                        "Escolha a tarefa para concluir selecionando seu respectivo número: "))
                    lista_id = bd.visualizar_tarefas(conexao)
                    ids = [tarefa[0] for tarefa in lista_id]

                    if excluir_tarefa in ids:
                        bd.alterar_status(conexao, id=excluir_tarefa,
                                          novo_status='concluída')
                        print("Tarefa concluída com sucesso!")
                        break
                    else:
                        print(
                            "\nEscolha inválida. Digite o número existente na lista de tarefas.")
                        print("Suas tarefas:")
                        bd.imprimir_tarefas()
                except:
                    print("\nPor favor, utilize apenas números.")
                    print("Suas tarefas:")
                    bd.imprimir_tarefas()

        elif escolha == 4:
            print()
            print("Suas tarefas:")
            bd.imprimir_tarefas()
            while True:
                try:
                    excluir_tarefa = int(input(
                        "Escolha a tarefa para excluir selecionando seu respectivo número: "))
                    lista_id = bd.visualizar_tarefas(conexao)
                    ids = [tarefa[0] for tarefa in lista_id]

                    if excluir_tarefa in ids:
                        bd.excluir_tarefa(conexao, id=excluir_tarefa)
                        print("Tarefa excluída com sucesso!")
                        break
                    else:
                        print(
                            "\nEscolha inválida. Digite o número existente na lista de tarefas.")
                        print("Suas tarefas:")
                        bd.imprimir_tarefas()
                except:
                    print("\nPor favor, utilize apenas números.")
                    print("Suas tarefas:")
                    bd.imprimir_tarefas()

        elif escolha == 5:
            bd.esvaziar_arquivo_json('tarefas.json')
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
                    bd.apagar_banco_de_dados(conexao)
                    print()
                    print("Todas as tarefas foram excluídas!")
                    print()
                    break
                else:
                    break


if __name__ == "__main__":
    main()
