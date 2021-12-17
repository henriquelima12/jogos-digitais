#Henrique Lima Araújo - 32091702

def pagamento(vP, dA):
    if dA == 0:
        valor = vP
    else:
        valor = vP +(vP * 0.03) + (vP * (0.001 * dA))
    return valor


def main():
    contador = 0
    quantidade = 0
    total = 0
    while(contador == 0):
        prestacao = float(input("Digite o valor da prestação: "))
        if prestacao == 0:
            contador = contador + 1
        else:
            atraso = float(input("Digite a quantidade de dias em atraso: "))
            print("O valor da prestação é: " ,pagamento(prestacao, atraso), "R$")
            quantidade = quantidade + 1
            total = total + pagamento(prestacao, atraso)

    print("Quantidade de prestações pagas: " ,quantidade)
    print("Valor total das prestações pagas: " ,total, "R$")


main()



