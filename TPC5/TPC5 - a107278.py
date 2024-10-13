# Menu
def menu():
    cinema = [] # Variavel Interna
    v = True 
    while v == True:
        print("""\n===== Menu =====
(1) Inserir Salas 
(2) Listar Filmes
(3) Disponibilidade de Lugar
(4) Editar Salas
(5) Vender Bilhete
(0) Sair do Programa""") 
        modo = int(input("Que modo deseja? "))

        if modo == 1:
            inserir_salas(cinema)
        elif modo == 2:
            if len(cinema) == 0:
                print("Não há salas!")
            else:
                listar_filmes(cinema)
        elif modo == 3:
            if len(cinema) == 0:
                print("Não há salas!")
            else:
                listar_disponibilidade(cinema)
        elif modo == 4:
            if len(cinema) == 0:
                print("Não há salas!")
            else:
                editar_salas(cinema)
        elif modo == 5:
            if len(cinema) == 0:
                print("Não há salas!")
            else:
                vender_bilhetes(cinema)
        elif modo == 0: 
            print("Programa Encerrado.")
            v = False
        else:
            print("Insira um modo válido!")
 
 # Inserir Salas
def inserir_salas(cinema):
    s = int(input(f"""\nQuantas salas quer adicionar?
Atualmente há {len(cinema)} salas. """))
    while s > 0:
        sala = []
        
        print("\nNova sala")
        num_lugares = int(input("Número de lugares? "))
        lugares = list(range(1, num_lugares + 1))
        sala.append(lugares)

        vendidos = 0
        sala.append(vendidos)

        filme = str(input("Nome do filme? "))
        sala.append(filme)
        s -= 1
        
        lugares_interditos = 0
        sala.append(lugares_interditos)
        
        cinema.append(sala)
    
    return cinema

# Listar Filmes
def listar_filmes(cinema):
    if len(cinema) == 0:
        print("\nAtualmente não há salas.")
    else:
        for idx, sala in enumerate(cinema):
            print(f"""\nSala {idx + 1}:
- Filme: {sala[2]}""")

# Listar Disponibilidade
def listar_disponibilidade(cinema):
    if len(cinema) == 0:
        print("\nAtualmente não há salas.")
    else:
        for idx, sala in enumerate(cinema):
            print(f"""\nSala {idx + 1}:
- Filme: {sala[2]}
- Lugares: {len(sala[0])}""")
            for idx, lugar in enumerate(cinema[idx][0]): # Demonstrar a disposição da sala
                print(lugar, end=' ') 
                if (idx + 1) % 10 == 0:
                    print()
            print(f"""- Bilhetes vendidos: {sala[1]}
- Lugares disponiveis: {len(sala[0]) - sala[1] - sala[3]}
- Lugares interditos: {sala[3]}""")

# Editar Salas
def editar_salas(cinema):
    v = True
    while v == True:
        print("""\n(1) Mudar nome do filme 
(2) Remover Filme 
(3) Interditar Lugares
(0) Voltar ao Menu """)

        modo = int(input("Que modo deseja? "))
        if modo == 1:
            sala_desejada = int(input(f"\nEscolha uma sala (1 a {len(cinema)}): ")) - 1
            if 0 <= sala_desejada < len(cinema):
                cinema[sala_desejada][2] = str(input("Nome do Filme? "))
                print(f"Filme alterado!")
            else:
                print("Número da sala inválido.")
        elif modo == 2:
            sala_desejada = int(input(f"\nEscolha uma sala (1 a {len(cinema)}): ")) - 1
            if 0 <= sala_desejada < len(cinema):
                cinema[sala_desejada][2] = "Sem Filme"
                print(f"Filme removido!")
        elif modo == 3:
            sala_desejada = int(input(f"\nEscolha uma sala (1 a {len(cinema)}): ")) - 1
            if 0 <= sala_desejada < len(cinema):
                lugar = int(input(("Que lugar deseja interditar? ")))
                for idx, numero in enumerate(cinema[sala_desejada][0]):
                    if numero == lugar:  
                        cinema[sala_desejada][0][idx] = "(!)"
                        print("Lugar interdito!")  
                        cinema[sala_desejada][3] += 1
            else:
                print("Sala Inválida")  
        elif modo == 0: 
            print("Programa Encerrado.")
            v = False
        else:
            print("Insira um modo válido!")

# Vender Bilhetes
def vender_bilhetes(cinema):
    sala_desejada = int(input(f"\nEscolha uma sala (1 a {len(cinema)}): ")) - 1  # Subtrai 1 para ajustar o índice
    if not cinema[sala_desejada][2] == "Sem Filme":
        v = int(input("Quantos bilhetes quer comprar? "))
        if 0 <= sala_desejada < len(cinema):
            sala = cinema[sala_desejada]
            if len(sala[0]) - sala[1] > v:
                sala[1] += v      
            else:
                print("Número da sala inválido.")
        for idx, lugar in enumerate(cinema[sala_desejada][0]): 
                    print(lugar, end=' ') 
                    if (idx + 1) % 10 == 0:
                        print()
        while v > 0:
            lugar = int(input(("Que lugar deseja? ")))
            if lugar in cinema[sala_desejada][0]:
                for idx, numero in enumerate(cinema[sala_desejada][0]):
                    if numero == lugar:  
                        cinema[sala_desejada][0][idx] = "(-)"
                        v -= 1
            else:
                print("Esse lugar já está ocupado.")
        cinema[sala_desejada][1] += v
    else:
        print("Sala sem filme!")

menu()