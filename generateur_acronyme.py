def generate_acronym(phrase):
    mots = phrase.split()  # Divisez la phrase en mots en utilisant l'espace comme séparateur
    acronym = ''.join(word[0].upper() for word in mots)  # Prenez la première lettre de chaque mot et convertissez-la en majuscule
    return acronym

# Demandez à l'utilisateur de saisir une phrase
phrase = input("Entrez une phrase : ")
acronyme = generate_acronym(phrase)
print("La phrase à transformer est : ", phrase)
print("Acronyme généré :", acronyme)