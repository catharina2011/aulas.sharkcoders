def soma():
    resultado1 = a + b
    print(f" o resultado da soma é{resultado1}")
    return resultado1
def subtração():
    resultado2 = a - b
    print(f" o resultado da subtração é{resultado2}")
    return resultado2

def divisão():
    resultado3 = a / b
    print(f" o resultado da divisão é{resultado3}")
    return resultado3

def multiplicação():
    resultado4 = a * b
    print(f" o resultado da multiplicação é {resultado4}")
    return resultado4

def Main():
    while True:
        global a
        global b
        print()
        print("\n 1 - soma \n 2 - subtração \n 3 - divisão \n 4 - multiplicção \n 0 - sair ")
        escolha = int(input("\nQual é a sua escolha ? "))
        print()
        if escolha==0:
            break
        else: 
            a = int ( input("entre com o valor a: "))
            b = int ( input("entre com o valor b: "))
            if escolha == 1:
               resultado = soma()
           
            elif escolha==2:
                resultado = subtração()
            
            elif escolha==3:
                if b !=0.0:
                    resultado = divisão()
                else:
                    print("\n O segundo valor tem de ser diferente de 0.\n")
                    input("\nEnter para terminar\n")
            elif escolha==4:
               resultado = multiplicação()

        print(f"\nO resultado é {resultado : .2f}")
            
                
Main()