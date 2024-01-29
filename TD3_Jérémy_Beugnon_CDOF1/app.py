import numpy as np

# Définir une matrice (par exemple, une matrice 2x2)
matrix = np.array([[4, 7],
                   [2, 6]])

# Calculer le déterminant de la matrice
determinant = np.linalg.det(matrix)

# Afficher le résultat
print(f"La matrice est :\n{matrix}")
print(f"Le déterminant de la matrice est : {determinant}")
