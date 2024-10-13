import random 

def computador_pensa():
    numero_computador = random.randint(0, 100)
    tentativas = 0 
    acertou = False

    print("\nAdivinhe o número entre 0 e 100.")

    while not acertou:
        tentativas += 1 
        palpite = int(input("Qual número? "))

        if palpite > numero_computador:
            print("O número é menor")
        elif palpite < numero_computador:
            print("O número é maior")
        else:
            print(f"Acertou! O número era {numero_computador} em {tentativas} tentativas.")
            acertou = True

def utilizador_pensa():
    numero_utlizador = int(input("Escolha um número. "))
    tentaivas = 0
    acertou = False
    min = 0
    max = 100

    print("\nO computador vai tentar adivinhar.")

    while not acertou:
        tentaivas += 1
        palpite_computador = (min + max) // 2 
        print(f"O número que escolheu é {palpite_computador}?")
        resposta = input("Responda: acertou/ menor/ maior. ").lower()

        if resposta == "acertou":
            print(f"O computador acertou no número {numero_utlizador} em {tentaivas} tentativas!")
            acertou = True
        elif resposta == "menor":
            max = palpite_computador - 1 
            print("O computador falhou vamos tentar outra vez.")
        elif resposta == "maior":
            min = palpite_computador + 1
            print("O computador falhou vamos tentar outra vez.")
        else:
            print("Resposta Invalida. Responda: acertou/ menor/ maior.")

def jogar():
    print("""Bem-vindo ao jogo 'Adivinha o número!
Há 2 modos de jogo! Escolha um:
1 - O computador pensa num número, e você tenta adivinhar.
2 - Você pensa num número, e o computador tenta adivinhar.""")

    modo = int(input("\nEscolha o modo de jogo (1 ou 2). "))

    if modo == 1:
        computador_pensa()
    elif modo == 2:
        utilizador_pensa()
    else:
        print("Modo de jogo inválido. Escolha entre o modo 1 ou 2")

jogar()