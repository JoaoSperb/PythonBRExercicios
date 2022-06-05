"""while True permanece executando os testes ate receber o comando break
por isso, ao digitar um numero entre 0 e 10 o programa encerra. Caso o contrário, se voce
informar um valor String,double ou um numero menor que zero ou maior que 10, o programa
informa o erro no input, e o computador so para de perguntar quando for digitado um valor
entre 0 e 10.
As chamadas exceçoes, sao tratadas com o try, por isso, no caso de um loop infinito, o
programa continua solicitando um input correto do usuário. Um exemplo de como funciona o try
esta na classe teste.
"""

while True:
    try:
        numero = int(input("Informe um numero de 0 a 10: "))
    except ValueError:
        print("Informe um valor inteiro.")
        #Linha de cima aparece na tela se o usuario digitar algo que nao seja inteiro.
    else:
        if 0<=numero<=10:
            print(f'Numero informado é {numero}')
            break
        else:
            print("O numero precisa estar entre 0 e 10.")