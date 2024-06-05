import csv

print("Bem-Vindo a Cafeterias\n")

cardapio = []

while True:
    print("\n------- MENU PRINCIPAL --------\n1) Adicionar itens ao cardápio\n2) Excluir itens do cardápio\n3) Alterar itens do cardápio\n4) Buscar itens no cardápio\n5) Listar todos os itens do cardápio\n0) Encerrar Programa")
    acao = int(input("\nDigite o numero correspondente a ação:"))
    if acao == 0:
        break

