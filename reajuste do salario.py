ordenado=float(input("Você receberá um aumento de acordo com o valor do seu ordenado. Por favor incira o valor do seu ordenado "))

if ordenado<500:
    reajuste = 15
elif ordenado<=1000:
    reajuste = 10
else:
    reajuste = 5
novoordenado=ordenado+(ordenado*reajuste/100)
print("o reajuste será de",reajuste,"e passará a " ,novoordenado )
print(f"o reajuste será de{reajuste}%, o valor acrescentado será de {novoordenado:.2f}")


