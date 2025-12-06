#ce ficnier sert à déterminer les classes d'équivalence 
#on va utiliser le sous-groupe des coins



import numpy as np
from itertools import permutations, product
import copy
from collections import deque
import sqlite3
import json

import coordinates






### je sais pas comment faire
def insert_new_class(state, card):
    with sqlite3.connect("classesequivalence.db") as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO classe (id, coins) VALUES (?, ?)
            ''', (card, state[0]))
            conn.commit()

####




#retourne les coordonnées des coins
def edge_only_class(configuration):
    configuration_str = ""

    for k in configuration[1]:
         configuration_str+= f"{k[0]}{k[1]}"

    return (configuration[1], configuration_str)



#fobction qui teste l'appartenance de deux config à la même classe d'équivalecne 
def is_equivalent(config1, config2):
     
     return (edge_only_class(config1) == edge_only_class(config2))



#dfs qui va parcourir les configurations du cube pour les stocker en classes d'équivalence
def bfs(config_init, profondeur_max):

    visited = [config_init]
    profondeur = 0
    deja_vu = [config_init]
    

    a_voir = [coordinates.Rubikscubemoves.rotateF(config_init), 
              coordinates.Rubikscubemoves.rotateB(config_init), 
              coordinates.Rubikscubemoves.rotateD(config_init), 
              coordinates.Rubikscubemoves.rotateL(config_init), 
              coordinates.Rubikscubemoves.rotateR(config_init), 
              coordinates.Rubikscubemoves.rotateU(config_init),
              coordinates.Rubikscubemoves.move_E(config_init),
              coordinates.Rubikscubemoves.move_M(config_init),
              coordinates.Rubikscubemoves.move_S(config_init)]
    
    
    
    classe_equivalence = [[config_init]]

    card = 2
    

    while a_voir != []:


        new_config = a_voir.pop()
        
        a_voir_new_configs = [coordinates.Rubikscubemoves.rotateF(new_config), 
                              coordinates.Rubikscubemoves.rotateB(new_config), 
                              coordinates.Rubikscubemoves.rotateD(new_config), 
                              coordinates.Rubikscubemoves.rotateL(new_config), 
                              coordinates.Rubikscubemoves.rotateR(new_config), 
                              coordinates.Rubikscubemoves.rotateU(new_config),
                              coordinates.Rubikscubemoves.move_E(config_init),
                              coordinates.Rubikscubemoves.move_M(config_init),
                              coordinates.Rubikscubemoves.move_S(config_init)]
        
        

        if not new_config in deja_vu:
            deja_vu += [new_config]



        for j in a_voir_new_configs:
            new = True

            #on regarde si j représente une nouvelle classe d'équivalence
            for k in classe_equivalence:
                if is_equivalent(k[0], j) == True:
                    new = False
            if new == True:
                insert_new_class(j, card)

        card+=1
            
        a_voir = a_voir_new_configs + a_voir
            


        #on appelle le dfs de nouveau
        bfs(new_config)

    #l'important est la base de données
    return  







