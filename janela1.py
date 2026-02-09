from tkinter import*
red ="#ff0010"
blue ="#8faecb"
green ="#24ff00"
black ="#010500"
def ação(): 
    labelação  = Label (janela, text = " welcome", font = " time 20 bold ", background= blue )
    labelação.place (width =150, height =40, x= 125, y = 150)

    
    
janela = Tk()
janela.title( "teste" )
janela.geometry("400x500+200+200")
janela.wm_resizable(width= True, height=True)

ButtonClick = Button (janela, text = " blue ", command = ação, font = " time 20 bold", background= blue )
buttonAção1 = Button (janela, text = " green",command = ação, font = " time 20 bold", background= green )
buttonAção2 = Button (janela, text = " black",command = ação, font = " time 20 bold", background= black )
buttonAção3 = Button (janela, text = " red",command = ação, font = " time 20 bold", background= red )
ButtonClick.place(x = 20,  y =50)
buttonAção1.place (x = 200,  y =50)
buttonAção2.place (x = 20,  y =300)
buttonAção3.place (x = 200,  y =300)
janela.mainloop()