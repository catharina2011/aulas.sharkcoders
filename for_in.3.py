n1=int(input("digite o numero inicial"))
n2=int(input("digite o numero final "))

print(f"os numero pares entre {n1} e {n2} são:")

for x in range(n1,n2): 
   if (x%2!=0):
       print(x)