import random 

numerosSorteados = []
somaPares = 0
soma = 0
def SortearNumerosDezVezes():
    for x in range (1,11):
        numero = random. randint (1, 100) 
        numerosSorteados.append (numero)

    print(f"os 10 valores sorteados foram : {numerosSorteados}")
          
def SomaDosParesDaLista():
    global somaPares
    for numero in numerosSorteados:
        if numero % 2 == 0:
            somaPares = somaPares + numero

    print(f"A soma dos valores pares contios na lista {numerosSorteados}é {somaPares}")


def SomaNumerosLista():
  
    global soma 
    for numero in numerosSorteados:
        soma = soma + numero
    print(f" a soma dos velores contidos na lista {numerosSorteados} é {soma}")



SortearNumerosDezVezes()
SomaDosParesDaLista()
SomaNumerosLista()


