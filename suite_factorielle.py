#Programme qui demande un nombre positif non nul de départ, et qui calcule sa factorielle
n=int(input("Entrer un entier : "))
f=1
if(n<0):
    print("Veuillez entrer un entier positif !")
else:
    for i in range(1,n+1):
        f=f*i
    print(f"La factorielle est {f}")
