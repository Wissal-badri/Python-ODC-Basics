#Exercice
x = 10
if x > 0:
    print("Positif")
elif x < 0:
    print("Négatif")
else:
    print("Nul")

#Exercice
note = float(input("Entrez la note de l'étudiant : "))
if note > 20 or note < 0:
    print("Note invalide")
elif note >= 16:
    print("La mention est : Très bien")
elif note >= 14:
    print("La mention est : Bien")
elif note >= 12:
    print("La mention est : Assez bien")
elif note >= 10:
    print("La mention est : Passable")
else:
    print("La mention est : Insuffisant")
