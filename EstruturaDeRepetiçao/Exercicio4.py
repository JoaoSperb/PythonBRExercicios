a = 80000
b = 200000
anos = 0
while True:
    if a>b:
        print(f"A quantidade de anos necessaria para cidade A ter mais habitantes foi {anos}")
        break
    a *= 1.03#mesma coisa que a = a*1.03
    b *= 1.015
    anos = anos + 1
