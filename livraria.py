print ('|' + '\u203E' * 34 + '|') #Print de boas-vindas
print ('|      Bem vindo a Livraria do     |')
print ('|        Rodrigo Alcantara         |')
print ('|' + '_' * 34 + '|')

lista_livro = []
id_global = 0

def cadastrar_livro(id): #função para cadastrar livros
    global id_global
    nome = input('Digite o nome do livro:\n')
    autor = input('Digite o autor do livro:\n')
    editora = input('Digite a editora do livro:\n')
    id_global += 1
    livro = {'id': id_global, 'nome':nome, 'autor': autor, 'editora':editora}
    lista_livro.append(livro)

def consultar_livro(): #função para consultar livros da lista
    while True:
        print ('|' + '\u203E' * 34 + '|')
        print ('|          CONSULTAR LIVRO         |')
        print ('|' + '_' * 34 + '|')
        print ('|' + '\u203E' * 34 + '|')
        print ('| 1 - Consultar todos os livros    |')
        print ('| 2 - Consultar Livro por ID       |')
        print ('| 3 - Consultar Livro(s) por autor |')
        print ('| 4 - Voltar ao Menu Principal     |')
        print ('|' + '_' * 34 + '|')
        opcao2 = input('Escolha uma das opções acima:\n')

        if opcao2 == "1":
            print('Esses são todos os livros que temos cadastrado:')
            for livro in lista_livro:
                print(livro)
        elif opcao2 == "2":
            id_consulta = int(input('Qual ID do livro que você quer consultar:\n'))
            for livro in lista_livro:
                if livro["id"] == id_consulta:
                    print(f'Livro cadastrado com ID {id_consulta}:')
                    print(livro)
                    break
            else:
                print('Livro não encontrado.')
        elif opcao2 == "3":
            autor_consulta = input('Qual o nome do autor?\n')
            print(f'Livros cadastrados do autor {autor_consulta}:\n')
            for livro in lista_livro:
                if livro["autor"].lower() == autor_consulta.lower():
                    print(livro)
        elif opcao2 == "4":
            break
        else:
            print('Opção inválida.')

def remover_livro(): #função para remover livro da lista
    while True:
        print ('|' + '\u203E' * 34 + '|')
        print ('|           REMOVER LIVRO          |')
        print ('|' + '_' * 34 + '|')
        print ('|' + '\u203E' * 34 + '|')
        print ('| 0 - Retorna ao Menu Principal    |')
        print ('| Digite o ID do livro             |')
        print ('| que deseja remover               |')
        print ('|' + '_' * 34 + '|')

        id_remover = int(input('Digite o ID do livro que você quer remover:\n'))
        if id_remover == 0:
            break
        for livro in lista_livro:
            if livro["id"] == id_remover:
                lista_livro.remove(livro)
                print(f'O livro de ID {id_remover} foi removido.')
                break
        else:
            print('ID não encontrado.')

while True: #looping menu principal
    print ('|' + '\u203E' * 34 + '|')
    print ('|           MENU PRINCIPAL         |')
    print ('|' + '_' * 34 + '|')
    print ('|' + '\u203E' * 34 + '|')
    print ('| 1 - Cadastrar Livro              |')
    print ('| 2 - Consultar Livro(s)           |')
    print ('| 3 - Remover Livro(s)             |')
    print ('| 4 - Sair                         |')
    print ('|' + '_' * 34 + '|')
    opcao1 = input('Digite uma das opções acima:\n')

    if opcao1 == '1':
        cadastrar_livro(id_global)
        continue
    elif opcao1 == '2':
        consultar_livro()
        continue
    elif opcao1 == '3':
        remover_livro()
        continue
    elif opcao1 == '4':
        print('Encerrando o programa...')
        break
    else:
        print('Opção não encontrada.')