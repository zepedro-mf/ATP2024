def menu():
    tabmeteo = []
    v = True 
    while v == True:
        print("""\n===== Menu =====
(1): Temperatura média;
(2): Guardar tabela num ficheiro;
(3): Carregar tabela de um ficheiro;
(4): Temperatura mínima mais baixa;
(5): Valor mais alto de percipitação;
(6): Número de dias com a percipitação superior a "x";
(7): Maior número de dias consecutivos com percipitação abaixo de "x";
(8): Gráfico de temperatura máxima e mínima;
(9): Gráfico de pluviosidade;
(0): Sair da aplicação""") 
        modo = int(input("Que modo deseja? "))

        if modo == 1:
            medias(tabmeteo)
        elif modo == 2:
            guardaTabMeteo(tabmeteo, "C:\\Users\\ze05p\\OneDrive\\Documentos\\Licenciatura em Engenharia Biomédica\\2º Ano\\1º Semestre\\Algoritmos e Técnicas de Programação\\Os meus Noteebooks\\TPC7\\meteorologia.txt")
        elif modo == 3:
            tabmeteo = carregaTabMeteo("C:\\Users\\ze05p\\OneDrive\\Documentos\\Licenciatura em Engenharia Biomédica\\2º Ano\\1º Semestre\\Algoritmos e Técnicas de Programação\\Os meus Noteebooks\\TPC7\\meteorologia.txt")
            print(tabmeteo)
        elif modo == 4:
            minMin(tabmeteo)
        elif modo == 5:
            maxChuva(tabmeteo)
        elif modo == 6:
            p = float(input("Que limite deseja? "))
            diasChuvosos(tabmeteo, p)
        elif modo == 7:
            p = float(input("Que limite deseja? "))
            maxPeriodoCalor(tabmeteo, p)
        elif modo == 8:
            grafTabMeteoTemp(tabmeteo)
        elif modo == 9:
            grafTabMeteoPulv(tabmeteo)
        elif modo == 0: 
            print("Programa Encerrado.")
            v = False
        else:
            print("Insira um modo válido!")

def medias(tabMeteo):
    res = []
    for info in tabMeteo:
        med = (info[0], (info[1] + info[2])/2)
        res.append(med)
    return print(f"""O valor médio dos dias é:
{res}""")

def guardaTabMeteo(t, fnome):
    file = open(fnome, "w")
    for data, tmin, tmax, precip in t:
        linha = f"{data[0]}::{data[1]}::{data[2]}::{tmin}::{tmax}::{precip}\n"
        file.write(linha)
    file.close()
    print("Ficheiro guardado.")
    return 

def carregaTabMeteo(fnome):
    res = []
    file = open(fnome, "r")
    for linha in file:
        if linha.strip() != "":
            campos = linha.strip().split("::")
            data = (int(campos[0]), int(campos[1]), int(campos[2]))
            dia = (data, float(campos[3]), float(campos[4]), float(campos[5]))
            res.append(dia)
    file.close()
    print("Ficheiro carregado.")
    return res

def minMin(tabMeteo):
    min = float(tabMeteo[0][1])
    for _, tmin, _, _ in tabMeteo: # ou for _, tmin, *_
        if tmin < min:
            min =  tmin
    return print(f"O valor mínimo de temperatura mais baixo é {min}ºC.")


def amplTerm(tabMeteo):
    res = []
    for data, tmin, tmax, _ in tabMeteo:
        amp =  tmax - tmin
        res.append((data, amp))
    return print(f"""A amplitude térmica dos dias é:
{res}""")

def maxChuva(tabMeteo):
    max_prec = float(tabMeteo[0][3])
    max_data = tabMeteo[0][0]
    for data, _, _, prec in tabMeteo: 
        if prec > max_prec:
            max_prec = prec
            max_data = data
    return print(f"O valor mais alto de percipitação foi {max_prec}mm/m^2 no dia {max_data}.")

def diasChuvosos(tabMeteo, p):
    res = []
    for data, _, _, prec in tabMeteo:
        if prec > p:
            res.append((data, prec))
    return print(F"""Os dias em que a percipitação foi superior a {p}mm/m^2 foram:
{res}""")

def maxPeriodoCalor(tabMeteo, p):
    res = 0
    consecutivo = 0
    for _, _, _, prec in tabMeteo:
        if prec < p:
            res += 1
            if res > consecutivo:
                consecutivo = res
        else:
            res = 0
    return print(f"O maior número de dias consecutivos em que a percipitação foi menor que {p} foram {consecutivo} dias.")

import matplotlib.pyplot as plt
def grafTabMeteoTemp(t):
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    for data, tmin, tmax, _ in t:
        x1.append(str(data))
        y1.append(float(tmin))
        x2.append(str(data))
        y2.append(float(tmax))

    plt.plot(x1, y1, label = "Temperatura mínima")
    plt.plot(x2, y2, label = "Temperatura máxima")
    plt.xlabel('Dias')
    plt.ylabel('Temperatura')
    plt.title('Temperaturas máxmias e mínimas')
    plt.legend()
    plt.show()

def grafTabMeteoPulv(t):
    x = []
    y = []
    for data, _, _, prec in t:
        x.append(str(data))
        y.append(float(prec))
    
    plt.bar(x, y, label = "Pluviosidade")
    plt.xlabel("Dias")
    plt.ylabel("mm/m^2")
    plt.title("Precipitação")
    plt.legend()
    plt.show()

menu()