import random

def deviner_nombre(choix_min, choix_max):
    essais = 0  # Compteur d'essais
    devine = False  # Indique si l'ordinateur a deviné le nombre

    print(f"Choisissez un nombre entre {choix_min} et {choix_max}. Je vais essayer de deviner.")

    while not devine:
        essais += 1  # Incrémente le compteur d'essais
        devine_nombre = random.randint(choix_min, choix_max)  # L'ordinateur choisit un nombre aléatoire dans la plage
        print(f"Est-ce que le nombre choisi est {devine_nombre}?")
        reponse = input("Entrez 'plus', 'moins' ou 'exact' : ").lower()

        if reponse == 'exact':
            devine = True  # L'ordinateur a deviné le nombre
            print(f"J'ai deviné en {essais} essais. Le nombre choisi est {devine_nombre}!")
        elif reponse == 'plus':
            choix_min = devine_nombre + 1  # L'intervalle est ajusté vers le haut
        elif reponse == 'moins':
            choix_max = devine_nombre - 1  # L'intervalle est ajusté vers le bas
        else:
            print("Réponse invalide. Entrez 'plus', 'moins' ou 'exact'.")

# Plage de nombres possibles (par exemple, de 1 à 100)
choix_min = 1
choix_max = 100

deviner_nombre(choix_min, choix_max)