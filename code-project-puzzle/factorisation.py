#ce ficnier sert à déterminer les classes d'équivalence 
#on va utiliser le sous-groupe des coins



import numpy as np
from itertools import permutations, product
import copy
from collections import deque
import sqlite3

import coordinates




def middle_layer_edges(configuration):


    middle_edges_indices=[4, 5, 6, 7]
    # Récupère les arêtes de la configuration
    arretes = configuration[1]

    # Extrait uniquement les arêtes de la couche du milieu
    middle_edges = [arretes[i] for i in middle_edges_indices]

    return middle_edges



#fobction qui teste l'appartenance de deux config à la même classe d'équivalecne 
def is_equivalent(config1, config2):
     
     return (middle_layer_edges(config1) == middle_layer_edges(config2))



#dfs qui va parcourir les configurations du cube pour les stocker en classes d'équivalence
def dfs(config_init, profondeur_max):

    visited = [config_init]
    profondeur = 0

    hidden_configs = (config_init,
                      coordinates.Rubikscubemoves.rotateF(config_init), 
                      coordinates.Rubikscubemoves.rotateB(config_init), 
                      coordinates.Rubikscubemoves.rotateD(config_init), 
                      coordinates.Rubikscubemoves.rotateL(config_init), 
                      coordinates.Rubikscubemoves.rotateR(config_init), 
                      coordinates.Rubikscubemoves.rotateU(config_init))
    
    a_voir = [coordinates.Rubikscubemoves.move_E(config_init), 
              coordinates.Rubikscubemoves.move_M(config_init), 
              coordinates.Rubikscubemoves.move_S(config_init)]
    
    classe_equivalence = []
    

    while a_voir != []:


        new_config = a_voir.pop()
        hidden_new_configs = [new_config,
                              coordinates.Rubikscubemoves.rotateF(new_config), 
                              coordinates.Rubikscubemoves.rotateB(new_config), 
                              coordinates.Rubikscubemoves.rotateD(new_config), 
                              coordinates.Rubikscubemoves.rotateL(new_config), 
                              coordinates.Rubikscubemoves.rotateR(new_config), 
                              coordinates.Rubikscubemoves.rotateU(new_config)]
        
        a_voir_new_configs = [coordinates.Rubikscubemoves.move_E(new_config), 
                              coordinates.Rubikscubemoves.move_M(new_config), 
                              coordinates.Rubikscubemoves.move_S(new_config)]
        
        if not new_config in visited:
            visited += hidden_new_configs
            new = True
            
            if profondeur >= profondeur_max:
                break

            #on emplie les nouvelles configurations
            a_voir += a_voir_new_configs

            #on check si le lot de configurations équivalentes appartient à une classe d'équivalence déjà taitée
            for k in classe_equivalence:
                if is_equivalent(k[0], new_config) == True:
                    k.append(new_config)
                new = False
            if new== True:
                classe_equivalence.append(hidden_new_configs)

            profondeur+=1

            #on appelle le dfs de nouveau
            dfs(new_config)


        else:
            pass







########

#base de donnée pas encore implémentée

########


"""

#implémentation de la base de donnée
class EquivalenceClassDatabase:
    def __init__(self, db_name="equivalence_classes.db"):
        # Nom de la base de données
        self.db_name = db_name
        # Initialise la base de données
        self._init_db()

    def _init_db(self):
        # Crée une connexion à la base de données
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            # Crée la table 'equivalence_classes' si elle n'existe pas
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS equivalence_classes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    middle_edges TEXT NOT NULL UNIQUE
                )
            ''')
            conn.commit()

    def insert_equivalence_class(self, middle_edges):
        # Insère une classe d'équivalence dans la base de données
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            # Convertit les arêtes de la couche du milieu en chaîne de caractères
            middle_edges_str = str(middle_edges)
            try:
                cursor.execute('''
                    INSERT INTO equivalence_classes (middle_edges) VALUES (?)
                ''', (middle_edges_str,))
                conn.commit()
            except sqlite3.IntegrityError:
                # Si la classe est déjà présente, on ne fait rien
                pass

    def get_all_equivalence_classes(self):
        # Récupère toutes les classes d'équivalence de la base de données
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM equivalence_classes
            ''')
            return cursor.fetchall()

    def close(self):
        # Ferme la connexion à la base de données
        pass

"""
