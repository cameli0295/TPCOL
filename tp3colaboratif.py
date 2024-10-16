
import random

# Générer un nombre secret entre 1 et 100
secret_number = random.randint(1, 100)

# Commencer la boucle de devinette
guess = None  # Initialiser la variable 'guess'
attempts = 0

while guess != secret_number:
    # Demander à l'utilisateur de deviner le nombre
    guess = int(input("Devinez le nombre secret (entre 1 et 100): "))
    attempts += 1
    
    # Vérifier si la devinette est trop basse, trop haute ou correcte
    if guess < secret_number:
        print("Trop bas ! Réessayez.")
    elif guess > secret_number:
        print("Trop haut ! Réessayez.")
    else:
        print(f"Félicitations ! Vous avez deviné le nombre : {secret_number}")
        print(f"nombre de tentatives: {attempts}")