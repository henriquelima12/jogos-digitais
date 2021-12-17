#Henrique Lima Araújo - 32091702

import random

def lancar():
    input("Clique enter para lançar os dados")
    dado1 = random.randrange(1, 7)
    dado2 = random.randrange(1, 7)
    soma = dado1 + dado2
    print("Dado 1: ", dado1)
    print("Dado 2: ", dado2)
    print("Soma dos dados: ", soma)
    return soma


def main():
    jogadas = 0
    contador = 0

    while contador == 0:
        jogadas = jogadas + 1
        dados = lancar()
        if dados == 7 or dados == 11:
            print("Você ganhou!")
            contador = contador + 1
        elif dados == 2 or dados == 3 or dados == 12:
            print("Você perdeu!")
            contador = contador + 1
        else:
            print('Ponto')
            contador2 = 0
            while contador2 == 0:
                next = lancar()
                jogadas = jogadas + 1
                if next == 2 or next == 3 or next == 12:
                    print("Você perdeu!")
                    contador2 = contador2 + 1
                elif next == 7:
                    print("Você perdeu!")
                    contador2 = contador2 + 1
                elif next == dados:
                    print("Você ganhou")
                    contador2 = contador2 + 1
                else:
                    print('Ponto')
                    print("Jogue novamente")
            contador = contador + 1
    print("Quantidade de jogadas: " ,jogadas)


main()
