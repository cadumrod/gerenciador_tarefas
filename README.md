# Gerenciador de Tarefas

Um aplicativo simples de gerenciamento de tarefas usando Python e SQLite.

## Descrição

Este projeto é um gerenciador de tarefas de linha de comando que permite aos usuários realizarem os comandos:
- **Adicionar tarefas**
- **Visualizar tarefas**
- **Marcar tarefas como concluídas**
- **Excluir uma tarefa específica**
- **Excluir todas as tarefas salvas no banco de dados**
- **Encerrar o programa**

## Persistência de dados

É utilizado um banco de dados feito com SQLite o qual possui uma única tabela contendo ID`s, tarefas e status da tarefa.

## Requisitos

- Python 3.6 ou superior
- Cx_Freeze

## Instalação

1. **Clone este repositório:**

    ```bash
    git clone https://github.com/cadumrod/gerenciador_tarefas
    cd gerenciador_tarefas
    ```

2. **Crie e ative um ambiente virtual:**

    No Windows:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

    No macOS/Linux:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Construa o executável com `cx_Freeze`**:

    ```bash
    python setup.py build
    ```

## Uso

1. Após a construção, o executável estará disponível no diretório `build`. Para executar o aplicativo, navegue até o diretório de saída (por exemplo, `build/exe.win-amd64-3.12` no Windows) e execute o arquivo gerado:

    No Windows:
    ```bash
    cd build/exe.win-amd64-3.12
    app.exe
    ```

    No macOS/Linux:
    ```bash
    cd build/exe.macosx-10.6-intel-3.12
    ./app
    ```


## Estrutura do Projeto

- `app.py`: Arquivo principal do aplicativo.
- `db_utils.py`: Utilitários para manipulação do banco de dados e funções do app.
- `python.ico`: Ícone usado no aplicativo.
- `setup.py`: Script de instalação e configuração do projeto.
- `README.md`: Este arquivo de documentação.
- `requirements.txt`: Arquivo de requisitos com as dependências do projeto.
- `LICENSE`: Licença MIT.


## Autor

**Carlos Rodrigues**

- [GitHub](https://github.com/cadumrod)
- [E-mail](mailto:carlosrod.dev@gmail.com)

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.