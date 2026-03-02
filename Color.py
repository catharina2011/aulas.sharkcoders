from tkinter import *

white = "#ffffff"
red ="#e40000"
blue ="#007ae4"
yellow ="#e4c900"
green ="#20b217"

def Blue ():
    janela.configure (bg = blue)
    labelColor.configure( text = "blue", bg = blue)

def Red ():
    janela.configure (bg = red)
    labelColor.configure( text = "red", bg = red)

def Green():
    janela.configure (bg = green)
    labelColor.configure( text = "green", bg = green)

def Yellow():
    janela.configure (bg = yellow)
    labelColor.configure( text = "yellow", bg = yellow)





janela = Tk()
janela.title("color changer")
janela.geometry("500x500+560+120")
janela.wm_resizable(width = False, height = False )
janela.configure(Background = white )


buttonBlue = Button (janela, text = "azul", command = Blue, font = "Time  14 bold ", bg = blue )
buttonBlue.place(width = 200, heigth =  160, x = 40, y = 20)

buttonRed = Button (janela, text = "vermelho", command = Red, font = "Time  14 bold ", bg = Red )
buttonRed.place(width = 200, heigth =  160, x = 260, y = 20)

buttonYellow = Button (janela, text = "amarelo", command = Yellow, font = "Time  14 bold ", bg = Yellow )
buttonYellow.place(width = 200, heigth =  160, x = 40, y = 200)

buttonGreen= Button (janela, text = "verde", command = Green, font = "Time  14 bold ", bg = Green )
buttonGreen.place(width = 200, heigth =  160, x = 260, y = 200)

labelColor = Label (janela, text = " Colour", font =" Time 20 bold ", bg = white)
labelColor.place ( width = 120, height = 60, X = 190, Y = 390)


janela.mainloop ()