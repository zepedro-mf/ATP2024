import random

# Menu
def menu():
    lista = [] # Variavel Interna
    v = True
    
    while v == True:
        print("""\n===== Menu =====
(1) Criar Lista 
(2) Ler Lista
(3) Soma
(4) Média
(5) Maior
(6) Menor
(7) estaOrdenada por ordem crescente
(8) estaOrdenada por ordem decrescente
(9) Procura um elemento
(0) Sair""")
        modo = int(input("Que modo deseja? "))

        if modo == 1:
            lista = criaListaAleatoria()
            print(f"Lista aleatória criada: {lista}")
        elif modo == 2:
            lista = criaLista()
            print(f"Lista criada pelo usuário: {lista}")
        elif modo == 3:
            if len(lista) > 0:
                print(f"Soma dos elementos: {somaLista(lista)}")
            else:
                print("A lista está vazia. Por favor, crie uma lista primeiro.")
        elif modo == 4:
            if len(lista) > 0:
                print(f"Média dos elementos: {mediaLista(lista)}")
            else:
                print("A lista está vazia. Por favor, crie uma lista primeiro.")
        elif modo == 5:
            if len(lista) > 0:
                print(f"Maior dos elementos: {maiorLista(lista)}")
            else:
                print("A lista está vazia. Por favor, crie uma lista primeiro.")
        elif modo == 6:
            if len(lista) > 0:
                print(f"Menor dos elementos: {menorLista(lista)}")
            else:
                print("A lista está vazia. Por favor, crie uma lista primeiro.")
        elif modo == 7:
            if len(lista) > 0:
                print(f" A lista está em ordem crescente? {estaOrdenadaC(lista)}")
            else:
                print("A lista está vazia. Por favor, crie uma lista primeiro.")
        elif modo == 8:
            if len(lista) > 0:
                print(f" A lista está em ordem decrescente? {estaOrdenadaD(lista)}")
            else:
                print("A lista está vazia. Por favor, crie uma lista primeiro.")
        elif modo == 9:
            if len(lista) > 0:
                elem = int(input("Que número deseja procurar? "))
                print(f"O {elem} está na posição {unicos(lista, elem)}")
            else:
                print("A lista está vazia. Por favor, crie uma lista primeiro.")
        elif modo == 0: 
            print(f"""Programa Encerrado.
Lista atual {lista}.""")
            v = False
        

# Criar Lista Aleatória
def criaListaAleatoria():
    tamanho = int(input("Tamanho da lista"))
    lista = [random.randint(1, 100) for _ in range(tamanho)]
    
    return lista

# Criar Lista 
def criaLista():
    lista = []
    tamanho = int(input("Tamanho da Lista?"))

    while tamanho > 0:
        lista.append(int(input("Que número deseja adicionar?")))
        tamanho -= 1

    return lista

# Soma da Lista
def somaLista(lista):
    res = 0 
    for x in lista: 
        res += x 
    
    return res

# Média da Lista
def mediaLista(lista):
    res = 0 
    for x in lista: 
        res += x 
    
    res = res / len(lista)
    
    return res

# Maior da Lista
def maiorLista(lista):
    res = lista[0]
    
    for x in lista:
        if x > res:
            res = x
    
    return res

# Menor da Lista
def menorLista(lista):
    res = lista[0]
    
    for x in lista:
        if x < res:
            res = x
    
    return res

# Ordem Crescente
def estaOrdenadaC(lista):
    res = "SIM"
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:  
            res = "NÃO" 
    
    return res 

# Ordem Decrescente
def estaOrdenadaD(lista):
    res = "SIM"
    for i in range(len(lista) - 1):
        if lista[i] < lista[i + 1]:  
            res = "NÃO"  
    
    return res  

# Encontrar um número
def unicos(lista, elem):
    contador = 0  
    posicao = -1 

    for num in lista:
        if num == elem:  
            posicao = contador  
        contador += 1 
    
    return posicao  

menu()