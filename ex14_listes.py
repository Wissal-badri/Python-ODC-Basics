# Ancien code (commenté)
# #les listes
# ma_liste = [10, 20, 30, 40, 50]
# print("Contenu de la liste :")
# for element in ma_liste:
#     print(element)
# print("Fin de l'affichage de la liste")

# L=[]
# for i in range(5):
#     valeur = int(input("Entrez une valeur à ajouter à la liste : "))
#     L.append(valeur)
# print("Contenu de la liste après ajout des valeurs :", L)

# ========================================
# EXERCICE 1 : Ajout d'éléments à une liste (TERMINÉ)
# ========================================
# # 1. Initialiser une liste vide pour stocker les nombres
# nombres = []
# 
# print("Veuillez entrer 5 nombres :")
# 
# # 2. Utiliser une boucle for pour entrer 5 nombres à l'aide de la fonction input()
# for i in range(5):
#     valeur = input(f"Entrez le nombre n°{i+1} : ")
#     # Ajouter l'élément à la liste
#     nombres.append(valeur)
# 
# # 3. Afficher la liste ensuite
# print("\nLa liste finale est :", nombres)

# ========================================
# EXERCICE 2 : Accéder aux éléments d'une liste
# ========================================

# Créer une liste nommée fruits qui contient les éléments suivants : "pomme", "banane", "cerise", "orange", "kiwi"
fruits = ["pomme", "banane", "cerise", "orange", "kiwi"]

# Afficher le premier élément de la liste
print("Premier élément :", fruits[0])

# Afficher le dernier élément de la liste
print("Dernier élément :", fruits[-1])

# Afficher le troisième élément de la liste
print("Troisième élément :", fruits[2])
