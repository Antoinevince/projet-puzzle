import coordinates
import factorisation

# Configuration du cube résolu
state = (
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # Coins
    [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]  # Arêtes
)

print(factorisation.dfs(state, 5))