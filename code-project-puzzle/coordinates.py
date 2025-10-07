""""
ce fichier sert à implémenter le système de coordonnées du rubik's cube, de la quarter turn metric
"""



"""on va représenter les configurations du cube sous forme de tableaux qui contiennent les mouvements qui ont permis d'arriver à cette configuration"""

#rubik's cube 3x3x3
class ClassicRubiksCube():

    def __init__(self, state):
        self.state = state
    
#les fonctions suivantes servent à gérer les différents mouvements que l'on peut faire sur les cube, et les interactions (ie si on fait un mouvement a, puis on effectue le mouvement inverse, il faut donc actualiser l'état du cube)
    
    def rotateF(self):

        if self.state[-1] != 'Fi':
            self.state.append('F')
        else: 
            self.state= self.state.pop()

        if self.state[-1] == 'F' and self.state[-2] == 'F' and self.state[-3] == 'F':
            self.state = self.state.pop()
            self.state = self.state.pop()
            self.state = self.state.pop()
            self.state.append('Fi')
        
        return self.state

    def rotateR(self):

        if self.state[-1] != 'Ri':
            self.state.append('R')
        else: 
            self.state= self.state.pop()

        if self.state[-1] == 'R' and self.state[-2] == 'R' and self.state[-3] == 'R':
            self.state = self.state.pop()
            self.state = self.state.pop()
            self.state = self.state.pop()
            self.state.append('Ri')
        
        return self.state

    def rotateU(self):
        if self.state[-1] != 'Ui':
            self.state.append('U')
        else: 
            self.state= self.state.pop()

        if self.state[-1] == 'U' and self.state[-2] == 'U' and self.state[-3] == 'U':
            self.state = self.state.pop()
            self.state = self.state.pop()
            self.state = self.state.pop()
            self.state.append('Ui')
        
        return self.state

    def rotateL(self):
        if self.state[-1] != 'Li':
            self.state.append('L')
        else: 
            self.state= self.state.pop()

        if self.state[-1] == 'L' and self.state[-2] == 'L' and self.state[-3] == 'L':
            self.state = self.state.pop()
            self.state = self.state.pop()
            self.state = self.state.pop()
            self.state.append('Li')
        
        return self.state

    def rotateB(self):
        if self.state[-1] != 'Bi':
            self.state.append('B')
        else: 
            self.state= self.state.pop()

        if self.state[-1] == 'B' and self.state[-2] == 'B' and self.state[-3] == 'B':
            self.state = self.state.pop()
            self.state = self.state.pop()
            self.state = self.state.pop()
            self.state.append('Bi')
        
        return self.state

    def rotateD(self):
        if self.state[-1] != 'Di':
            self.state.append('D')
        else: 
            self.state= self.state.pop()

        if self.state[-1] == 'D' and self.state[-2] == 'D' and self.state[-3] == 'D':
            self.state = self.state.pop()
            self.state = self.state.pop()
            self.state = self.state.pop()
            self.state.append('Di')
        
        return self.state


#cependant, à cause de la lourdeur en mémoire de ce type de représentation, nous allons en utiliser d'autres

def upgraded_representation():

    def __init__(self, corners, edges):
        self.corners = corners
        self.edges = edges

    