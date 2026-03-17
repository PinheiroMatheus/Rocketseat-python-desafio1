# LISTA
contatos = []

def ver_contatos(lista_contatos):
    print("\nLista de contatos:")
    for indice, contato in enumerate(lista_contatos, start=1):
        favorito_mensagem = ""
        if contato['favorito'] == True:
            favorito_mensagem = "- Favorito"
        print(f"{indice} - Nome:{contato['nome']} - Telefone:{contato['telefone']} - Email:{contato['email']} {favorito_mensagem}")
    return

def editar_contato(lista_contatos):
    indice = int(input("\nDigite o número referente ao contato que deseja alterar:\n")) - 1
    informacao_a_alterar = input("\nQual das informações a seguir você quer alterar?\nnome\ntelefone\nemail\n:")
    valor_informacao = input(f"\nO que você quer escrever no {informacao_a_alterar}:\n")
    try:
        lista_contatos[indice][informacao_a_alterar] = valor_informacao
        print("Contato alterado!")
    except:
        print("Contato ou alteração inválida!")
    return

def favoritar_contato(lista_contatos):
    indice = int(input("\nDigite o número referente ao contato que você quer favoritar?:\n")) - 1
    try:
        lista_contatos[indice]["favorito"] = True
        print("Contato favoritado!")
    except:
        print("Contato inválido!")
    return

def ver_contatos_favoritos(lista_contatos):
    print("\nLista de contatos favoritos:")
    for indice, contato in enumerate(lista_contatos, start=1):
        favorito_mensagem = ""
        if contato['favorito'] == True:
            favorito_mensagem = "- Favorito"
            print(f"{indice} - Nome:{contato['nome']} - Telefone:{contato['telefone']} - Email:{contato['email']} {favorito_mensagem}")
    return

def excluir_contato(lista_contatos):
    indice = int(input("\nQual dos contatos você deseja excluir?:\n")) - 1
    try:
        lista_contatos.pop(indice)
        print("Contato excluido!")
    except:
        print("Contato inválido!")
    return

while True:
    # ESCOLHAS
    print("\nAgenda de Contatos")
    print("1- Adicionar contato")
    print("2- Ver contatos")
    print("3- Editar contato")
    print("4- Marcar contato como favorito")
    print("5- Ver contatos favoritos")
    print("6- Apagar um contato")
    print("7- Sair")
    escolha = input("Escolha a opção desejada:\n")
    
    # VALIDACAO DE INPUT
    try:
        valor = int(escolha)
    except:
        print("Escolha uma opção válida!")
    
    # OPCOES
    match valor:
        case 1:
            contato_nome = input("Digite o nome do contato que deseja adicionar:\n")
            contato_telefone = input("Digite o telefone do contato que deseja adicionar:\n")
            contato_email = input("Digite o email do contato que deseja adicionar:\n")
            contato_favorito = input("O contato será classificado como favorito? (S ou N):\n").upper() == "S"
            contatos.append({
                "nome": contato_nome,
                "telefone": contato_telefone,
                "email": contato_email,
                "favorito": contato_favorito
            })
        case 2:
            ver_contatos(contatos)
        case 3:
            ver_contatos(contatos)
            editar_contato(contatos)
        case 4:
            ver_contatos(contatos)
            favoritar_contato(contatos)
        case 5:
            ver_contatos_favoritos(contatos)
        case 6:
            ver_contatos(contatos)
            excluir_contato(contatos)
        case 7:
            print("Finalizando...")
            break
    
