#!/usr/bin/env python3

import unittest

#Créer une calculatrice simple.
#Il faut demander à l’utilisateur un premier nombre.
#Puis un opérateur
#Puis un deuxième nombre.
#Ensuite il faut écrire le résultat dans un fichier dont l'utilisateur choisit le nom.

def operation(a, b, c):
        result = 0
        if a == "+":
            result = b + c
        elif a =="-":
            result = b - c
        elif a =="*":
            result = b * c
        elif a =="/":
            if c != 0:
                result = b / c
            else:
                print("on ne peut pas diviser par 0")
        else:
            raise TypeError
        return(result)

def main():

    #Récupération entrées utilisateur
    firstInt = int(input("Veuillez entrer un chiffre \n"))
    operator = input("Veuillez entrer un opérateur \n")
    secondInt = int(input("veuillez choisir un deuxieme chiffre \n"))
    #nameFile = input("dans quel fichier voulez vous écrire le resultat ?\n")

    #Calcul en fonction de l'opérateur choisis
    result = operation(operator, firstInt, secondInt)
    #Création, écriture et fermeture du fichier
    print(result)

    #fileToWrite =  open(nameFile + ".txt", "w")
    #fileToWrite.write(str(firstInt) + operator + str(secondInt) + " =" + str(result))
    #fileToWrite.close()


if __name__== "__main__":
    main()