from datetime import date 

hoje=date. today(). year
nasc=int(input(" qual o ano de nascimento do atleta?"))
idade=hoje-nasc
print()
if idade<=9:
    print("este atleta é da base mirin")
elif idade<=14:
    print("este atleta é da base infantil")
elif idade<=19:
    print("este atleta é da base junior")
elif idade <=25:
    print("este atleta é da base senior")
else:
    print("este atleta é da base master")