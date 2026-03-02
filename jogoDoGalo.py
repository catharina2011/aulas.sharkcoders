import tkinter as tk
from tkinter import messagebox


def ClicaBotao(index):
    global jogadorAtual, board, buttons

    if board[index] == "": 
        board[index] = jogadorAtual
        buttons [index].config( text = jogadorAtual)

        if VerificaVencedor():
           messagebox.showinfo (" Fim de  Jogo", f" jogador {jogadorAtual} venceu !")
           Reset()

        elif "" not in board:
           messagebox.showinfo (" Fim de Jogo", " Empate !")
           Reset()
            
        else:
            if jogadorAtual == "X":
               jogadorAtual = "O"
            else:
               jogadorAtual = "X" 

def VerificaVencedor():

    combinacoes = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for comb in combinacoes :
   
        if board[ comb[0]] == board [ comb [1]] == board [comb[2]] != "": 
            return True
    return False 

def Reset():
    global jogadorAtual, board
    jogadorAtual = "X"
    board = ["" for _ in range(9)]
    for button in buttons :
        button.config(text="")

    
if __name__ == "__main__":
    janela = tk.Tk() 
    janela.title(" Jogo do Galo ")


    jogadorAtual = "X"
    board = ["" for _ in range (9)]
    buttons = []

    for i in range (9) :
        button = tk.Button (janela, text = "", font = ("normal", 40), width = 5, height = 2, command = lambda i = i : ClicaBotao(i)) 
        linha = i// 3
        coluna = i % 3
        button.grid (row =linha, column = coluna)
        buttons.append(button)

    janela.mainloop()