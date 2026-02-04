#Afficchage un message simple
print("Hello, ODC!")

#Variables

#camelCase notation
#nomEtudiant= "Wissal"
#snake_case notation
#nom_etudiant= "Wissal"
#Kebab-case notation
#nom-etudiant= "Wissal"
#Pas de notation
#nometudiant= "Wissal"

#Exemple
# Prix_casquette= 20
# print("Le prix de la casquette est de", Prix_casquette, "Dirham")

#input function
# nom= input("Entrez votre nom: ")
# age= input("Entrez votre age: ")
# #affichage des variables
# print("Votre nom est:", nom)
# print("Votre age est:", age)

# #Exercice
# A= "Wissal"
# B= "Badri"
# print ("Avant l'échange: A =", A, ", B =", B)
# #Echange des valeurs
# temp= A
# A= B
# B= temp
# print ("Après l'échange: A =", A, ", B =", B)

#Les oprateurs arithmétiques
# N=14
# X=20
# print ("La somme de N et X est:", N + X)
# print ("La différence de N et X est:", X - N)
# print ("Le produit de N et X est:", N * X)
# print ("Le quotient de X par N est:", X / N)
# print ("Le reste de la division de X par N est:", X % N)
# print ("La puissance de N à la X est:", N ** X)
# print ("La division entière de X par N est:", X // N)

# #Exercice
# # Demander à l'utilisateur d'entrer deux nombres
# nombre1 = int(input("Entrer le premier nombre : "))
# nombre2 = int(input("Entrer le deuxième nombre : "))

# # Calcul de la somme
# somme = nombre1 + nombre2

# # Affichage du résultat
# print("La somme est :", somme)

#La concatenation des chaines de caractères String
# prenom= input("Entrez votre prénom: ")
# nom= input("Entrez votre nom: ")
# print("Bonjour, " + prenom + " " + nom + "!")

# #La repetition des chaines de caractères String
# message= "Bienvenue à ODC! "
# print( message * 3)

#La comparaison des valeurs
# A= 10
# B= 20
# print("A est égal à B:", A == B)
# print("A est différent de B:", A != B)
# print("A est supérieur à B:", A > B)
# print("A est inférieur à B:", A < B)

#Exercice
# x,y,z= 5,10,15
# print("x est le plus grand:", x > y and x > z)
# print("y est le plus grand:", y > x and y > z)
# print("z est le plus grand:", z > x and z > y)
# print("Au moins un des nombres est supérieur à 12:", x > 12 or y > 12 or z > 12)

# print(x>z)
# print((y-5)==x)

#Les fonctions intégrées
# nom="Wissal"
# print(nom.upper())
# print(nom.lower())
# print("La longueur de", nom, "est:", len(nom))
# print("La position de 's' dans", nom, "est:", nom.index("s"))

#Booleans et conditions
# age= int(input("Entrez votre âge: "))
# if age >= 18:
#     print("Vous êtes majeur.")
# else:
#     print("Vous êtes mineur.")

# #And Or Not
# temperature= int(input("Entrez la température actuelle: "))
# if temperature > 30 and temperature <= 40:
#     print("Il fait chaud.")
# elif temperature > 20 and temperature <= 30:
#     print("Il fait doux.")
# elif temperature >= 10 and temperature <= 20:
#     print("Il fait frais.")

# #Or
# elif temperature < 10 or temperature > 40:
#     print("Température extrême.")
# else:
#     print("Température normale.")

#Traitement conditionnel en python
#if condition1:
# x=5
# if x > 0:
#     print("x est un nombre positif.")
# if x < 2 :
#     print("x est inférieur à 2.")
# if x % 2 == 1:
#     print("x est un nombre impair.")
# if x == 0 :
#     print("x est égal à 0.")

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
#     resultat= num1 * num2
     print("Le résultat de la multiplication est:", resultat)
elif operation == "/":
     if num2 != 0:
         resultat= num1 / num2
         print("Le résultat de la division est:", resultat)
     else:
         print("Erreur: Division par zéro.")
else:
    print("Opération non reconnue.")

# if else condition2:
# Demander à l'utilisateur d'entrer un nombre
nombre = int(input("Entrez un nombre : "))

if nombre % 2 == 0:
    print("Le nombre est pair")
else:
    print("Le nombre est impair")
