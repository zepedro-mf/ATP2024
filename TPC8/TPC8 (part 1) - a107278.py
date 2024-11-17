# TPC1
print("\n>>>>> TPC1 <<<<<")
## a)
print("=== a) ===")
def comuns(a, b):
    res = [num for num in a if num not in b] + [num for num in b if num not in a]
    return res

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8] 
print(comuns(lista1, lista2))


## b)
print("\n=== b) ===")
def palavra3(texto):
    res = [palavra for palavra in texto.split(" ") if len(palavra) >= 3]
    return res

texto = """Vivia há já não poucos anos algures num concelho do Ribatejo 
    um pequeno lavrador e negociante de gado chamado Manuel Peres Vigário"""
print(palavra3(texto))


## c)
print("\n=== c) ===")
def indice(lista):
    res = [(indice, palavra) for indice, palavra in enumerate(lista)]
    return res

lista = ['anaconda', 'burro', 'cavalo', 'macaco']
print(indice(lista))


# TPC2
print("\n>>>>> TPC2 <<<<<")
## a)
print("=== a) ===")
def strCount(s, subs):
    lista = s.split(subs)
    return (len(lista) - 1)

print(strCount("catcowcat", "cat")) # --> 2
print(strCount("catcowcat", "cow")) # --> 1
print(strCount("catcowcat", "dog")) # --> 0d


## b)
print("\n=== b) ===")
def produtoM3(lista):
    min = sorted(lista)[:3]
    return print(f"{min[0]} * {min [1]} * {min[2]} = {min[0] * min [1] * min[2]}")
    
produtoM3([12,3,7,10,12,8,9])


## c)
print("\n=== c) ===")
def reduxInt(n):
    while n >= 10:  # Continua enquanto o número tiver mais de um dígito            
        soma = 0      
        while n > 0:  # Soma cada dígito do número
            soma += n % 10  # Adiciona o último dígito ao somatório
            n //= 10 # tirar o ultimo digito
        n = soma  # Atualiza o número com a soma dos dígitos
    return n

print(reduxInt(38))   # Output: 2
print(reduxInt(777))  # Output: 3
print(reduxInt(1234)) # Output: 1


## d)
print("\n=== d) ===")
def myIndexOf(s1, s2):
    lista = s1.split(" ")
    encontrado = False
    contador = 0
    for palavra in lista:
        contador += 1
        if palavra == s2:
            encontrado = True
            res = contador
    if not encontrado:
        res = -1
    return res
    
print(myIndexOf("Hoje está um belo dia de sol!", "belo"))
print(myIndexOf("Hoje está um belo dia de sol!", "chuva"))

