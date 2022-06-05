import math

preco = 0
print("Para cancelar, digite uma string ou boolean.")
while True:
    try:
        produto = float(input("Informe o codigo do produto que voce deseja comprar: "))
    except ValueError:
        print(preco)
        break
    else:
        if produto<100:
            print("CODIGO INVALIDO.")
        elif produto >  105:
            print("CODIGO INVALIDO")
        else:
            if produto == 100:
                nome = "cachorro(s) quente(s)"
                un = int(input("quantos?"))
                preco = preco + 1.2*un
                print(f'Você pediu {un} {nome}, subtotal: {preco}')
            elif produto == 101:
                nome = "bauru(s) simples"
                un = int(input("quantos?"))
                preco = preco +1.30*un
                print(f'Você pediu {un} {nome}, subtotal: {preco}')
            elif produto == 102:
                nome = "bauru(s) com ovo"
                un = int(input("quantos?"))
                preco = preco +1.50*un
                print(f'Você pediu {un} {nome}, subtotal: {preco}')
            elif produto == 103:
                nome = "hamburguer(es)"
                un = int(input("quantos?"))
                preco = preco +1.20*un
                print(f'Você pediu {un} {nome}, subtotal: {preco}')
            elif produto == 104:
                nome = "cheeseburguer(es)"
                un = int(input("quantos?"))
                preco = preco +1.30*un
                print(f'Você pediu {un} {nome}, subtotal: {preco}')
            elif produto == 105:
                nome = "refrigerante(s)"
                un = int(input("quantos?"))
                preco = preco + 1.0 * un
                print(f'Você pediu {un} {nome}, subtotal: {preco}')
