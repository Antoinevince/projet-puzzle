""""
ce fichier sert à implémenter le système de coordonnées du rubik's cube, de la quarter turn metric
"""

import copy


"""on va représenter les configurations du cube sous forme de tableaux qui contiennent les mouvements qui ont permis d'arriver à cette configuration"""

#rubik's cube 3x3x3
class ClassicRubiksCube():


#les coordonnées seront implémentées de la façon [coins, arretes] 

#chaque coin sera représenté par une liste contenant la position du coin et son orientation


    def __init__(self, state):
        self.coins = state[0]
        self.arretes = state[1]
    
#les fonctions suivantes servent à gérer les différents mouvements que l'on peut faire sur les cube, et les interactions (ie si on fait un mouvement a, puis on effectue le mouvement inverse, il faut donc actualiser l'état du cube)
    
    def rotateF(self):
        self.new_coins = copy.deepcopy(self.coins) #copie de la liste des coords des coins

#mise à jours des positions des coins
        for k in range(len(self.new_coins)):
            if self.coins[k][0] <= 3:
                if not self.new_coins[k][0] == 3:
                    self.new_coins[k][0]+= 1
                else:
                    self.new_coins[k][0]=0
            else:
                pass
        
        self.coins = copy.deepcopy(self.new_coins)
        print(self.new_coins)

#mise à jour des orientations de chaque coins
        for k in range(len(self.new_coins)):
            if self.coins[k][0] <= 3:
                self.new_coins[k][1] = (self.new_coins[k][1] +1)%3
            else:
                pass
        
        self.coins = copy.deepcopy(self.new_coins)   





        #permutations des positions des arrêtes
        self.new_arretes = copy.deepcopy(self.arretes)  #copie de la liste des coords des coins

        for k in range(len(self.new_arretes)):
            if self.arretes[k][0] <= 3:
                if not self.new_arretes[k][0] == 3:
                    self.new_arretes[k][0]+= 1
                else:
                    self.new_arretes[k][0]=0
            else:
                pass
        
        #mise à jour des orientations de chaque arrête
        for k in range(len(self.new_arretes)):
            if self.arretes[k][0] <= 3:
                self.new_arretes[k][1] = (self.new_arretes[k][1] +1)%3
            else:
                pass
        
        self.arretes = copy.deepcopy(self.new_arretes)
        #print([self.new_coins, self.arretes])
        #print(self.arretes)




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

    