import datetime

def escolha():
    resposta = input("O que deseja realizar?\nI para inserir um usuario."
                  "\nP para pesquisar um usuario\nE para excluir um usuario."
                  "\nL para listar um usuario.\n").upper()
    return resposta

def inserir(dicionario):
    nome = input("Digite o nome: ").upper()
    dataAcesso = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    estacao = input("Digite a estação acessada: ").upper()
    nivel = input("Digite o nível de acesso: ").upper()
    if not (nivel == "ADM" or nivel == "USR" or nivel == "GST"):
        nivel = "UNKNOWN"

    key = nivel + nome[:1] + dataAcesso[:2] + dataAcesso[-2:]
    dicionario[key] = [nome, dataAcesso, estacao, nivel]

def pesquisar(dicionario, nome):
    for key, valor in dicionario.items():
        if valor[0] == nome:
            print("Nome: ", valor[0])
            print("Ultimo acesso: ", valor[1])
            print("Ultima estação: ", valor[2])
            print("Nivel de acesso: ", valor[3])
        else:
            print("Não foi encontrado o usuario informado")

def excluir(dicionario, key):
    if dicionario.get(key) != None:
        del dicionario[key]
        print("Usuario excluido")
    else:
        print("Não foi encontrado o usuario informado")

def listar(dicionario):
    for key, valor in dicionario.items():
        print("Login: ", key)
        print("Dados: ", valor)
