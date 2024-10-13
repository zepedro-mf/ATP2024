import random

# Menu
def menu():
    print("""Bem vindo ao jogo dos 21 fósforos!
Há dois modos possiveis para iniciar escolha um:
    1 - O computador começa a jogar.
    2 - O Utilizador começa a jogar.""")

    modo = int(input("Que modo deseja? "))

    if modo == 1 or modo == 2:
        if modo == 1:
            computador_começa()
        else:
            utilizador_começa()
    else:
        print("Erro! Insira um modo válido")

# Jogada do Utilizador
def jogada_utilizador(fosforos_restantes):
    jogo_terminou = False
    while not jogo_terminou:
        entrada = input("Escolha um número de 1 a 4: ")

        if entrada.isdigit():
            n = int(entrada)

            if 1 <= n <= 4 and n <= fosforos_restantes:
                jogo_terminou = True
            else:
                print(f"Erro: Insira um número válido entre 1 e 4 e que não exceda {fosforos_restantes}.")
        else:
            print("Erro: Por favor, insira um número inteiro válido.")

    return n

# Utilizador começa o jogo
def utilizador_começa():
    fosforos = 21
    jogo_terminou = False
    print("\nO utilizador começa a jogar.")
    
    while not jogo_terminou:
        # Turno do utilizador
        n = jogada_utilizador(fosforos)
        print(f"O Utilizador escolheu {n} fósforos, e sobram {fosforos - n}.")
        
        fosforos -= n
        
        # Verifica se o utilizador tirou o último fósforo
        if fosforos <= 0:
            print("Você tirou o último fósforo. O computador venceu!")
            jogo_terminou = True
        else:
            c = 5 - n
            print(f"O computador escolheu {c}, e sobram {fosforos - c}.")
            
            fosforos -= c
            
            # Verifica se o computador tirou o último fósforo
            if fosforos <= 0:
                print("O computador tirou o último fósforo. Você venceu!")
                jogo_terminou = True

# Computador começa o jogo
def computador_começa():
    fosforos = 21
    t = 0
    jogo_terminou = False
    while fosforos > 0:
        if t == 0:
            c = random.randint(1,4)
            fosforos -= c
            t += 1
        elif fosforos % 5 != 1 and jogo_terminou == False:
            if n + c > 5:
                c = (10-n-c)
            else:
                c = (5-n-c)
            fosforos -= c
            t += 1
            jogo_terminou = True
        elif fosforos % 5 != 1:
            c = (5-n)
            fosforos -= c
            t += 1
        else:
            c = random.randint(1,4)
            fosforos -= c
            t += 1
        
        if fosforos > 0:
            print(f"O computador escolheu {c} fósforo, e sobram {fosforos}.")
            n = jogada_utilizador(fosforos)
            fosforos -= n
            t += 1
            print(f"O Utilizador escolheu {n} fósforo, e sobram {fosforos}.")
    if t%2 == 1:
        print("O computador tirou o último fósforo. Você venceu!")
    else:
        print("O Utilizador tirou o último fósforo. Você perdeu!")

menu()


