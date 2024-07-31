import bd
from time import sleep


def menu():
    print(f"{'*' * 20} Gerenciador de tarefas {'*' * 20}\n")
    print('Escolha uma das opções abaixo digitando o número respectivo: \n1 - Adicionar uma tarefa \n2 - Visualizar tarefas \n3 - Marcar uma tarefa como concluída \n4 - Remover tarefas \n5 - Encerrar programa')


def escolha_usuario():
    while True:
        try:
            escolha = int(input("Digite sua escolha: "))
            if escolha in [1, 2, 3, 4, 5]:
                return escolha
            else:
                print("Escolha inválida. Digite um número entre 1 e 5.")
        except:
            print("Por favor, utilize apenas números.")


def main():
    while True:
        menu()
        escolha = escolha_usuario()

        if escolha == 1:
            print('adicionando tarefa')
        elif escolha == 2:
            print('visualizando tarefa')
        elif escolha == 3:
            print('concluindo tarefa')
        elif escolha == 4:
            print('removendo tarefa')
        elif escolha == 5:
            print('Saindo...')
            sleep(2)
            break


if __name__ == "__main__":
    main()
