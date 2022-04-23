#EXERCICIO1
x = int(input("Informe um numero"))
y = int(input("Informe outro numero"))
if x > y:
    print(x)
else:
    print(y)

#EXERCICIO2
x = int(input("Informe um numero"))
if x==0:
    print("x e zero")
elif x<0:
    print("x e negativo")
else:
    print("x e positivo")

#EXERCICIO3
sexo = input("Informe seu sexo popr M ou F")
sexo = sexo.upper()
if sexo == 'M':
    print("Masculino")
else:
    print("Feminino")
