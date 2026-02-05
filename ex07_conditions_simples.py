#Booleans et conditions
age= int(input("Entrez votre âge: "))
if age >= 18:
    print("Vous êtes majeur.")
else:
    print("Vous êtes mineur.")

#And Or Not
temperature= int(input("Entrez la température actuelle: "))
if temperature > 30 and temperature <= 40:
    print("Il fait chaud.")
elif temperature > 20 and temperature <= 30:
    print("Il fait doux.")
elif temperature >= 10 and temperature <= 20:
    print("Il fait frais.")

#Or
elif temperature < 10 or temperature > 40:
    print("Température extrême.")
else:
    print("Température normale.")
