"""
Exercicio que lê 5 valores inteiros e os coloca na lista.

listas podem armazenar qualquer tipo primitivo simultaneamente(menos boolean).
lista = [1,2,1.2,71.0,'String',[]]
lista.append(10) <-acrescenta o numero 10 ao final da lista.
"""
lista = []
for _ in range(5):
    numero = int(input("Informe um valor inteiro."))
    lista.append(numero)
print(lista)
