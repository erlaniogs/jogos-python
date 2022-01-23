import forca
import advinhacao2

def escolhe_jogo():
    print("**************************")
    print("***** Escolha o jogo! ****")
    print("**************************")

    print("(1)Forca (2)Adivinhação")

    jogo = int(input("Qual jogo?"))

    if(jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando Adivinhação")
        advinhacao2.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()