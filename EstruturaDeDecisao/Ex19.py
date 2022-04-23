"""
3//5 é  o equivalente a 3/5 no java
"""

x = int(input("Informe um numero até 1000: "))
if x>=1000:
    print("Digite um numero ATÉ 1000")
else:
    centenas = 0;
    dezenas = 0
    unidades = 0
    resto = 0
    centenas = x//100
    resto = x%100
    dezenas = resto//10
    resto = resto%10
    unidades = resto//1
    print(centenas, " centenas ", dezenas, " dezenas ",unidades, " unidades")