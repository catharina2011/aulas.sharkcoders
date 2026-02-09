from random import randint 

def jogo1():
  while True:
    dado = [
        randint (1,6),
        randint (1,6),
        randint (1,6),
        randint (1,6),
        randint (1,6)
    ]

    print ("dado", dado )

    soma = 0

    for numero in dado:
        if dado.count(numero)>1:
            soma += numero
      
    print ("Soma de dois dados iguais dara a soma total")
    break 
    






def jogo2():
   while True:
    dadoUm = randint ( 1, 6 )
    dadoDois = randint ( 1, 6 )
    dadoTrês = randint ( 1, 6 )

    if dadoUm + dadoDois > 15 :
     print(f" O valor da soma dos dados é {dadoUm + dadoDois}. ")

    else:
      print(f" O valor estourou você perdeu")
      break


jogo2()
   