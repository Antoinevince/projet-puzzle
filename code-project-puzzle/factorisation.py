#ce ficnier sert à déterminer les classes d'équivalence 
#on va utiliser le sous-groupe des coins



import numpy as np
from itertools import permutations, product
import copy
from collections import deque
import sqlite3

import coordinates


class MiddleLayerSubgroup(coordinates.ClassicRubiksCube):
    def __init__(self, state):
        super().__init__(state)

    
    

class MiddleLayerEquivalenceClasses:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.equivalence_classes = []
        self.visited = set()

        

    def find_equivalence_classes(self):
        queue = deque()
        queue.append(self.initial_state)
        self.visited.add(self.initial_state)

        current_class = []

        while queue:
            current_state = queue.popleft()
            current_class.append(current_state)

            for move in [self.apply_move_M, self.apply_move_E, self.apply_move_S]:
                new_state = move(current_state)
                if new_state not in self.visited:
                    self.visited.add(new_state)
                    queue.append(new_state)

        self.equivalence_classes.append(current_class)

        return self.equivalence_classes
    



    
class MiddleLayerEquivalenceDB:
    def __init__(self, db_name="rubiks_cube_equivalence.db"):
        self.db_name = db_name
        self._init_db()

    def _init_db(self):
        # Crée la table si elle n'existe pas
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS equivalence_classes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    class TEXT NOT NULL
                )
            ''')
            conn.commit()

    def insert_equivalence_class(self, eq_class):
        # Insère une classe d'équivalence dans la base de données
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            # Convertit la classe en chaîne de caractères
            class_str = str(eq_class)
            cursor.execute('''
                INSERT INTO equivalence_classes (class) VALUES (?)
            ''', (class_str,))
            conn.commit()

    def get_all_equivalence_classes(self):
        # Récupère toutes les classes d'équivalence de la base de données
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM equivalence_classes
            ''')
            return cursor.fetchall()
        

