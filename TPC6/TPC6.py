def menu():
    escola = [] # Variavel Interna
    v = True 
    while v == True:
        print("""\n===== Menu =====
(1): Criar uma turma;
(2): Inserir um aluno na turma;
(3): Listar a turma;
(4): Consultar um aluno por id;
(5): Guardar a turma em ficheiro;
(6): Carregar uma turma dum ficheiro;
(0): Sair da aplicação""") 
        modo = int(input("Que modo deseja? "))

        if modo == 1:
            cria_turma(escola)
        elif modo == 2:
            inserir_aluno(escola)
        elif modo == 3:
            listar_turma(escola)
        elif modo == 4:
            consultar_aluno(escola)
        elif modo == 5:
            guardar(escola)
        elif modo == 6:
            escola = carregar("escola.txt")
        elif modo == 0: 
            print("Programa Encerrado.")
            v = False
        else:
            print("Insira um modo válido!")

# Criar uma Turma
def cria_turma(escola):
    add = str.lower(input("Quer adicionar uma turma (s/n)? "))
    
    if add == "s":
        escola.append([])
        print("Turma adicionada!")
    else:
        print("Turma não adicionada!")
    print(f"Atualmente há {len(escola)} turmas.")

# Inserir aluno numa turma 
def inserir_aluno(escola):
        listar_turma(escola)
        turma = int(input(f"\nA que turma deseja adicionar?")) - 1 # -1 para ajustar ao indice 
        if turma > len(escola):
            print("ERRO! Insira uma turma válida.")
        else:
            nome_aluno = (str(input("Nome do aluno? ")))
            id_aluno = (str(input("Id do aluno? ")))
            notas = []
            notaTPC = float(input("Nota do TPC? "))
            notaPROJ = float(input("Nota do Projeto? "))
            notaTESTE = float(input("Nota do Teste? "))
            notas.append(notaTPC)
            notas.append(notaPROJ)
            notas.append(notaTESTE)
            aluno = (nome_aluno, id_aluno, notas)
            escola[turma].append(aluno)

# Listar todas as turmas
def listar_turma(escola):
    contador_turma = 1
    for turma in escola:
        print(f"\nTurma {contador_turma}:")
        for aluno in turma:
            print(f"{aluno[0]}(id:{aluno[1]})| Nota TPC: {aluno[2][0]}; Nota Projeto: {aluno[2][1]}; Nota Teste: {aluno[2][2]}")
        contador_turma += 1

# Consultar aluno por id na escola
## Cada linha do documento será uma turma
### Cada aluno está separado por "::"         
def consultar_aluno(escola):
        num_turma = 0
        aluno_encontrado = False
        id = input("Qual é o id que deseja procurar? ")
        for turma in escola:
            num_turma += 1
            for aluno in turma:
                if aluno[1] == id:
                    print(f"""\nO aluno com o id {id} é da turma {num_turma}:
{aluno[0]}(id:{aluno[1]})| Nota TPC: {aluno[2][0]}; Nota Projeto: {aluno[2][1]}; Nota Teste: {aluno[2][2]}""")
                    aluno_encontrado = True
        if not aluno_encontrado:
            print(f"\nO aluno com id {id} não existe na escola")

# Guarda informações num documento de texto    
def guardar(escola):
    file = open("escola.txt", "w")
    file.write(linha(escola))
    file.close()
    print("Ficheiro guardado em escola.txt")

# Ler e converter as linhas do documento   
def linha(escola):
    res = ""
    for turma in escola:
        for aluno in turma:
            res += str(aluno[0]) + "," + str(aluno[1]) + "," + str(aluno[2][0])+ "," + str(aluno[2][1]) + "," + str(aluno[2][2])
            res +="::"
        res += "\n"

    return res

# Carregar as informações do documento para a lista "escola"       
def carregar(fnome):
    escola = []
    file = open(fnome, "r")
    for linha in file:
        if linha.strip() != "":
            turma =[] 
            alunoS = linha.strip().split("::")
            for aluno in alunoS:
                campos = aluno.split(",")
                
                if campos != ['']:
                    nome = campos[0]
                    id = campos[1]
                    notas = [float(campos[2]), float(campos[3]), float(campos[4])]
                    turma.append((nome, id, notas))
        escola.append(turma)
    file.close()
    print(f"Informações carregadas de {fnome}")

    return escola

menu()