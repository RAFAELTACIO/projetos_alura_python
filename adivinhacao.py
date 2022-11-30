from random import randrange

print("--------------------------------")
print('BEM VINDO AO JOGO DE ADIVINHAÇÃO')
print("--------------------------------")

var=randrange(0,100)
print(var)

print("TENTE ADIVINHAR UM NUMERO ENTRE 0 E 100")

for i in range(3):
    resposta = input("DIGITE UM NUMERO: ")
    resposta_int = int(resposta)

    if resposta_int == var:
        print("PARABENS VOCE ACERTOU!!!")
        break
    elif i == 2:
        print("VOCE PERDEU!!!")
        break
    elif i < 3:
        print("Você ainda tem mais", 2-i,"chances")