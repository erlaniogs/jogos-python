import random
def jogar():

    inicializacao()
    palavra_secreta = criar_palavra()

    letras_acertadas = mostra_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou  = False
    erros = 0

    while(not enforcou and not acertou):

        chute = chuta()

        if(chute in palavra_secreta):
            mostra_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros +=1
            desenha_forca(erros)
            #print("Você errou e tem somente {}".format(6-erros))

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        imprime_vencedor()
    else:
        imprime_perdedor(palavra_secreta)


# Definição das funções

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def inicializacao():
    print("************************************************************")
    print("********** Bem-vindo ao mundo Python jogo de forca *********")
    print("************************************************************")

def criar_palavra():
    arquivo = open("palavras.txt", "r")
    poss_palavras = []
    for linha in arquivo:
        linha = linha.strip()
        poss_palavras.append(linha)
    arquivo.close()
    numero = random.randrange(0, len(poss_palavras))
    palavra_secreta = poss_palavras[numero].upper()
    return palavra_secreta

def mostra_acertadas(palavra):
    lista = ["_" for letra in palavra] # List Comprehension
    return lista

def chuta():
    chute = input("Qual a letra? ")
    chute = chute.strip().upper()
    return chute

def mostra_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        #            print("Encontrei a letra {} na posição {}".format(chute, index+1))
        index += 1

#    Codificação inicial
#    palavra_secreta = "banana".upper()
#    letras_acertadas = ["_","_","_","_","_","_"]
#    poderia ser implementado:
#    for letra in palavra_secreta:
#        letras_acertadas.append("_")

if(__name__ == "__main__"):
    jogar()
