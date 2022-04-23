saque = int(input("Informe o valor do saque: "))

notas_de_100, saque = divmod(saque, 100)
if notas_de_100>0:
    print(f'{notas_de_100} notas de 100')
notas_de_50, saque = divmod(saque, 50)
if notas_de_50>0:
    print(f'{notas_de_50} notas de 50')
notas_de_10, saque = divmod(saque, 10)
if notas_de_10>0:
    print(f'{notas_de_10} notas de 10')
notas_de_5, saque = divmod(saque,5)
if notas_de_5>0:
    print(f'{notas_de_5} notas de 5                           ')
notas_de_1, saque = divmod(saque, 1)
if notas_de_1>0:
    print(f"{notas_de_1} notas de 1")
