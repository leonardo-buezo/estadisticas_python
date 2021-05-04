import random

class Borracho:

    def __init__(self, nombre):
        self.nombre = nombre

""" Clase BorrachoTradicional que extiende de Borracho """
class BorrachoTradicional(Borracho):

    """ Generamos un constructor (con el __init__) """
    def __init__(self, nombre):
        super().__init__(nombre)
    """ Lo hacemos caminar aleatoriamente hacia arriba, abajo, derecha o izquierda """
    def camina(self):
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
