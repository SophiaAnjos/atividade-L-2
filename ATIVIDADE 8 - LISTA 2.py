n = int(input("Digite um número de 1 a 7: "))

dsemana = [
    "Domingo",
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
    "Sábado"
]

if n >= 1 and n <= 7:
    dia_semana = dsemana[n - 1]

    print("O dia da semana correspondente ao número", n, "é:", dia_semana)
else:
    print("Número inválido. Digite um número de 1 a 7.")