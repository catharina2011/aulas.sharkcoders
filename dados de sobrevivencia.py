import os
from random import randint

def Limpar():
    os.system("cls")

def Cabecalho (texto):
    Limpar()
    tamanho = len(texto) + 6
    print()
    print("="*tamanho)
    print(f"|| {texto} ||")
    print("="*tamanho)

def DadosDaSobrevivencia():
    print("- Neste jogo deves rolar o dado que decidirá a tua sobrevivencia. ") 
    print("1º - A cada dia só haverá 1 evento" \
    "2º - A cada dia que passa os eventos vão causar mais dano" \
    "3º - o jogo tem duração de 15 dias " \
    "4º - Se a tua pontuação de vida for menor que 3 o jogo para automaticamente ")

def Dia1():
    



   
    vida = 10
    while True :
        dado = randint (1,6)

        if dado == 1:
            vida -= 3 

        elif dado == 2:
            vida -= 2

        elif dado == 3:
            vida  -= 1

        elif dado == 4 :
            vida +=1

        elif dado == 5 :
            vida +=1

        else:
            vida +=2

        
Cabecalho("Dados Da Sobrevivencia")
DadosDaSobrevivencia()
Cabecalho("Regras basicas")



           

