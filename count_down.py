from time import sleep


def Countdown():
    contagem = int(input("qual o valor inicial da contagem? "))

    while True:
        if contagem == 0:
            print("blast off!")
            break
        else:
            print(contagem)
            contagem -= 1
            sleep(1)

Countdown()