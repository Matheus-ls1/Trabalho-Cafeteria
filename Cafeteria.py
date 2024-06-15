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
        cont = 0      # <- contador começa em 0 que funciona como indice
        for i in cardapio:
            print(cont,i)
            cont+=1
        lista = []
        lista.clear()
        x = int(input("\nInsira o numero correspondente ao item que deseja alterar:"))
        x1 = str(input("\nInsira o item:"))
        x2 = str(input("Insira o sub-item:"))
        lista.append(x2)
        x3 = str(input("Insira o produto:"))
        lista.append(x3)
        x5 = "R$"
        lista.append(x5)
        x4 = str(input("Insira o valor:"))
        lista.append(x4)
        dados = {x1: lista}     # <- gerar um dicionario conforme a pessoa escreveu
        cardapio[x] = dados     # <- atualizar o item do cardapio escolhido pelo que a pessoa escreveu a partir do indice
        print("\nItem alterado com sucesso!")
        print("Cardápio atualizado:")
        for i in cardapio:
            print(i)
        reset = []
        with open("arq.json", "w") as fil:
            json.dump(reset, fil)
        with open("arq.json", "w") as file:
            json.dump(cardapio, file)
# --------- Parte buscar
    
# ------------ Parte Carrinho

    elif acao == 6:
        lista0 = []  # <- lista separada para o carrinho começa vazia
        while True:  # <- looping para o carrinho
            print("\n1) Adicionar itens ao carrinho\n2)Remover itens do carrinho\n0) Finalizar compra")  # <- menu do carrinho
            cont = 0      # <- contador começa em 0 que funciona como indice
            x = int(input("\nDigite o numero correspondente a ação:"))  # <- digitar o numero do indice

            if x == 1:
                for i in cardapio:
                    print(cont, i)  # <- imprimir todos os itens do cardapio com o indice na frente
                    cont += 1
                y = int(input("\nDigite o numero correspondente ao item que deseja adicionar:"))
                carr = cardapio[y]   # <- criar variavel com o dicionario que a pessoa quer adcionar ao carrinho
                lista0.append(carr)  # <- adicionar este dicionario a lista separada paro o carrinho (lista0)
                print("\nCarrinho atual:")
                for n in lista0:
                    print(n)
            elif x == 2:
                for i in lista0:      # <- imprimir todos os itens do cardapio com o indice na frente
                    print(cont, i)
                    cont += 1
                y = int(input("\nDigite o numero correspondente ao item que deseja remover:"))
                del lista0[y]      # <- deletar o dicionario escolhido da lista0 pelo indice
                print("\nCarrinho atual:")
                for n in lista0:
                    print(n)
            elif x == 0:
                lista1 = []  # <- lista vazia para armazenar os valores
                for i in lista0: # <- para cada dicionario da lista do carrinho
                    u = i.values()  # <- a variavel "u" vai ser só os valores dos dicionarios -- exemplo : ["refrigerante","coca-cola","R$","5,00"]
                    for z in u:     # <- para cada elemento de "u"  ------------------------------------------------^ -----------^ ------^ ----^
                        a = str((z[-1]).replace(",", "."))  # <- "a" vai ser o ultimo indice[-1] e ao inves da virgula (,) vai escrever ponto (.)
                        a1 = float(a)   # <- "a1" vai ser igual ao a mas vai transformar a string em numero real
                        lista1.append(a1)   # <- adicionar o elemento do ultimo indice como numero real(float) na lista1
                        valor = sum(lista1)     # <- somar todos os elementos da lista1
                        garcom = valor*(10/100)     # <- calcular os 10% do garçom
                        valor_total = valor + garcom    # <- soma do valor dos produtos + 10% do garçom
                print(f"\nSua compra ficou no valor de R$ {valor_total:.2f} (incluso os 10% do garçom)\n")
                c = str(input("Se deseja finalizar sua compra digite '0', se deseja alterar o carrinho digite '1':"))   # ação final da compra
                if c == "0":  # <- se digitar 0
                    print("\nSUA COMPRA FOI REALIZADA COM SUCESSO !")
                    break   # <- finaliza o carrinho e volta para o menu do cardapio la em cima
                elif c == "1":    # <- se digitar 1
                    continue    # <- continuar o código la no menu do carrinho
                else:
                    print("\n------ Erro! -------\nInsira um número correspondente a ação do menu!")
            else:
                print("\n------ Erro! -------\nInsira um número correspondente a ação do menu!")
                continue
    else:   # <- se a pessoa digitar um numero que não existe no menu do cardapio
        print("\n------ Erro! -------\nInsira um número correspondente a ação do menu!")
        continue    # <- retorna para o menu do cardapio
