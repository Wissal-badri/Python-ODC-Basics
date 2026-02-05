# if elif elif condition3:
# Demander à l'utilisateur d'entrer un nombre
nombre = int(input("Entrez un nombre : "))
if nombre > 0 and nombre % 2 == 0:
    print("Le nombre est positif et pair")
elif nombre > 0 and nombre % 2 != 0:
    print("Le nombre est positif et impair")
elif nombre < 0 and nombre % 2 == 0:
    print("Le nombre est négatif et pair")
elif nombre < 0 and nombre % 2 != 0:
    print("Le nombre est négatif et impair")
else:
    print("Le nombre est zéro")
