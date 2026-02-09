maior=0
menor=0

for contador in range (1,6):
    peso=float(input(f"\n Entre om o {contador}º peso"))

    print(f"\n O peso introduzido foi :{peso}kg")
    input("\n Carrega Enter para continuar")

    if contador==1:
       maior = menor = peso
    if peso > maior:
       maior= peso 
    if peso > menor:
       peso =menor 

print()
print(f"o numero maior é :{maior}")
print(f"o numero menor é :{menor}")


    