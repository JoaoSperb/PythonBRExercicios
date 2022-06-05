"""
usos do comando str em a para conseguir utilizar o [::1] e filtro de valores não validos
"""

while True:
    try:
        a = int(input("numero"))
    except ValueError:
        print("è necessario ser um numero inteiro e positivo.")
    else:
        if a < 0:
            print("Somente numeros positivos")
        else:
            contrario = str(a)[::-1]
            print(contrario)
            
            zap = int(str(a)[::-1])
            print(type(zap))
            break
