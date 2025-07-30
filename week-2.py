
my_list = []

# 2. Ajouter les nombres: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print("Liste après ajout:", my_list)

# 3. Insert la valeur 15 à l'index 1 (2ème position)
my_list.insert(1, 15)

print("Liste après insertion de 15 à l'index 1:", my_list)

# 4. Etendre la liste avec la liste [50, 60, 70]
my_list.extend([50, 60, 70])

print("Liste après extension:", my_list)

# 5. Supprimer le dernier élément de la liste
my_list.remove(my_list[-1])

print("Liste après suppression du dernier élément:", my_list)

# 6. Trier la liste par ordre croissant
my_list.sort()

print("Liste triée:", my_list)

# 7. Rechercher l'index de la valeur 30 dans la liste
index_30 = my_list.index(30)
print("Index de la valeur 30:", index_30)
