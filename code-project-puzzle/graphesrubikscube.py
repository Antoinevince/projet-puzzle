#implémentation d'un BFS qui s'arrête à une certaine distance de la configuration initiale (cube résolu)
import queue
import coordinates

def configurations_voisinnes(c):
    lvoisins = []

    c_rotateF = coordinates.ClassicRubicksCube.rotateF(c)
    lvoisins.append(c_rotateF)

    c_rotateB = coordinates.ClassicRubicksCube.rotateB(c)
    lvoisins.append(c_rotateB)

    c_rotateL = coordinates.ClassicRubicksCube.rotateL(c)
    lvoisins.append(c_rotateL)

    c_rotateR = coordinates.ClassicRubicksCube.rotateR(c)
    lvoisins.append(c_rotateR)

    c_rotateU = coordinates.ClassicRubicksCube.rotateU(c)
    lvoisins.append(c_rotateU)

    c_rotateD = coordinates.ClassicRubicksCube.rotateD(c)
    lvoisins.append(c_rotateD)

    return lvoisins

#ce bfs permet de s'arrêter à une certaine distance distance de la configuration résolue du cube
def bfs_limit(m):
    a_voir = queue.Queue
    deja_vu = []
    a_voir.put([])

    compteur = 0

    while a_voir != queue.Empty:
        s = a_voir.get()
        deja_vu.append(s)
        if compteur < m:
            compteur+=1

            for k in configurations_voisinnes(s):
                if k not in deja_vu:
                    a_voir.put(k)
                    deja_vu.append(k)
        else:
            break

    return deja_vu
