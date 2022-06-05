maior = -1
menor = 200
tamanho = int(input("Informe o tamanho da lista"))
for _ in range(tamanho):
    numero = int(input(f"Informe {tamanho} numeros"))
    menor = min(menor, numero)
    maior = max(maior, numero)  # quase a mesma coisa que no java, so que tem um metodo para isso

print(maior)
print(menor)
