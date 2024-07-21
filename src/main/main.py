while True:
    a = input("Entrez un premier nombre : ")
    b = input("Entrez un deuxième nombre : ")

    if not (a.isdigit() and b.isdigit()):
        print("Veuillez entrer deux nombres valides !")
        continue

    break

print(f"{a} + {b} = {int(a) + int(b)}")