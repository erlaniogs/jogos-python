import random

def jogar():
    print("**************************************************************")
    print("**Bem-vindo ao mundo Python jogo de adivinhação com loop for**")
    print("**************************************************************")

    # Possibilidades números secretos  (digitados, aleatórios arredondados, utilizando função Python)
    # numero_secreto = 43
    # numero_secreto = round(random.random()*100)
    numero_secreto = random.randrange(1,101)
    tentativas = 0
    pontuacao = 1000

    print("Qual o nível de dificuldade?")
    print("(1)Fácil (2)Médio (3)Difícil")

    nivel = int(input("Defina o nível de dificuldade:"))

    if(nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1,tentativas + 1):
        print("Tentativa {} de {} ".format(rodada, tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 0 e 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos".format(pontuacao))
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontuacao = pontuacao - pontos_perdidos

            if (maior):
                print("Você errou. Chute maior que número secreto")
                if (rodada == tentativas):
                    print("Acabaram as tentativas")
                    print("O número secreto era {} e você fez {} pontos".format(numero_secreto, pontuacao))
            elif (menor):
                print("Você errou. Chute menor que número secreto")
                if (rodada == tentativas):
                    print("Acabaram as tentativas")
                    print("O número secreto era {} e você fez {} pontos".format(numero_secreto, pontuacao))

    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()