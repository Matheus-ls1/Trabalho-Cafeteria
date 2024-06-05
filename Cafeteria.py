import csv

print("Bem-Vindo a Cafeterias\n")

cardapio = []

while True:
    print("\n------- MENU PRINCIPAL --------\n1) Adicionar itens ao cardápio\n2) Excluir itens do cardápio\n3) Alterar itens do cardápio\n4) Buscar itens no cardápio\n5) Listar todos os itens do cardápio\n0) Encerrar Programa")
    acao = int(input("\nDigite o numero correspondente a ação:"))
    if acao == 0:
        break

# -------------- Parte Adicionar

    elif acao == 1:
        print("\nCardapio atual:")
        for i in cardapio:
            print(i)
        lista = []
        lista.clear()
        x1 = str(input("\nInsira o item:"))
        lista.append(x1)
        x2 = str(input("Insira o sub-item:"))
        lista.append(x2)
        x3 = str(input("Insira o produto:"))
        lista.append(x3)
        x4 = str(input("Insira o valor:"))
        lista.append("R$ "+x4)
        cardapio.append(lista)
        print("\nCadápio atualizado:")
        for i in cardapio:
            print(i)
        with open('arq.csv',"w") as arquivo:
            conteudo = csv.writer(arquivo)
            for linha in cardapio:
                conteudo.writerow(linha)


