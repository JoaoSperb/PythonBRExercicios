import math
"""
Programa interessante, usando math.ceil para arredondar os numeros para cima e round()
para limitar as casas decimais. math.floor arredonda para baixo
"""
print("")
area = int(input("Informe a area, em metros quadrados a ser pintada: "))
area_com_folga = area * 1.1
litros_por_metro = area_com_folga/6  # 6 metros por litro
latas_de_18 = litros_por_metro/18
galoes_de_3 = litros_por_metro/3.6
print("A quantidade de litros necessaria era ", round(litros_por_metro, 2), " latas de 18: ",
      math.ceil(latas_de_18), " Galoes de 3: ", math.ceil(galoes_de_3))
preco_latas = math.ceil(latas_de_18)*80
print("O preço a ser pago se comprar latas de 18: R$", preco_latas)
preco_galoes = math.ceil(galoes_de_3)*25
print("O preço a ser pago se comprar galoes de 3: R$", preco_galoes)
latas_de_18 = math.floor(litros_por_metro/18)
preco_latas = latas_de_18*80
litros_faltantes = litros_por_metro%18
galoes_de_3 = math.ceil(litros_faltantes/3.6)
preco_galoes = galoes_de_3*25
print("voce deve usar ", latas_de_18, "latas, e para o que faltou, serao necessarios ",
      galoes_de_3, " de 3,6. Tudo isso custando ", preco_galoes + preco_latas)
