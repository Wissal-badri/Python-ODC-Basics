#Traitement conditionnel en python
#if condition1:
x=5
if x > 0:
    print("x est un nombre positif.")
if x < 2 :
    print("x est inférieur à 2.")
if x % 2 == 1:
    print("x est un nombre impair.")
if x == 0 :
    print("x est égal à 0.")

#Exercice
num1= int(input("Entrez le premier nombre: "))
num2= int(input("Entrez le deuxième nombre: "))
operation= input("Entrez l'opération (+, -, *, /): ")
if operation == "+":
     resultat= num1 + num2
     print("Le résultat de l'addition est:", resultat)
elif operation == "-":
     resultat= num1 - num2
     print("Le résultat de la soustraction est:", resultat)
elif operation == "*":
     resultat= num1 * num2
     print("Le résultat de la multiplication est:", resultat)

elif operation == "/":
     if num2 != 0:
         resultat= num1 / num2
         print("Le résultat de la division est:", resultat)
     else:
         print("Erreur: Division par zéro.")
else:
    print("Opération non reconnue.")
