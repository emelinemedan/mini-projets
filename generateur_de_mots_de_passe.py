import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    # ascii_letters contiens les lettres en majuscules et minuscules ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # digits contiens les chiffres de 0 à 9 digits ='0123456789'
    # punctuation contiens les symboles punctuation = '!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Demandez à l'utilisateur de choisir la longueur du mot de passe
try:
    length = int(input("Entrez la longueur du mot de passe : "))

    if length <= 0:
        print("La longueur du mot de passe doit être supérieure à zéro.")
    else:
        password = generate_password(length)
        print("Mot de passe généré :", password)
except ValueError:
    print("Veuillez entrer un nombre entier pour la longueur du mot de passe.")
