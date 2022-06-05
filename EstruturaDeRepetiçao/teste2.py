while True:
    try:
        salario = int(input("Informe o seu salário."))
    except ValueError:
        print("Valor informado nao é valido.")
    else:
        if salario<0:
            print("Salario inválido.Tente novamente")
        else:
            break
print(salario)