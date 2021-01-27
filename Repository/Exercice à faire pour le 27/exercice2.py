x = int(input("Un nombre: "))
y = int(input("Un deuxième nombre: "))
op = input("Un opérateur: ")

if op == "+":
    res = x + y
elif op == "-":
    res = x - y
elif op == "*":
    res = x * y
elif op == "/":
    res = x / y
else:
    print("Veuillez saisir un opérateur correct")
    res = x + y

nom = input("Donnez un nom pour votre fichier: ")
nom = nom + '.txt'

f = open(nom,'x')
f.write("Resultat: " + str(res))
f.close()