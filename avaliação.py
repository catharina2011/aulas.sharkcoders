nota =int(input("insira a nota"))
match nota:
    case 20:
        avaliação=(" excelente")

    case 18:
        avaliação=("muito bom")
    
    case _:
        avaliação=("nota não reconhecida")

print(avaliação)