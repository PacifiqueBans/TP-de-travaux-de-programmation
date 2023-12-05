# Demander à l'utilisateur le nombre d'employés
nb_employes = int(input("Entrez le nombre d'employés : "))

# Créer un tableau vide pour stocker les noms et salaires des employés
employes = []

# Demander à l'utilisateur de saisir les noms et salaires des employés
for i in range(nb_employes):
    nom = input("Entrez le nom de l'employé : ")
    salaire = float(input("Entrez le salaire de l'employé : "))
    employe = (nom, salaire)
    employes.append(employe)

# Trouver l'employé avec le salaire le plus bas
min_salaire = min(employes, key=lambda x: x[1])
print("L'employé avec le salaire le plus bas est :", min_salaire[0], "avec un salaire de", min_salaire[1])

# Trouver l'employé avec le salaire le plus élevé
max_salaire = max(employes, key=lambda x: x[1])
print("L'employé avec le salaire le plus élevé est :", max_salaire[0], "avec un salaire de", max_salaire[1])

