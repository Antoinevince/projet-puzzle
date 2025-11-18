import coordinates
import factorisation

# Configuration du cube résolu
state = [
    # Liste des coins
    [
        [0, 0],  # Coin 0
        [1, 0],  # Coin 1
        [2, 0],  # Coin 2
        [3, 0]   # Coin 3
    ],
    # Liste des arêtes
    [
        [0, 0],  # Arête 0
        [1, 0],  # Arête 1
        [2, 0],  # Arête 2
        [3, 0],  # Arête 3
        [4, 0],  # Arête 4
        [5, 0],  # Arête 5
        [6, 0],  # Arête 6
        [7, 0]   # Arête 7
    ]
]

print(factorisation.dfs(state, 5))