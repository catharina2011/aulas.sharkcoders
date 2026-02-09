from random import randint

def Jmm():
    secret = randint (1, 100)
    contador = 0
    while True:
        contador += 1
        guess = int(input("\nadvinha o numero secreto "))
        if guess == secret:
            print(f"\nacertaste meu brother em {contador} vezes")
            break
        if guess > secret:
            print(f"\no numero secreto é menor do que {guess}")
        if guess < secret:
            print(f"\no numero secreto é maior do que {guess}")


Jmm()