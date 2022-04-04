import random


def jogar():
    print("=============================================")
    print("JOGO DE ADVINHAÇÃO")
    print("=============================================")

    numero_secreto = random.randrange(1, 101)
    tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        tentativas = 20
    elif (nivel == 2):
        tentativas = 10
    elif (nivel == 3):
        tentativas = 5
    else:
        print("Número invalido.")

    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada, tentativas))
        chute = input("Digite um número entre 1 e 100: ")
        print("você chutou o número: {}".format(chute))
        chute = int(chute)

        if (chute < 1 or chute > 100):
            print("numero invalido tente novamente")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Parabéns você acertou!! E fez {} pontos".format(pontos))
            break
        elif (maior):
            print("Errou! seu chute foi maior que o número")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        elif (menor):
            print("Errou! seu chute foi menor que o número")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

if(__name__ == "__main__"):
    jogar()