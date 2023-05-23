cod = int(input("Digite o código do item: "))
quant = int(input("Digite a quantidade: "))

if cod == 100:
    preco_unitario = 18.50
elif cod == 101:
    preco_unitario = 21.30
elif cod == 102:
    preco_unitario = 19.20
elif cod == 103:
    preco_unitario = 22.30
elif cod == 104:
    preco_unitario = 25.00
elif cod == 105:
    preco_unitario = 5.00
else:
    print("Código de item inválido.")
    exit()
valor_total = preco_unitario * quant
print("O valor total a ser pago é: R$", valor_total)