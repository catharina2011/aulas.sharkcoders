with open("FicheiroCom1Linha.txt", "w") as ficheiro: 
    ficheiro.write(" queijo")

with open("FicheiroCom3Linhas.txt", "w") as ficheiro:
    ficheiro.write(" Primeira Linha  \n ")
    ficheiro.write(" Segunda Linha  \n ")
    ficheiro.write(" Terceira Linha  \n ")

with open("FicheiroCom3Linhas.txt", "a") as ficheiro:
    ficheiro.write("\nLinha")
    novasLinhas = ["\n Linha 5", "\nLinha 6"]
    ficheiro.writelines(novasLinhas)

with open("FicheiroCom3Linhas.txt", "r") as ficheiro:
    conteudo = ficheiro.readlines()
    for linha in conteudo:
        if "segunda" in linha :
            print (linha)
   
    print(conteudo[1])
   