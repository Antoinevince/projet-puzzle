""""
ce fichier sert à implémenter le système de coordonnées du rubik's cube, de la quarter turn metric
"""

import copy


"""on va représenter les configurations du cube sous forme de tableaux qui contiennent les mouvements qui ont permis d'arriver à cette configuration"""



class RubikscubeCoordinate():

    def __init__(self, state):
        self.coins = state[0]
        self.arretes = state[1]






#rubik's cube moves
class Rubikscubemoves():


    def __init__(self):
        pass
    
#les fonctions suivantes servent à gérer les différents mouvements que l'on peut faire sur les cube, et les interactions (ie si on fait un mouvement a, puis on effectue le mouvement inverse, il faut donc actualiser l'état du cube)
    
    def rotateF(self, state):
        self.new_coins = copy.deepcopy(state[0]) #copie de la liste des coords des coins

#mise à jours des positions des coins
        for k in range(len(self.new_coins)):
            if self.coins[k][0] <= 3:
                if not self.new_coins[k][0] == 3:
                    self.new_coins[k][0]+= 1
                else:
                    self.new_coins[k][3]=0
            else:
                pass
        
        self.coins = copy.deepcopy(self.new_coins)
        

#mise à jour des orientations de chaque coins
        for k in range(len(self.new_coins)):
            if self.coins[k][0] <= 3:
                self.new_coins[k][1] = (self.new_coins[k][1] +1)%3
            else:
                pass
        
        self.coins = copy.deepcopy(self.new_coins)   







        #permutations des positions des arrêtes
        self.new_arretes = copy.deepcopy(state[1])  #copie de la liste des coords des coins
        arretesl = [0, 1, 2, 3]

        for k in range(len(self.new_arretes)):
            if self.arretes[k][0] in arretesl:
                if not self.new_coins[k][0]!= arretesl[arretesl.index(self.arretes[k][0])+1]:
                    self.new_arretes[k][0]-= 1
                else:
                    self.new_arretes[k][0]=3
            else:
                pass
        
        #mise à jour des orientations de chaque arrête
        for k in range(len(self.new_arretes)):
            if self.arretes[k][0] in arretesl:
                self.new_arretes[k][1] = (self.new_arretes[k][1] +1)%3
            else:
                pass
        
        self.arretes = copy.deepcopy(self.new_arretes)
        state2 = [self.new_coins, self.arretes]

        return state2
        







    def rotateR(self,state):
        #edgesl est dans l'ordre d'une rotation de la face R
        edgesl = [2, 3, 4, 5]
        self.new_coins = copy.deepcopy(state[0]) #copie de la liste des coords des coins

#mise à jours des positions des coins
        for k in range(len(self.new_coins)):
            if self.coins[k][0]in edgesl:
                if edgesl.index(self.coins[k][0]) != (len(edgesl)-1):
                    self.new_coins[k][0]=edgesl[edgesl.index(self.coins[k][0])+1]
                else:
                    self.new_coins[k][0]=edgesl[0]
            else:
                pass
        
        self.coins = copy.deepcopy(self.new_coins)
        

#mise à jour des orientations de chaque coins
        for k in range(len(self.new_coins)):
            if self.coins[k][0] in edgesl:
                self.new_coins[k][1] = (self.new_coins[k][1] +1)%3
            else:
                pass
        
        self.coins = copy.deepcopy(self.new_coins)   



        #permutations des positions des arrêtes
        self.new_arretes = copy.deepcopy(state[1])  #copie de la liste des coords des coins
        arretesl = [2, 4, 6, 9]

        for k in range(len(self.new_arretes)):
            if self.arretes[k][0] in arretesl:
                if not self.new_coins[k][0]!= arretesl[arretesl.index(self.arretes[k][0])+1]:
                    self.new_arretes[k][0]-= 1
                else:
                    self.new_arretes[k][0]=3
            else:
                pass
        
        #mise à jour des orientations de chaque arrête
        for k in range(len(self.new_arretes)):
            if self.arretes[k][0] in arretesl:
                self.new_arretes[k][1] = (self.new_arretes[k][1] +1)%3
            else:
                pass
        
        self.arretes = copy.deepcopy(self.new_arretes)
        print([self.new_coins, self.arretes])

        self.state = [self.new_coins, self.arretes]
        return self.state
        



    def rotateU(self, state):
       #edgesl est dans l'ordre d'une rotation de la face R
        edgesl = [0, 3, 4, 7]
        self.new_coins = copy.deepcopy(state[0]) #copie de la liste des coords des coins

#mise à jours des positions des coins
        for k in range(len(self.new_coins)):
            if self.coins[k][0]in edgesl:
                if edgesl.index(self.coins[k][0]) != (len(edgesl)-1):
                    self.new_coins[k][0]=edgesl[edgesl.index(self.coins[k][0])+1]
                else:
                    self.new_coins[k][0]=edgesl[0]
            else:
                pass
        
        self.coins = copy.deepcopy(self.new_coins)
        

#mise à jour des orientations de chaque coins
        for k in range(len(self.new_coins)):
            if self.coins[k][0] in edgesl:
                self.new_coins[k][1] = (self.new_coins[k][1] +1)%3
            else:
                pass
        
        self.coins = copy.deepcopy(self.new_coins)



        #permutations des positions des arrêtes
        self.new_arretes = copy.deepcopy(state[1])  #copie de la liste des coords des coins
        arretesl = [11, 9, 8, 10]

        for k in range(len(self.new_arretes)):
            if self.arretes[k][0] in arretesl:
                if not self.new_coins[k][0]!= arretesl[arretesl.index(self.arretes[k][0])+1]:
                    self.new_arretes[k][0]-= 1
                else:
                    self.new_arretes[k][0]=3
            else:
                pass
        
        #mise à jour des orientations de chaque arrête
        for k in range(len(self.new_arretes)):
            if self.arretes[k][0] in arretesl:
                self.new_arretes[k][1] = (self.new_arretes[k][1] +1)%3
            else:
                pass
        
        self.arretes = copy.deepcopy(self.new_arretes)
        
        self.state = [self.new_coins, self.arretes]
        return self.state






    def rotateL(self, state):
        #edgesl est dans l'ordre d'une rotation de la face R
        edgesl = [0, 1, 4, 5]
        self.new_coins = copy.deepcopy(state[0]) #copie de la liste des coords des coins

#mise à jours des positions des coins
        for k in range(len(self.new_coins)):
            if self.coins[k][0]in edgesl:
                if edgesl.index(self.coins[k][0]) != 0:
                    self.new_coins[k][0]=edgesl[edgesl.index(self.coins[k][0])-1]
                else:
                    self.new_coins[k][0]=edgesl[-1]
            else:
                pass
        
        self.coins = copy.deepcopy(self.new_coins)
        

#mise à jour des orientations de chaque coins
        for k in range(len(self.new_coins)):
            if self.coins[k][0] in edgesl:
                self.new_coins[k][1] = (self.new_coins[k][1] +1)%3
            else:
                pass
        
        self.coins = copy.deepcopy(self.new_coins) 
    

    #permutations des positions des arrêtes
        self.new_arretes = copy.deepcopy(state[1])  #copie de la liste des coords des coins
        arretesl = [10, 11, 7, 0]

        for k in range(len(self.new_arretes)):
            if self.arretes[k][0] in arretesl:
                if not self.new_coins[k][0]!= arretesl[arretesl.index(self.arretes[k][0])+1]:
                    self.new_arretes[k][0]-= 1
                else:
                    self.new_arretes[k][0]=3
            else:
                pass
        
        #mise à jour des orientations de chaque arrête
        for k in range(len(self.new_arretes)):
            if self.arretes[k][0] in arretesl:
                self.new_arretes[k][1] = (self.new_arretes[k][1] +1)%3
            else:
                pass
        
        self.arretes = copy.deepcopy(self.new_arretes)

        state2 = [self.new_coins, self.arretes]
        return state2






    def rotateB(self, state):
       #edgesl est dans l'ordre d'une rotation de la face R
        edgesl = [7, 6, 5, 4]
        self.new_coins = copy.deepcopy(state[0]) #copie de la liste des coords des coins

#mise à jours des positions des coins
        for k in range(len(self.new_coins)):
            if self.coins[k][0]in edgesl:
                if edgesl.index(self.coins[k][0]) != 0:
                    self.new_coins[k][0]=edgesl[edgesl.index(self.coins[k][0])-1]
                else:
                    self.new_coins[k][0]=edgesl[-1]
            else:
                pass
        
        self.coins = copy.deepcopy(self.new_coins)
        

        

#mise à jour des orientations de chaque coins
        for k in range(len(self.new_coins)):
            if self.coins[k][0] in edgesl:
                self.new_coins[k][1] = (self.new_coins[k][1] +1)%3
            else:
                pass
        
        self.coins = copy.deepcopy(self.new_coins)   

        
        #permutations des positions des arrêtes
        self.new_arretes = copy.deepcopy(state[1])  #copie de la liste des coords des coins
        arretesl = [8, 6, 5, 11]

        for k in range(len(self.new_arretes)):
            if self.arretes[k][0] in arretesl:
                if not self.new_coins[k][0]!= arretesl[arretesl.index(self.arretes[k][0])+1]:
                    self.new_arretes[k][0]-= 1
                else:
                    self.new_arretes[k][0]=3
            else:
                pass
        
        #mise à jour des orientations de chaque arrête
        for k in range(len(self.new_arretes)):
            if self.arretes[k][0] in arretesl:
                self.new_arretes[k][1] = (self.new_arretes[k][1] +1)%3
            else:
                pass
        
        self.arretes = copy.deepcopy(self.new_arretes)
        

        state2 = [self.new_coins, self.arretes]
        return state2






    def rotateD(self, state):
        #edgesl est dans l'ordre d'une rotation de la face R
        edgesl = [0, 7, 4, 3]
        self.new_coins = copy.deepcopy(state[0]) #copie de la liste des coords des coins

#mise à jours des positions des coins
        for k in range(len(self.new_coins)):
            if self.coins[k][0]in edgesl:
                if edgesl.index(self.coins[k][0]) != 0:
                    self.new_coins[k][0]=edgesl[edgesl.index(self.coins[k][0])-1]
                else:
                    self.new_coins[k][0]=edgesl[-1]
            else:
                pass
        
        self.coins = copy.deepcopy(self.new_coins)
        

#mise à jour des orientations de chaque coins
        for k in range(len(self.new_coins)):
            if self.coins[k][0] in edgesl:
                self.new_coins[k][1] = (self.new_coins[k][1] +1)%3
            else:
                pass
        
        self.coins = copy.deepcopy(self.new_coins)   
    
    #permutations des positions des arrêtes
        self.new_arretes = copy.deepcopy(state[1])  #copie de la liste des coords des coins
        arretesl = [3, 4, 5, 7]

        for k in range(len(self.new_arretes)):
            if self.arretes[k][0] in arretesl:
                if not self.new_coins[k][0]!= arretesl[arretesl.index(self.arretes[k][0])+1]:
                    self.new_arretes[k][0]-= 1
                else:
                    self.new_arretes[k][0]=3
            else:
                pass
        
        #mise à jour des orientations de chaque arrête
        for k in range(len(self.new_arretes)):
            if self.arretes[k][0] in arretesl:
                self.new_arretes[k][1] = (self.new_arretes[k][1] +1)%3
            else:
                pass
        
        self.arretes = copy.deepcopy(self.new_arretes)
        
        state2 = [self.new_coins, self.arretes]
        return state2





    def move_M(self, state):
        # Sauvegarde l'état actuel des arêtes
        new_arretes = copy.deepcopy(state[0])

        # Exemple : Permutation des arêtes de la couche du milieu pour M
        # Supposons que les arêtes de la couche du milieu sont aux indices 4, 5, 6, 7
        new_arretes[4], new_arretes[5], new_arretes[6], new_arretes[7] = (
            self.arretes[5], self.arretes[6], self.arretes[7], self.arretes[4]
        )

        # Met à jour l'état des arêtes
        arretes2 = new_arretes

        return arretes2

    def move_E(self, state):
        # Sauvegarde l'état actuel des arêtes
        new_arretes = copy.deepcopy(state[0])

        # Exemple : Permutation des arêtes de la couche du milieu pour E
        new_arretes[4], new_arretes[5], new_arretes[6], new_arretes[7] = (
            self.arretes[6], self.arretes[4], self.arretes[7], self.arretes[5]
        )

        # Met à jour l'état des arêtes
        arretes2 = new_arretes

        return arretes2

    def move_S(self, state):
        # Sauvegarde l'état actuel des arêtes
        new_arretes = copy.deepcopy(state[0])

        # Exemple : Permutation des arêtes de la couche du milieu pour S
        new_arretes[4], new_arretes[5], new_arretes[6], new_arretes[7] = (
            self.arretes[7], self.arretes[5], self.arretes[4], self.arretes[6]
        )

        # Met à jour l'état des arêtes
        arretes2 = new_arretes

        return arretes2