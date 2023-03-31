import random

def main():
    print("Bem-vindo ao Jogo da Adivinhação!")
    print("Eu escolhi um número entre 1 e 100. Tente adivinhar qual é.")
    numero_secreto = random.randint(1, 100)
    numero_de_tentativas = 0
    while True:
        palpite = int(input("Digite seu palpite: "))
        numero_de_tentativas += 1
        if palpite < numero_secreto:
            print("Seu palpite está abaixo do número secreto.")
        elif palpite > numero_secreto:
            print("Seu palpite está acima do número secreto.")
        else:
            print(f"Parabéns! Você acertou em {numero_de_tentativas} tentativas!")
            break

if __name__ == '__main__':
    main()