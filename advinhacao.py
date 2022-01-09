print("**************************************************************")
print("Bem-vindo ao mundo Python começando com um jogo de adivinhação")
print("**************************************************************")

numero_secreto = 43
tentativas = 3
rodada = 1

while(rodada <= tentativas):
    print("Tentativa {} de {} ".format(rodada, tentativas))
    chute = int(input("Digite um número: "))

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou")
    else:
        if (maior):
            print("Você errou. Chute maior que número secreto")
        elif (menor):
            print("Você errou. Chute menor que número secreto")

    rodada = rodada + 1

print("Fim do jogo!")