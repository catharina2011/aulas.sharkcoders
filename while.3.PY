paises=["portugal","suíça","frança","espanha ","dinamarca"]

while True:
    PE=input("escolha um pais europeu   ")

    if PE in paises:
       print("parabéns ")
       break
    else:
       print("não acertou, tente novamente")