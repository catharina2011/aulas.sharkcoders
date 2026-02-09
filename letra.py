def quantas_letras_tem ():
    soma =0
    jeremias=input("escreve qualquer coisa, de preferencia q faça sentido ")
    letra= input("escolhe uma letra, de preferencia que estaja no que escreveste antes ")
    for x in jeremias:
        if x == letra :
            soma +=1
    print(f"o que escreveste tem {soma} letras {letra}")

for x in range (1,6):
    quantas_letras_tem()