#Exercice : Système de gestion des tickets de cinéma

print("--- Système de gestion des tickets de cinéma ---")
# 1. Demander l'âge
age = int(input("Veuillez entrer votre âge : "))
# 2. Demander la carte d'étudiant
carte = input("Avez-vous une carte d'étudiant ? (oui/non) : ")
# 3. Demander l'horaire
horaire = input("Quelle est l'horaire de la séance ? (matin, après-midi ou soir) : ")
prix = 0
if age < 12:
    prix = 50
elif 12 <= age <= 17:
    if carte == "oui":
        prix = 50
    else:
        prix = 70
else:  # age >= 18
    if horaire == "soir":
        prix = 120
    else:
        prix = 100
    # Appliquer la réduction étudiant
    if carte == "oui":
        prix -= 20
        
print("Le prix du billet est de :", prix, "DH")
