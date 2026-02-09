from random import randint 
from time import sleep
def DadosIguais():
    contador = 0
    while True:
        contador += 1
        dadoUm = randint(1, 6)
        dadoDois = randint (1, 6)
    
        if dadoUm and dadoDois == 6:
            print(f"os dados ficaram ambos iguais a 6 em {contador} tentativas")
            input("Enter para terminar")
            break
        else:
            print(f"{contador} tentativa")
            sleep(1)

DadosIguais()