from Dicionarios.Dicionario2.ManagerFunctions import *

usuarios = {}

opcao = escolha()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(usuarios)
    if opcao == "P":
        pesquisar(usuarios, input("Informe o nome: ").upper())
    if opcao == "E":
        excluir(usuarios, input("Informe o login que será excluido: ").upper())
    if opcao == "L":
        listar(usuarios)
    opcao = escolha()

exit()