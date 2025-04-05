import sys

# Controla a continuidade do sistema com base na resposta do usuário
def continuarSistema():
    escolha = False
    
    while escolha != True:
        stop = input("Deseja parar? S/N: ").strip().upper()

        print (stop)
        match stop:
            case 'S':
                sys.exit(1)  # Encerra o programa
            case 'N':
                print("Retornando para inserção de novo usuário...")
                escolha = True
            case _:
                print ("Opção inexistente, por favor, digite S ou N!")

# Coleta dados básicos de uma pessoa
def coletarInformacao():
    print("COLETANDO INFORMAÇÕES DA PESSOA")

    nome = input("Insira um nome: ")
    idade = input("Insira uma idade: ")
    cor = input("Insira uma cor preferida: ")

    return {
        "nome": nome,
        "idade": idade,
        "cor": cor
    }

# Insere nova pessoa na lista, tratando conflitos por cor
def insercaoLista(infoPessoas):
    info_pessoa = coletarInformacao()
    adicionarAtual = True

    for pessoaAtual in infoPessoas:
        pDic = dict(pessoaAtual)

        # Verifica conflito de cor
        if info_pessoa.get('cor') == pDic.get('cor'):
            escolha = False

            while escolha != True:
                choicePessoa = input (
                    f"{info_pessoa.get('nome')} selecionou a mesma cor de {pDic.get('nome')}. Deseja remover {pDic.get('nome')}? S/N: "
                ).strip().upper()

                match choicePessoa:
                    case 'S':
                        print(f"Removendo {pDic.get('nome')}!")
                        infoPessoas.remove(pessoaAtual)   
                        escolha = True
                    case 'N':
                        print(f"Portanto, {info_pessoa.get('nome')} não entrou na lista")
                        adicionarAtual = False
                        escolha = True
                    case _:
                        print("Opção inexistente, por favor, digite S ou N!") 

    if adicionarAtual:
        infoPessoas.append(info_pessoa)
        print(f"Adicionando {info_pessoa.get('nome')} à lista de pessoas.")

    return infoPessoas

# Ordena a lista de pessoas por nome e adiciona um índice de ordenação
def ordenarLista(infoPessoas):
    print("Ordenando lista de pessoas...")

    ordemAlfabetica = sorted(infoPessoas, key=lambda pessoa: pessoa['nome'])

    listaAtualizada = []

    for pessoaAtual in ordemAlfabetica:
        pessoaDic = dict(pessoaAtual)

        pessoaAtualizada = {
            "nome": pessoaDic.get('nome'),
            "idade": pessoaDic.get('idade'),
            "cor": pessoaDic.get('cor'),
            "indice": ordemAlfabetica.index(pessoaAtual)
        }

        listaAtualizada.append(pessoaAtualizada)

    print(listaAtualizada)

# Loop principal do sistema
def looping():
    infoPessoas = []

    while True: 
        insercaoLista(infoPessoas)
        ordenarLista(infoPessoas)
        continuarSistema()

looping()

    












    
        
    









