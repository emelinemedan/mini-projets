import random


def jeu_pierre_papier_ciseaux():
    print("Jouons à Pierre-Papier-Ciseaux !")

    score_utilisateur = 0
    score_ordinateur = 0

    while True:
        choix_utilisateur = input("Choisissez : pierre, papier, ou ciseaux (ou 'quitter' pour sortir) : ").lower()

        if choix_utilisateur == 'quitter':
            print(
                f"Score final : Vous avez {score_utilisateur} point(s) et l'ordinateur a {score_ordinateur} point(s). Au revoir !")
            break  # Sortir de la boucle si l'utilisateur choisit de quitter

        # Liste des choix possibles pour l'ordinateur
        choix_ordinateur = ["pierre", "papier", "ciseaux"]

        # L'ordinateur fait un choix aléatoire
        choix_ordinateur = random.choice(choix_ordinateur)

        print(f"L'ordinateur a choisi : {choix_ordinateur}")

        # Détermine le gagnant
        if choix_utilisateur == choix_ordinateur:
            print("Égalité !")
        elif (choix_utilisateur == "pierre" and choix_ordinateur == "ciseaux") or (
                choix_utilisateur == "papier" and choix_ordinateur == "pierre") or (
                choix_utilisateur == "ciseaux" and choix_ordinateur == "papier"):
            print("Vous avez gagné !")
            score_utilisateur += 1
        else:
            print("L'ordinateur a gagné !")
            score_ordinateur += 1

        print(f"Score actuel : Vous avez {score_utilisateur} point(s) et l'ordinateur a {score_ordinateur} point(s)")


# Appel de la fonction pour jouer
jeu_pierre_papier_ciseaux()