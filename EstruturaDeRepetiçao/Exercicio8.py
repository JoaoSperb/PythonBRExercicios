"""
Programa interessante, faz um loop 5 vezes, solicitando necessariamente um numero do tipo
float. Em seguida, mostra a soma e a media desses 5 valores, assim como o maior e o menor.
"""
soma = 0
maior = -1
menor = 12341238

for _ in range(5):
    while True:
        try:
            numero = float(input("Informe um valor inteiro: "))
        except ValueError:
            print("é necessario ser informado um número inteiro.")
        else:
            break
    soma = soma + numero
    maior = max(maior,numero)
    menor = min(menor,numero)
media = soma/5
print(f"A soma dos 5 números é {soma} e a média é {media}")
print(f"O maior dos valores é {maior} e o menor deles é {menor}")
