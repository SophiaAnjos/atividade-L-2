n = int(input("Digite um número de 1 a 6: "))

nextenso = [
    "um",
    "dois",
    "três",
    "quatro",
    "cinco",
    "seis"
]
if n >= 1 and n <= 6:

    extenso = nextenso[n - 1]

    print("O número", n, "por extenso é:", extenso)
else:
    print("Número inválido. Digite um número de 1 a 6.")