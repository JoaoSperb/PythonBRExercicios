"""
Programa que solicita numero indeterminado de valores até o numero -1 ser digitado,
depois calcula e mostra uma analise sobre a lista.
"""
lista = []
while True:
    try:
        notas = float(input("Informe os valores de suas notas, digite -1 para parar: "))
        if notas == -1:
            break
        else:
            lista.append(notas)
    except ValueError:
        print("Valor informado é inválido.")

soma_das_notas = sum(lista)
total_de_valores = len(lista)
media = soma_das_notas/total_de_valores
print(lista)
print(total_de_valores)
lista.reverse()
print(lista)
print(soma_das_notas)
print(media)
acima = 0
abaixo = 0
valores_acima_da_media = []
valores_abaixo_de_7 = []
for valor_media in lista:
    if valor_media >= media:
        acima = + 1
        valores_acima_da_media.append(valor_media)
    if valor_media < 7:
        abaixo = + 1
        valores_abaixo_de_7.append(valor_media)
print(f'A quantidade de valores acima ou na média foi {acima}'
      f' e a quantidade de valores abaixo de 7 foi {abaixo}')

print('Os valores acima da media foram: ', valores_acima_da_media)
print('As notas abaixo de 7 foram: ', valores_abaixo_de_7)
