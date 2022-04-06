t = (19,42,21)

print("The 3 numbers are: ", end='') #end = pour enlever le \n pour le remplacer par '' ou n importe
for x in t:
    if x == t[-1]:
        print(x)
    else:
        print(x, end=", ")
