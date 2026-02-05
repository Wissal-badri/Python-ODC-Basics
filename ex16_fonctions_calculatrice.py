# ========================================
# EXEMPLES DE FONCTIONS EN PYTHON
# ========================================

# Exemple 1 : Fonction simple sans paramètres
# def dire_bonjour():
#     print("Bonjour !")
# 
# dire_bonjour()  # Appel de la fonction

# Exemple 2 : Fonction avec paramètres
# def additionner(a, b):
#     return a + b
# 
# resultat = additionner(5, 3)
# print("5 + 3 =", resultat)

# Exemple 3 : Fonction avec plusieurs opérations
# def calculer(x, y):
#     somme = x + y
#     difference = x - y
#     produit = x * y
#     quotient = x / y
#     return somme, difference, produit, quotient
# 
# s, d, p, q = calculer(10, 2)
# print(f"Somme: {s}, Différence: {d}, Produit: {p}, Quotient: {q}")


# ========================================
# EXERCICE : Création d'une calculatrice en Python
# ========================================

# 1. Définir des fonctions pour chaque opération de calcul
def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Erreur : Division par zéro impossible"

# 2. Créer une fonction principale (calculatrice) qui utilise une boucle pour afficher un menu d'options
def calculatrice():
    while True:
        print("\n=== CALCULATRICE ===")
        print("1. Addition")
        print("2. Soustraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quitter")
        
        choix = input("\nChoisissez une opération (1-5) : ")
        
        if choix == "5":
            print("Au revoir !")
            break
        
        if choix in ["1", "2", "3", "4"]:
            # 3. À chaque sélection, demander à l'utilisateur d'entrer deux nombres
            num1 = float(input("Entrez le premier nombre : "))
            num2 = float(input("Entrez le deuxième nombre : "))
            
            # 4. Afficher le résultat de l'opération et permettre de continuer
            if choix == "1":
                resultat = addition(num1, num2)
                print(f"\nRésultat : {num1} + {num2} = {resultat}")
            elif choix == "2":
                resultat = soustraction(num1, num2)
                print(f"\nRésultat : {num1} - {num2} = {resultat}")
            elif choix == "3":
                resultat = multiplication(num1, num2)
                print(f"\nRésultat : {num1} × {num2} = {resultat}")
            elif choix == "4":
                resultat = division(num1, num2)
                print(f"\nRésultat : {num1} ÷ {num2} = {resultat}")
        else:
            print("\nChoix invalide ! Veuillez choisir entre 1 et 5.")

# Lancer la calculatrice
calculatrice()
