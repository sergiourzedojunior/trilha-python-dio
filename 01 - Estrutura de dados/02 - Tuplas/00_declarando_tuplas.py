frutas = (
    "laranja",
    "pera",
    "uva",
)
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",)
print(pais)

def min_max(lista):
    return min(lista), max(lista)

resultados = min_max([1, 2, 3, 4, 5])
print(resultados)  # (1, 5)


pares = [("maçã", "vermelho"), ("banana", "amarelo"), ("uva", "roxo")]
for fruta, cor in pares:
    print(f"A {fruta} é {cor}")