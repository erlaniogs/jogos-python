import random

def jogar():
    print("************************************************************")
    print("********** Bem-vindo ao mundo Python jogo de forca *********")
    print("************************************************************")

    arquivo = open("palavras.txt", "r")
    poss_palavras = []

    for linha in arquivo:
        linha = linha.strip()
        poss_palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(poss_palavras))
    palavra_secreta = poss_palavras[numero].upper()

#    palavra_secreta = "banana".upper()
#    letras_acertadas = ["_","_","_","_","_","_"]
#    poderia ser implementado:
#    for letra in palavra_secreta:
#        letras_acertadas.append("_")
    letras_acertadas = ["_" for letra in palavra_secreta] # List Comprehension

    enforcou = False
    acertou  = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual a letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
        #            print("Encontrei a letra {} na posição {}".format(chute, index+1))
                index +=1
        else:
            erros +=1
            print("Você errou e tem somente {}".format(6-erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você ganhou")
    else:
        print("Você perdeu")

    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()
