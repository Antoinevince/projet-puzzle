import coordinates
import factorisation
import sqlite3


# Configuration du cube résolu
state = [
    # Liste des coins
    [
        [0, 0],  # Coin 0
        [1, 0],  # Coin 1
        [2, 0],  # Coin 2
        [3, 0],   # Coin 3
        [4, 0],
        [5, 0],
        [6, 0],
        [7, 0],
        [8, 0]
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

#print(coordinates.Rubikscubemoves.rotateF(state))

print(factorisation.bfs(state, 5))

#database = sqlite3.connect('classesequivalence.db')