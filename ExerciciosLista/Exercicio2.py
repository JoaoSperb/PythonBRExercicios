"""
Exercicio que mostra uma lista ao contrario.
"""
lista = []
for _ in range(10):
    numero = float(input("Informe um valor inteiro."))
    lista.append(numero)
lista.reverse()
print(lista)
