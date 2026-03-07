segredo = 42
tentativas = 0
print("Bem-vindo ao Jogo da Adivinhação!")
while True:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1
    if palpite < segredo:
        print("Muito baixo! Tente novamente.")
    elif palpite > segredo:
        print("Muito alto! Tente novamente.")
    else:
        print("Parabéns! Você acertou o número!")
        break
print("Você acertou o número em " + str(tentativas) + " tentativas.")