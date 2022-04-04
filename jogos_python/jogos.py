import forca
import adivinhacao

print("=============================================")
print("ESCOLHA SEU JOGO")
print("=============================================")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo? "))

if (jogo == 1):
    print("forca")
    forca.jogar()
elif (jogo == 2):
    print("adivinhação")
    adivinhacao.jogar()
else:
    print("Opção inválida")
