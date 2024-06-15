import csv
import json

# Condição: para execução do código sem erro é necessário pelo menos uma lista vazia no arquivo de texto

print("Bem-Vindo a Cafeteria\n")

with open("arq.json") as card:    # <- abrir e ler o arquivo de texto
    cardapio = json.load(card)

while True:
    print("\n------- MENU PRINCIPAL --------\n1) Adicionar itens ao cardápio\n2) Excluir itens do cardápio\n3) Alterar itens do cardápio\n4) Buscar itens no cardápio\n5) Listar todos os itens do cardápio\n6) Acessar o carrinho\n0) Encerrar Programa")
    acao = int(input("\nDigite o numero correspondente a ação:"))     # <- executar a ação do menu
    if acao == 0:  # <- se for a ação 0
        break      # <- finaliza o programa

# -------------- Parte Adicionar

    elif acao == 1:    # <- se for a ação 1
        print("\nCardapio atual:")
        for i in cardapio:              #  <- exibir o cardapio
            print(i)
        lista = []          # <- lista vazia para adcionar os itens
        lista.clear()       #  <- zerar a lista para não repetir itens
        x1 = str(input("\nInsira o item:"))
        x2 = str(input("Insira o sub-item:"))
        lista.append(x2)
        x3 = str(input("Insira o produto:"))
        lista.append(x3)
        x5 = "R$"       # <- inserir a string de de reais na lista
        lista.append(x5)
        x4 = str(input("Insira o valor:"))
        lista.append(x4)
        dados = {x1:lista}      # <- gerar dicionario com os itens e produtos
        cardapio.append(dados)    # <- adicionar o item ao cardapio
        print("\nCadápio atualizado:")
        for i in cardapio:          # <- imprimir o cardapio atualizado
            print(i)
        with open("arq.json", "w") as file:     # <- escrever o cardapio atualizado no arquivo txt
            json.dump(cardapio, file)

# ----------- Parte Excluir

    elif acao == 2:
        print("\n")
        cont = 0     # <- contador começa em 0 que funciona como indice
        for i in cardapio:
            print(cont,i)   # <- listar o cardapio a partir do indice
            cont+=1
        x = int(input("\nInsira o numero correspondente ao item que deseja excluir:"))  # <- digitar o indice do item
        del cardapio[x]         # <- deletar o item escolhido do cardapio
        print("\nItem removido com sucesso!")
        print("Cardápio atualizado:")
        for i in cardapio:          # <- imprimir o cardapio atualizado
            print(i)
        inicio = []   # <- criar lista vazia
        with open("arq.json", "w") as fil:      # <- resetar o txt com uma com uma lista vazia
            json.dump(inicio, fil)
        with open("arq.json", "w") as file:     # <- escrever o cardapio atualizado no txt
            json.dump(cardapio, file)

# ----------- Parte Alterar itens

    elif acao == 3:
        cont = 0
        for i in cardapio:
            print(cont,i)
            cont+=1
        lista = []
        lista.clear()
        x = int(input("\nInsira o numero correspondente ao item que deseja alterar:"))
        x1 = str(input("\nInsira o item:"))
        lista.append(x1)
        x2 = str(input("Insira o sub-item:"))
        lista.append(x2)
        x3 = str(input("Insira o produto:"))
        lista.append(x3)
        x4 = str(input("Insira o valor:"))
        lista.append("R$ " + x4)
        cardapio[x] = lista
        print("\nItem alterado com sucesso!")
        print("Cardápio atualizado:")
        for i in cardapio:
            print(i)
        with open('arq.csv',"w") as arquivo:
            conteudo = csv.writer(arquivo)
            for linha in cardapio:
                conteudo.writerow(linha)
