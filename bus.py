from vehicule import Vehicule
class Bus(Vehicule):


    def __init__(self,immatriculation,color):
        Vehicule.__init__(self,immatriculation,color)
        self.__number_floors=None

        @property
        def number_floors(self):
            return self.__number_floors

        @number_floors.setter
        def number_floors(self, new_value):
            if new_value in [1, 2]:
                self.__number_floors = new_value
            else:
                raise ValueError("le nombre d'etage doit etre 1 ou 2")