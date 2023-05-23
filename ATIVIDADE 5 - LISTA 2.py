n = int(input("Digite um número para a tabuada: "))

for i in range(1, 11): # laço de repetição
    resultado = n * i
    print(n, "x", i, "=", resultado)