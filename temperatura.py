def far_to_celsius (temp):
    temperatura=((temp - 32 * 5/9))
    print(temperatura)
    return temperatura
far_to_celsius(60)
def pedirtemperatura():
    valor= input("que temperatura quer calcular?")
    resultado = far_to_celsius(valor)
    print(f"o resultado da conversão é :{resultado}")

pedirtemperatura()