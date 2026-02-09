velocidade=int(input("indique a velocidade" ))
multa= (velocidade-80)*2
if velocidade <= 80:
    print(" Dentro do limite. Boa viagem")
else:
    print("Está a cima do limite permitido. A multa foi gerada no valor de ", multa)
    