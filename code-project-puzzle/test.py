import coordinates
import factorisation

# Configuration du cube résolu
coins =[
    [0, 0], [1, 0], [2, 0], [3, 0],  # Coins 0 à 3
    [4, 0], [5, 0], [6, 0], [7, 0]   # Coins 4 à 7
]

arretes = [
    [0, 0], [1, 0], [2, 0], [3, 0],  # Arêtes 0 à 3
    [4, 0], [5, 0], [6, 0], [7, 0],  # Arêtes 4 à 7
    [8, 0], [9, 0], [10, 0], [11, 0] # Arêtes 8 à 11
]
state = [coins, arretes]

dummy_config = coordinates.ClassicRubiksCube(state)

dummy_class = factorisation.MiddleLayerEquivalenceClasses(state)
print(dummy_class.find_equivalence_classes(state))