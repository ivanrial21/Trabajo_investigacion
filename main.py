def calcular_promedio(lista_numeros):
    return sum(lista_numeros) / len(lista_numeros) if lista_numeros else 0

def es_primo(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def es_palindromo(texto):
    texto = str(texto).lower().replace(" ", "")
    return texto == texto[::-1]