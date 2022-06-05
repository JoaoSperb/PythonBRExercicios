preco = 0
while True:
    produto = int(input("Informe o codigo do produto que voce deseja comprar"))
    if produto==0:
        print(preco)
        break
    elif produto<100:
        print("CODIGO INVALIDO.")
    elif produto >  105:
        print("CODIGO INVALIDO")
    else:
        if produto == 100:
            preco = preco + 1.2
        elif produto == 101:
            preco = preco +1.30
        elif produto == 102:
            preco = preco +1.50
        elif produto == 103:
            preco = preco +1.20
        elif produto == 104:
            preco = preco +1.30
        elif produto == 105:
            preco = preco +1.0
