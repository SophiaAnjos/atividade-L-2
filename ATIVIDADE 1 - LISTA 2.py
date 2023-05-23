nascimento = int(input("Em que ano de nascimento: "))
ano_atual = int(input("Qual o ano atual: "))
futuro = int(input("Digite o ano para fazer a comparação: "))

idade_atual = ano_atual - nascimento

#CALCULO IDADE FUTURA
idade_futura = futuro - nascimento

#EXIBICAO
print("Idade atual:", idade_atual, "anos")
print("Idade em 2099:", idade_futura, "anos")