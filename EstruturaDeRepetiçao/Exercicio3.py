while True:
    try:
        nome = str(input("Informe o seu nome: "))
    except ValueError:
        print("Valor invalido.")
    else:
        if len(nome)>=3:
            break
        else:
            print("O nome informado precisa ter 3 ou mais letras.")
while True:
    try:
        idade = int(input("Informe a sua idade: "))
    except ValueError:
        print("Valor informado não é válido.Tente novamente.")
    else:
        if idade<0 or idade>150:
            print("Idade não possivel, tente novamente.")
        else:
            break
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
while True:
    try:
        sexo = str(input("informe o seu sexo com F ou M: "))
    except ValueError:
        print("Valor informado é inválido. Tente novamente.")
    else:
        if str.lower(sexo)=='f' or str.lower(sexo)=='m':
            break
        else:
            print("Valor inválido informado. Tente novamente. ")
while True:
    try:
        estadoCivil = str(input("Informe o seu estado civil com s=solteiro,c=casado,d=divorciado"
                          ",v=viuvo: "))
    except ValueError:
        ("Valor inválido informado. Tente novamente.")
    else:
        if str.lower(estadoCivil) == "s":
            if sexo == 'm':
                estadoCivil = 'solteiro'
            else:
                estadoCivil = 'solteira'
            break
        elif str.lower(estadoCivil) == "c":
            if sexo == 'm':
                estadoCivil = 'casado'
            else:
                estadoCivil = 'casada'
            break
        elif str.lower(estadoCivil) == 'v':
            if sexo == 'm':
                estadoCivil = 'viuvo'
            else:
                estadoCivil = 'viuva'
            break
        elif str.lower(estadoCivil) == 'd':
            if sexo == 'm':
                estadoCivil = 'divorciado'
            else:
                estadoCivil = 'divorciada'
print(f'Seu nome é {nome},idade {idade}, salario {salario}, sexo {sexo} e estado civil'
      f' {estadoCivil}')