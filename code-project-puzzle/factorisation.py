#ce ficnier sert à déterminer les classes d'équivalence 
#on va utiliser le sous-groupe des coins



import numpy as np
from itertools import permutations, product
import copy
from collections import deque
import sqlite3

import coordinates

def is_equivalent(state1, state2):

    middle_edges_indices=[4, 5, 6, 7]
    
    middle_edges_state1 = [state1[1][i] for i in middle_edges_indices]
    middle_edges_state2 = [state2[1][i] for i in middle_edges_indices]

    
    return middle_edges_state1 == middle_edges_state2

def get_middle_layer_edges(self, arretes):
        
        return tuple(arretes[i] for i in self.middle_edges_indices)

def dfs(self, current_state, visited, equivalence_class):
        
        equivalence_class.append(current_state)
        
        visited.add(self.get_middle_layer_edges(current_state[1]))

       
        for move in [self.apply_move_M, self.apply_move_E, self.apply_move_S]:
            new_arretes = move(current_state[1])
            new_state = (current_state[0], new_arretes)
            new_middle_edges = self.get_middle_layer_edges(new_arretes)
            if new_middle_edges not in visited:
                self.dfs(new_state, visited, equivalence_class)

def find_equivalence_classes(self):
    
    visited = set()
    equivalence_classes = []


    initial_middle_edges = self.get_middle_layer_edges(self.initial_state[1])
    if initial_middle_edges not in visited:
        equivalence_class = []
        self.dfs(self.initial_state, visited, equivalence_class)
        equivalence_classes.append(equivalence_class)

    return equivalence_classes