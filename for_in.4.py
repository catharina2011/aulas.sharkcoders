inicial = int(input("escolha o numero inicial "))
final = int (input("escolha o numero  final "))
incremento = int(input("escolha o valor do incremento "))

print("")
print(f"\nOs numeros entre {inicial} e {final},com um incremento de {incremento}")

for numero in range(inicial, final+1, incremento ):
    print(numero, end=" ")

print()
input("Enter ")
    
