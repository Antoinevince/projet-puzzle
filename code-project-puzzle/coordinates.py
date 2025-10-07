""""
ce fichier sert à implémenter le système de coordonnées du rubik's cube, de la quarter turn metric
"""

import copy


"""on va représenter les configurations du cube sous forme de tableaux qui contiennent les mouvements qui ont permis d'arriver à cette configuration"""

#rubik's cube 3x3x3
class ClassicRubiksCube():


#on implémente les coordonnées en notant les coins et leur orientation sous formes de listes

#chaque coin sera représenté par une liste contenant la position du coin et son orientation


    def __init__(self, state):
        self.coins = state[0]
        self.arretes = state[1]
    
#les fonctions suivantes servent à gérer les différents mouvements que l'on peut faire sur les cube, et les interactions (ie si on fait un mouvement a, puis on effectue le mouvement inverse, il faut donc actualiser l'état du cube)
    
    def rotateF(self):
        self.new_coins = copy.deepcopy(self.coins) #copie de la liste des coords des coins

        #permutations des positions des 
        self.new_arretes = copy.deepcopy(self.arretes)  #copie de la liste des coords des coins



    def rotateR(self):

        pass

    def rotateU(self):
        pass

    def rotateL(self):
        pass
        
        return self.state

    def rotateB(self):
       pass

    def rotateD(self):
        pass


#cependant, à cause de la lourdeur en mémoire de ce type de représentation, nous allons en utiliser d'autres

def upgraded_representation():

    def __init__(self, corners, edges):
        self.corners = corners
        self.edges = edges

    